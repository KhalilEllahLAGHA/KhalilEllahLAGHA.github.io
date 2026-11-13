# Winding project: Dolomites and multiphase study

Prepared on 13 November 2026 at Khalil's request for publication with the updated
application source.

## Content

The winding case study now describes the current PyQt6 interface, explicit phase
and layer metadata, the pinned Dolomites/Koil generator, cached sparse LU with
checked PCG fallback, and two-basis continuous field animation. Five screenshots
were refreshed from the verified packaged application's 1440 by 960 self-test.

The bilingual page links the detailed report by **LAGHA Khalil Ellah**, containing
the general algorithm followed by three double-layer studies:

| Phases | Slots | Total poles | Coil span in slots |
|---:|---:|---:|---:|
| 3 | 36 | 4 | 9 |
| 2 | 24 | 4 | 6 |
| 5 | 45 | 8 | 11 |

Exactly two HTML5 video players show the default and requested five-phase fields.
Both are silent H.264 MP4 files, 1280 by 720, 30 frames per second, 360 frames and
12 seconds per electrical cycle. Controls, inline playback, looping, poster
images and download links are provided; playback does not start automatically.
The legend remains fixed within each video, and the comparison text explicitly
warns that colour scales differ between cases.

The five-phase interpretation follows the calculated winding and harmonic data:
the 352-degree electrical throw gives a pitch factor of 0.06976 and working
winding factor of about 0.06863. Balanced 72-degree currents coexist with a strong
counter-rotating two-pole spatial MMF subharmonic and the weak intended eight-pole
wave. The page explains mixed spatial orders, contour deformation and poor
eight-pole current utilisation without reporting an uncalculated efficiency or
attributing a general disadvantage to five-phase machines.

Dolomites/Koil, its GPLv3 source and contributors, and Luigi Alberti's ICEM 2018
Koil article (DOI 10.1109/ICELMACH.2018.8507004) receive explicit credits. The
harmonic-loss discussion links to Brkovic and Jecmenica, *Machines* 2022, 10(5),
401 (DOI 10.3390/machines10050401). The earlier FEMM comparison remains clearly
identified as evidence from the 12 November audit, rather than a validation of
all new multiphase cases.

## Local verification

- The canonical source is `projects/build_project_pages.py`; only the winding
  HTML page was rendered, with dedicated additions in `projects/winding.css`.
- All 28 local HTML resource/link targets resolve, including both videos, both
  posters and the report; the DOM contains exactly two video players.
- Isolated headless Edge checks passed at 1440 and 360 pixels in French/English
  and dark/light modes, without page-level horizontal overflow, broken images or
  JavaScript exceptions. The historical comparison table retains its intended
  internal horizontal scroll on phones.
- Both MP4 players loaded 1280 by 720 video metadata with a 12-second duration and
  decoded/played frames after seeking to two seconds. No video playback error
  occurred.
- Desktop and phone screenshots of the hero, both video blocks and the five-phase
  interpretation were visually inspected. Private QA evidence and the source-to-
  portfolio asset hash manifest are under `tmp/multiphase-report/` in the parent
  workspace.
- The unrelated CV binaries and shared CSS/JS files were not edited. Shared
  stylesheet/script bytes match HEAD after newline normalisation; their existing
  working-copy newline differences were preserved.

The publication commit and live verification are recorded by the accompanying
workspace handoff after deployment.
