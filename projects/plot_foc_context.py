"""Plot one unchanged FOC scenario with shared time axes.

Run from this workspace (NumPy and Matplotlib required):
    python Portfolio/csee-github-pages/projects/plot_foc_context.py

The default input is Projects/foc-induction-motor/python/main.py.  Only its
run_simulation() function is called: scenario A is rerun once, without changing
the motor, control gains, references, limits or integration.  Existing project
figures are not overwritten.  All four panels use the same returned signal log.
The Python experiment uses the documented averaged SVPWM inverter, not hardware
measurements or the separately documented switched Simscape implementation.
Use --simulation-source to locate the original Python project elsewhere.

The script prints input hashes, event values and validation metrics so the
generated illustration can be audited without introducing a second data source.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


BLUE = "#2676cc"
ORANGE = "#d55a30"
GREEN = "#07845c"
INK = "#172c38"
MUTED = "#647583"
GRID = "#dce4e8"
BACKGROUND = "#fcfdfd"


def load_simulation(source: Path):
    """Load the documented source without calling its file-writing main()."""
    source = source.resolve()
    sys.path.insert(0, str(source))
    spec = importlib.util.spec_from_file_location("foc_original_scenario", source / "main.py")
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load the FOC source in {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_and_summarize(r: dict, sim, source: Path) -> dict:
    t = r["t"]
    required = ("omega_ref", "omega_m", "t_load", "te", "i_d", "i_q", "psi_r_mag")
    for key in required:
        if r[key].shape != t.shape or not np.all(np.isfinite(r[key])):
            raise ValueError(f"Invalid or unaligned signal: {key}")
    if not np.all(np.diff(t) > 0):
        raise ValueError("Time samples must increase strictly")
    rpm_factor = 60.0 / (2.0 * math.pi)
    speed = r["omega_m"] * rpm_factor
    speed_ref = r["omega_ref"] * rpm_factor
    events = [("A", 0.30), ("B", 0.55), ("C", 0.80), ("D", 1.30), ("E", 1.80)]
    event_values = []
    for tag, instant in events:
        k = int(np.argmin(np.abs(t - instant)))
        event_values.append({
            "tag": tag, "time_s": float(t[k]), "speed_reference_rpm": float(speed_ref[k]),
            "speed_simulated_rpm": float(speed[k]), "load_torque_Nm": float(r["t_load"][k]),
            "electromagnetic_torque_Nm": float(r["te"][k]),
            "rotor_flux_Wb": float(r["psi_r_mag"][k]),
        })
    load_window = (t >= 0.55) & (t < 0.80)
    k_min = np.flatnonzero(load_window)[np.argmin(speed[load_window])]
    return_window = np.flatnonzero(load_window & (np.abs(speed - 800.0) > 10.0))
    load_recovery_s = float(t[return_window[-1]] + sim.TS_CONTROL - 0.55) if len(return_window) else 0.0
    post_startup = t >= 0.50
    source_paths = ("main.py", "control/foc.py", "control/pid.py", "models/induction_motor.py", "models/inverter.py")
    return {
        "experiment": "Original Python scenario A, unchanged; same run in every panel",
        "inverter_mode": sim.PWM_MODE, "controller_sample_s": sim.TS_CONTROL,
        "integration_substeps": sim.N_SUBSTEPS, "samples": len(t),
        "simulated_duration_s": float(t[-1] + sim.TS_CONTROL),
        "simulation_wall_s": round(float(r["wall_time"]), 3),
        "source_sha256": {p: hashlib.sha256((source / p).read_bytes()).hexdigest() for p in source_paths},
        "events": event_values,
        "load_step_minimum": {"time_s": float(t[k_min]), "speed_rpm": float(speed[k_min]),
                              "dip_from_800_rpm": float(800.0 - speed[k_min]),
                              "return_within_10_rpm_after_load_step_s": load_recovery_s},
        "flux_reference_Wb": float(r["psi_ref"]),
        "flux_after_0_50_s_min_max_Wb": [float(np.min(r["psi_r_mag"][post_startup])),
                                         float(np.max(r["psi_r_mag"][post_startup]))],
        "final": {"speed_rpm": float(speed[-1]), "load_torque_Nm": float(r["t_load"][-1]),
                  "electromagnetic_torque_Nm": float(r["te"][-1]),
                  "id_A": float(r["i_d"][-1]), "iq_A": float(r["i_q"][-1]),
                  "rotor_flux_Wb": float(r["psi_r_mag"][-1])},
        "load_sign_note": "The original model imposes signed +10 Nm after 0.55 s, including after reversal; it does not reverse a resistive load with speed.",
    }


def plot_context(r: dict, output: Path) -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10.5,
        "text.color": INK, "axes.labelcolor": INK, "axes.titlecolor": INK,
        "axes.edgecolor": "#adbdc5", "xtick.color": MUTED, "ytick.color": MUTED,
        "axes.spines.top": False, "axes.spines.right": False,
        "figure.facecolor": BACKGROUND, "axes.facecolor": BACKGROUND,
        "savefig.facecolor": BACKGROUND, "axes.grid": True,
        "grid.color": GRID, "grid.linewidth": 0.7,
        "legend.frameon": False, "legend.fontsize": 10.0,
        "lines.linewidth": 1.85,
    })
    fig, axes = plt.subplots(4, 1, sharex=True, figsize=(12.5, 11.9),
                              gridspec_kw={"height_ratios": [1.35, 1.0, 1.0, 0.95]})
    fig.subplots_adjust(left=0.10, right=0.97, top=0.80, bottom=0.085, hspace=0.40)
    fig.suptitle("FOC : comprendre la réponse du moteur\nReading the motor response", x=0.10, y=0.98,
                 ha="left", va="top", fontsize=21, fontweight="bold", linespacing=1.3)
    fig.text(0.10, 0.899, "Simulation Python · moteur asynchrone / induction motor 5 kW · SVPWM moyennée / averaged", fontsize=10.5, color=MUTED)
    fig.text(0.10, 0.866, "A  0,30 s → 800 tr/min     B  0,55 s → charge / load +10 N·m     C  0,80 s → 1 400 tr/min", fontsize=10.5, color=INK)
    fig.text(0.10, 0.840, "D  1,30 s → 600 tr/min     E  1,80 s → −800 tr/min     Flux visé / target flux : 0,80 Wb", fontsize=10.5, color=INK)

    t = r["t"]
    rpm = 60.0 / (2.0 * math.pi)
    events = [("A", 0.30), ("B", 0.55), ("C", 0.80), ("D", 1.30), ("E", 1.80)]
    for ax in axes:
        ax.set_xlim(0.0, 2.4)
        ax.axvspan(0.0, 0.30, color=GREEN, alpha=0.045, zorder=0)
        for tag, instant in events:
            ax.axvline(instant, color=ORANGE if tag == "B" else "#9cabb4", lw=0.85,
                       ls=":" if tag == "B" else "--", alpha=0.70, zorder=0)
        ax.margins(x=0)
        ax.tick_params(axis="both", labelsize=9.5)

    ax = axes[0]
    ax.set_title("1  Vitesse / Speed", loc="left", fontsize=12, fontweight="bold", pad=10)
    ax.plot(t, r["omega_ref"] * rpm, "--", color=MUTED, lw=1.45, label="Consigne / Reference")
    ax.plot(t, r["omega_m"] * rpm, color=BLUE, label="Simulation")
    ax.set_ylabel("tr/min · rpm")
    ax.set_ylim(-950, 1650)
    ax.set_yticks([-800, 0, 800, 1400])
    ax.legend(loc="lower left", ncol=2)
    for tag, instant in events:
        ax.text(instant, 0.97, tag, transform=ax.get_xaxis_transform(), ha="center", va="top",
                fontsize=9, fontweight="bold", color=ORANGE if tag == "B" else MUTED,
                bbox={"facecolor": BACKGROUND, "edgecolor": "none", "alpha": 0.85, "pad": 0.6})
    load_window = (t >= 0.55) & (t < 0.80)
    k_min = np.flatnonzero(load_window)[np.argmin(r["omega_m"][load_window])]
    ax.annotate("Creux de vitesse sous charge\nLoad causes a brief speed dip", xy=(t[k_min], r["omega_m"][k_min] * rpm),
                xytext=(0.70, 245), fontsize=9.0, color=INK,
                arrowprops={"arrowstyle": "-", "lw": 0.9, "color": ORANGE},
                bbox={"facecolor": BACKGROUND, "edgecolor": "none", "alpha": 0.88, "pad": 2})

    ax = axes[1]
    ax.set_title("2  Couples / Torques", loc="left", fontsize=12, fontweight="bold", pad=10)
    ax.plot(t, r["t_load"], "--", color=MUTED, lw=1.5, label="Charge imposée / Applied load")
    ax.plot(t, r["te"], color=ORANGE, label="Électromagnétique / Motor")
    ax.set_ylabel("N·m")
    ax.set_ylim(-42, 43)
    ax.set_yticks([-35, 0, 10, 35])
    ax.legend(loc="lower left", ncol=2)

    ax = axes[2]
    ax.set_title("3  Deux rôles de courant / Two current roles", loc="left", fontsize=12, fontweight="bold", pad=10)
    ax.plot(t, r["i_d"], color=GREEN, label="id : flux")
    ax.plot(t, r["i_q"], color=ORANGE, label="iq : couple / torque")
    ax.set_ylabel("A")
    ax.set_ylim(-23, 24)
    ax.set_yticks([-20, 0, 12, 20])
    ax.legend(loc="lower left", ncol=2)

    ax = axes[3]
    ax.set_title("4  Flux rotorique / Rotor flux", loc="left", fontsize=12, fontweight="bold", pad=10)
    ax.axhline(r["psi_ref"], color=MUTED, ls="--", lw=1.4, label="Consigne / Reference")
    ax.plot(t, r["psi_r_mag"], color=GREEN, label="Module simulé / Simulated magnitude")
    ax.set_ylabel("Wb")
    ax.set_ylim(-0.04, 0.98)
    ax.set_yticks([0, 0.4, 0.8])
    ax.legend(loc="lower right", ncol=2)
    ax.annotate("Établissement du flux\nFlux builds up", xy=(0.125, np.interp(0.125, t, r["psi_r_mag"])),
                xytext=(0.34, 0.27), fontsize=9.0,
                arrowprops={"arrowstyle": "-", "lw": 0.9, "color": GREEN})
    ax.text(1.07, 0.45, "Puis maintenu près de 0,80 Wb\nThen held near 0.80 Wb", fontsize=9.3, color=GREEN)
    ax.set_xticks([0.0, 0.30, 0.55, 0.80, 1.30, 1.80, 2.40])
    ax.set_xticklabels(["0", "0,30", "0,55", "0,80", "1,30", "1,80", "2,40"])
    ax.set_xlabel("Temps / Time [s]", labelpad=7)

    fig.text(0.10, 0.025, "Même simulation sur les quatre panneaux · Same run in all four panels · Aucune mesure sur banc / No hardware measurements", fontsize=9.0, color=MUTED)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=150, metadata={"Title": "FOC response context: one unchanged Python simulation",
                                           "Description": "Aligned speed, torque, control-current and rotor-flux traces; averaged SVPWM scenario A."})
    plt.close(fig)


def main() -> None:
    script = Path(__file__).resolve()
    workspace = script.parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--simulation-source", type=Path, default=workspace / "Projects/foc-induction-motor/python")
    parser.add_argument("--output", type=Path, default=script.parent.parent / "assets/projects/foc-response-context.png")
    args = parser.parse_args()
    source = args.simulation_source.resolve()
    sim = load_simulation(source)
    r = sim.run_simulation(sim.SPEED_SEGMENTS, sim.LOAD_STEPS, sim.T_END)
    report = validate_and_summarize(r, sim, source)
    plot_context(r, args.output)
    report["output"] = str(args.output.resolve())
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
