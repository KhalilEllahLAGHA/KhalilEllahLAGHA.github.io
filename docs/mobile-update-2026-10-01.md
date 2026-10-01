# Mobile portfolio update — 1 October 2026

## Layout and navigation

- Homepage portrait and profile highlights now appear above the longer introduction
  on phones. Project cards use one column below 768 px and two columns on tablets.
- Header controls, filters, report links and the back-to-top button have at least
  44 px touch targets. Mobile proof captions are at least 12 px.
- Mobile menus scroll within short landscape viewports and close after selecting a
  link, pressing Escape or tapping outside. The desktop breakpoint matches the CSS.
- Safe-area spacing accommodates device cutouts and the bottom gesture area.
- All six project pages have four compact, translated chapter tabs on phones.
  Full chapter names remain in accessible labels. Sticky navigation offsets keep
  chapter headings visible; figure links include an enlargement hint.
- Project titles and image cards scale to small screens. Existing language/theme
  persistence and reduced-motion support remain available.
- CSS and JavaScript references carry content versions to refresh cached assets.

## Downloads

The homepage links to a new French/English portfolio CV pair. Each PDF uses the
current portrait, verified CSEE profile, current M2 dates and availability. Both
are one tagged A4 page, with selectable text and five working contact annotations.
Sizes are 131,184 bytes (French) and 130,213 bytes (English). Existing historical
CV files and public project reports are preserved.

## Checks

- Homepage: 320 × 740, 360 × 800, 390 × 844, 430 × 932, 768 × 1024,
  844 × 390 landscape, and 1440 × 900. No horizontal document overflow or
  clipped primary headings, cards or controls.
- All six project pages: English at 320 px, without horizontal overflow or clipped
  primary content. French laboratory page also reviewed at 390 px.
- Landscape menu height stays inside the viewport and its final link is reachable.
  Navigation selection and Escape close it.
- Project chapter links land below the sticky bars; chapter targets are 44 px high.
- Language persists between homepage and projects; CV links switch to the English
  PDF. Local asset/document links, cache versions and JavaScript syntax checked.
- Both new CVs pass independent text extraction and visual layout review.

## Publication

Target repository: `KhalilEllahLAGHA/KhalilEllahLAGHA.github.io`, branch `main`.
This update includes the refreshed homepage, six illustrated project pages,
project visuals and the two new portfolio CV PDFs. It excludes the six existing
local CV modifications. The detailed workspace project guide remains in
`Projects/PROJECTS_DETAILED.md` outside the website repository.
