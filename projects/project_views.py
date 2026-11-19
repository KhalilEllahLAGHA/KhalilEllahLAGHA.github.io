"""Shared bilingual figures for the homepage and the individual project stories."""
from dataclasses import dataclass
from hashlib import sha256
from html import escape
import re


@dataclass(frozen=True)
class View:
    file: str
    label: tuple[str, str]
    caption: tuple[str, str]
    background: str = "paper"
    movie: str | None = None


VIEWS = {
    "foc-induction-motor": [
        View("foc-signal-flow.svg", ("Commande", "Control"), ("Les boucles de vitesse et de courant pilotent l’onduleur triphasé.", "The speed and current loops control the three-phase inverter."), "navy"),
        View("foc-speed-trace.webp", ("Vitesse", "Speed"), ("La vitesse simulée suit la consigne jusqu’à l’inversion à −800 tr/min.", "The simulated speed follows the reference through reversal to −800 rpm."), "navy"),
        View("foc-dq-trace.webp", ("Courants", "Currents"), ("Dans le repère du flux rotorique, le courant d règle l’aimantation et le courant q le couple.", "In the rotor-flux frame, the d-axis current controls magnetisation and the q-axis current controls torque."), "navy"),
    ],
    "power-grid-analysis": [
        View("ieee14-topology.svg", ("Topologie", "Topology"), ("Cas IEEE 14. Les 20 branches relient les nœuds slack, PV et PQ.", "IEEE 14-bus case. Its 20 branches connect the slack, PV and PQ buses."), "sage"),
        View("grid-loadflow-iterations.png", ("Convergence", "Convergence"), ("Nombre d’itérations des trois méthodes de calcul du load flow.", "Iteration counts for the three load-flow methods.")),
    ],
    "winding-flux-analysis": [
        View("winding-field-45.webp", ("Champ", "Field"), ("Champ calculé à 90° électriques pour 45 encoches, 8 pôles et 5 phases.", "Computed field at 90 electrical degrees for 45 slots, 8 poles and 5 phases."), "navy"),
        View("winding-mesh-app.png", ("Maillage", "Mesh"), ("La vue de maillage de l’application discrétise la section de la machine.", "The app’s mesh view divides the machine cross-section into cells.")),
        View("winding-five-phase-flux-poster.jpg", ("Animation", "Animation"), ("Animation du champ et des courants du bobinage pentaphasé, avec un pas de 5 encoches.", "Field and current animation for the five-phase winding with a five-slot coil span."), "navy", "winding-five-phase-flux.mp4"),
    ],
    "dc-motor-cascade-control": [
        View("dc-feedback-loops.svg", ("Cascade", "Cascade"), ("Le PI de vitesse fixe la consigne de courant. Le PID de courant commande le pont à thyristors.", "The speed PI sets the current reference. The current PID controls the thyristor bridge."), "sage"),
        View("dc-motor-response.png", ("Réponse", "Response"), ("Réponses normalisées des boucles de courant et de vitesse du modèle moyen.", "Normalised current- and speed-loop responses from the averaged model.")),
    ],
    "mlp-backpropagation": [
        View("mlp-weight-flow.svg", ("Architecture", "Architecture"), ("Deux entrées, deux neurones cachés et une sortie. Le gradient sert à corriger les poids.", "Two inputs, two hidden neurons and one output. The gradient updates the weights."), "plum"),
        View("mlp-sequential-training.png", ("Apprentissage", "Training"), ("Évolution de l’erreur lors de l’apprentissage successif des trois exemples.", "Error over successive training on the three examples.")),
    ],
    "power-electronics-labs": [
        View("diode-bridge.svg", ("Circuit", "Circuit"), ("Un pont triphasé à six diodes alimente une charge résistive.", "A three-phase six-diode bridge supplies a resistive load."), "sage"),
        View("rectifier-scope.webp", ("Oscilloscope", "Oscilloscope"), ("Tension redressée du pont complet, relevée à l’oscilloscope pendant le TP.", "Full-bridge rectified voltage recorded on the oscilloscope during the lab."), "navy"),
    ],
    "pemfc-internship": [
        View("pemfc-identification-fr.svg", ("Méthode", "Workflow"), ("Cellules 3 à 9. Ajustement sur 269 échantillons, puis test sur les 116 suivants du même essai.", "Cells 3–9. The model was fitted to 269 samples and tested on the next 116 from the same run."), "navy"),
        View("pemfc-holdout.png", ("Résultats", "Results"), ("Comparaison des tensions mesurées et prédites sur la fenêtre de test chronologique.", "Measured and predicted voltages over the chronological test window.")),
    ],
}


