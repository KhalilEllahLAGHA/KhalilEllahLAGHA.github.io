# Project case studies

Six standalone project pages extend the existing portfolio. Each page contains
French and English content, a visual introduction, four reading chapters,
documented results, source links, and navigation to the next project.

## Pages

- [Power-grid analysis](power-grid-analysis.html)
- [Field-oriented control](foc-induction-motor.html)
- [Winding and flux analysis](winding-flux-analysis.html)
- [DC-motor cascade control](dc-motor-cascade-control.html)
- [MLP and backpropagation](mlp-backpropagation.html)
- [Power-electronics laboratories](power-electronics-labs.html)

## Editing and rebuilding

`build_project_pages.py` is the editable source for the bilingual copy, image
captions, report links, and page structure. Edit this source, then run:

```sh
python projects/build_project_pages.py
```

Run the command from the portfolio root. The builder uses Python's standard
library and writes the six HTML files into this directory. Styling and browser
behaviour are maintained directly in `project.css` and `project.js`.

To preview the portfolio locally from its root:

```sh
python -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/index.html#projets`.

## Content and visuals

Personal facts follow `Profile/CSEE/CV.md` in the parent workspace. Detailed
technical evidence comes from the six project folders and their reports; the
companion editable guide is `Projects/PROJECTS_DETAILED.md`.

The PNG and JPEG assets in `../assets/projects/` are display copies of existing
project plots, application views, or laboratory-report figures. Original project
assets and reports are preserved. The three SVG diagrams explain the FOC, DC
motor, and MLP architectures; they are explanatory drawings, not measurements.
Reported simulation and laboratory results were not rerun during this portfolio
update.

The third power-electronics experiment documents theory and bench measurements;
the MATLAB/Simulink work belongs to the first two experiments. The winding tool
and laboratory work are presented as collaborative projects.

## Checks completed on 30 September 2026

- Six pages checked at 360, 768, and 1440 pixels without horizontal overflow.
- French/English and light/dark selections persist between the main portfolio
  and the project pages.
- Local page links, image paths, document targets, and Markdown links resolve.
- Project images load, SVG files parse, and the JavaScript syntax checks pass.
- Reduced-motion preferences disable the decorative animation and smooth scroll.

The pages are static, require no runtime framework, and show French content by
default. They were built and previewed locally on that date; publication was not
requested during that check. The subsequent mobile refinements and GitHub
publication scope are recorded in [the 1 October update](../docs/mobile-update-2026-10-01.md).
External repository addresses are retained from the project documentation; live
GitHub availability was not confirmed by the web tool during the final check.
