# Project explanations and FOC response context

Updated at Khalil's request on 1 November 2026.

- The seven bilingual case studies now state the engineering problem and show a short operating sequence before the optional calculation details. Existing reports and evidence remain available.
- The canonical FOC, DC-motor and neural-network SVGs use fixed-size arrow markers and endpoints at block boundaries. The HTML interview presentation embeds these same canonical assets. Its FOC slide shows the control chain rather than the speed result.
- The FOC explanation distinguishes the rotating reference frame, current-model flux estimate, slip-based orientation, d/q current control, inverse Park, SVPWM, gate commands and inverter power stage. The estimate supports orientation; frame alignment and feed-forward terms provide decoupling.
- `assets/projects/foc-response-context.png` contains four aligned views of one execution of the original Python scenario A: speed, applied/electromagnetic torque, d/q currents and rotor-flux magnitude. The simulation source and controller were unchanged. Python uses the averaged inverter; these curves are not hardware measurements.
- `projects/plot_foc_context.py` reproduces the figure with the original simulation directory supplied through `--simulation-source` when needed. It reports source hashes and numerical checks.

The same-run scenario builds flux before the first speed step, then requests 800 rpm at 0.30 s, applies a signed +10 N·m load at 0.55 s, requests 1,400 rpm at 0.80 s, slows to 600 rpm at 1.30 s and reverses to -800 rpm at 1.80 s. The load remains signed +10 N·m after reversal. Flux reference remains 0.8 Wb, without field weakening.

The added load produces a minimum near 731 rpm at 0.561 s. Current `iq` and electromagnetic torque show the controller's response, while `id` and the rotor-flux plot distinguish magnetisation from torque demand. A return within ±10 rpm occurs 57.7 ms after load application in this run; this defined threshold is separate from older settling-time conventions in the report.

Method references: [Imperix rotor-field-oriented control](https://imperix.com/doc/implementation/rotor-field-oriented-control), [Imperix space-vector modulation](https://imperix.com/doc/implementation/space-vector-modulation). These explain the method; the local project code and reports establish this project's implementation and results.

Validation uses the generated project pages in French and English, desktop and phone layouts, image/report links, canonical SVGs and the local HTML presentation. No CV or report is rebuilt as part of this update.
