# Winding application walkthrough — 2 November 2026

The bilingual winding project page now follows the application's engineering workflow: winding parameters and phase drawing, machine geometry, resultant MMF, polar mesh, sparse Ax = b solve, branch fluxes, flux density B and the 2D display.

Six unedited screenshots were captured from the existing native PyQt5 application. They show one illustrative case: 36 slots, 2 pole pairs, double layer, coil span 9 slots, 204 turns, phase-current setting 0.5 A, electrical angle 90°, and the medium mesh preset (8,640 cells). The flux computation was rerun through the app after setting the excitation. The solver reported convergence. The screenshots are a numerical demonstration, without a claim of rated operation or experimental validation.

New assets in `assets/projects/`:

- `winding-parameters-app.png`: winding settings and stator phase layout.
- `winding-machine-app.png`: dimensions and cross-section preview.
- `winding-mmf-app.png`: phase MMFs and their resultant.
- `winding-mesh-app.png`: polar mesh and settings.
- `winding-flux-lines-app.png`: reconstructed flux paths.
- `winding-b-map-app.png`: magnetic flux-density magnitude map.

The implementation is a magnetic reluctance network on a polar grid. The unknown x in Ax = b is the nodal magnetic potential. Branch fluxes follow from potential differences, MMF sources and reluctances; the branch cross-sections then give B. This description follows `core/flux_solver.py`, `core/reluctance_calculator.py`, `core/meshing_engine.py`, `core/mmf_engine.py` and `ui/flux_visualization.py` in the linked project repository. It does not claim an explicit finite-difference PDE implementation. The model has prescribed permeabilities, without a saturation calculation; flux lines are interpolated and smoothed for display. FEMM is an optional numerical comparison.

The canonical generator remains `projects/build_project_pages.py`. It now permits figures within workflow steps; the other project pages render identically. The candidate's private French HTML deck uses the first winding interface and a short summary of the same chain. Existing CVs, reports and application source code were preserved.

Validation: all six images load; French/English switching and phone/desktop layouts checked in Edge; candidate slide 11 checked for clipping and phone overflow.