def bilingual(pair):
    return ''.join(f'<span lang="{lang}">{escape(value)}</span>' for lang, value in zip(("fr", "en"), pair))


def render_views(slug, location, original=None):
    """Primary images work without JavaScript. Alternate views load on demand."""
    views = list(VIEWS[slug])
    prefix = "../assets/projects/" if location == "story" else "assets/projects/"
    if location == "story":
        file, _, _, caption_fr, caption_en = original
        names = {
            "foc-induction-motor": ("Schéma détaillé", "Full diagram"),
            "power-grid-analysis": ("Application", "Application"),
            "winding-flux-analysis": ("Paramètres", "Parameters"),
            "dc-motor-cascade-control": ("Schéma détaillé", "Full diagram"),
            "mlp-backpropagation": ("Schéma détaillé", "Full diagram"),
            "power-electronics-labs": ("Schéma du TP", "Lab diagram"),
            "pemfc-internship": ("Banc", "Bench"),
        }
        initial = View(file, names[slug], (caption_fr, caption_en))
        views.insert(0 if slug == "winding-flux-analysis" else len(views), initial)
    elif location == "card" and slug == "foc-induction-motor":
        views = [views[1], views[0]]
    elif location == "hero":
        assert slug == "foc-induction-motor"

    figures, buttons = [], []
    for index, view in enumerate(views):
        identifier = f"{location}-{slug}-{index}"
        source = prefix + view.file
        alternate = source.replace('-fr.svg', '-en.svg') if view.file.endswith('-fr.svg') else source
        href = f"projects/{slug}.html" if location == "card" else source
        target = '' if location == "card" else ' target="_blank" rel="noopener"'
        action = ("Ouvrir le projet", "Open project") if location == "card" else ("Agrandir la figure", "Enlarge figure")
        src = f'src="{source}"' if index == 0 else f'data-file="{source}"'
        localised = f' data-source-fr="{source}" data-source-en="{alternate}"' if alternate != source else ''
        hint = 'fetchpriority="high"' if location != "card" and index == 0 else 'loading="lazy" decoding="async"'
        media = (
            f'<a class="view-image {view.background}" href="{href}"{target} data-figure-link="{location}">'
            f'<img {src}{localised} width="760" height="396" alt="{escape(view.caption[0])}" '
            f'data-figure-alt-fr="{escape(view.caption[0])}" data-figure-alt-en="{escape(view.caption[1])}" {hint}>'
            f'<span class="view-action">{bilingual(action)}</span></a>')
        if view.movie:
            media = (f'<video class="view-movie" controls playsinline preload="none" '
                     f'data-movie="{prefix}{view.movie}" data-poster="{source}" '
                     f'aria-describedby="{identifier}-caption"></video>')
        figures.append(
            f'<figure id="{identifier}" class="view-panel"{"" if index == 0 else " hidden"}>{media}'
            f'<figcaption id="{identifier}-caption">{bilingual(view.caption)}</figcaption></figure>')
        buttons.append(f'<button type="button" aria-controls="{identifier}" aria-pressed="{str(index==0).lower()}">{bilingual(view.label)}</button>')
    return ('<div class="project-views" data-project-views><div class="view-stage">'+''.join(figures)+'</div>'
            '<div class="view-switcher" role="group" aria-label="Vues du projet" data-views-group hidden>'+''.join(buttons)+'</div></div>')


def refresh_homepage(destination):
    """Update only the explicitly marked figures in the hand-authored home page."""
    html = destination.read_text(encoding="utf-8")
    def update(match):
        slug = match.group(1)
        return f'<!-- views card {slug} -->\n{render_views(slug, "card")}\n<!-- /views -->'
    rebuilt, count = re.subn(r'<!-- views card ([\w-]+) -->.*?<!-- /views -->', update, html, flags=re.S)
    if count != len(VIEWS):
        raise ValueError("Expected one project viewer per card")
    def version(match):
        path = match.group(1)
        content = (destination.parent / path).read_bytes().replace(b'\r\n', b'\n')
        return f'{path}?v={sha256(content).hexdigest()[:12]}'
    rebuilt = re.sub(r'(css/(?:style|project-views)\.css|js/(?:main|project-views)\.js)(?:\?v=[a-f0-9]+)?(?=")', version, rebuilt)
    if html != rebuilt:
        destination.write_text(rebuilt, encoding="utf-8")
