# Homepage update — 30 September 2026

The main portfolio was redesigned locally to introduce the six detailed project
pages created in this session. This update has not been published.

## Changes

- Split introduction with the current portrait, a three-line technical statement,
  concise proof points, and direct project/CV/contact actions.
- Projects moved near the top, with six real image previews, result summaries,
  category filters, and links to the detailed case studies and existing sources.
- Shorter navigation and a clearer sequence: projects, background, experience,
  education, skills, documents, contact.
- Navy/amber and light themes, revised typography and spacing, image hover effects,
  scroll reveals, and a mobile navigation menu.
- Profile-aligned copy: M2 in progress (09/2026–08/2027), internship of 4–6 months
  from mid-March 2027, a 10-cell PEMFC stack, and participation in the industrial HMI.
- Skills distinguish project practice from theoretical knowledge. Collaborative
  work is labelled; placeholder repository promises were removed.
- Share preview refreshed with the correct name and availability. Page metadata
  and image/link accessible labels follow the selected language.

The portrait is a 640 × 800 WebP display copy of
`Documents/assets/photo-2026-09-30.png` (32,558 bytes). It preserves the original
proportions and likeness. Project image previews reuse the existing project assets.
Existing CVs, public reports, and approved evidence documents were not rebuilt.

## Verification

- Desktop (1440 × 900), tablet (768 × 1024), and phone (360 × 800) inspected in the
  browser; no document overflow or clipped primary content was found.
- French/light and English/dark layouts inspected. Language and theme persist
  when opening a project page and returning to the homepage.
- Category filters return six projects for All, two for Control, and one for AI;
  the selection is announced through an accessible status message.
- Mobile menu opens and closes with Escape and with a navigation selection.
  Keyboard Enter expands a skill detail; its full contents fit.
- All seven homepage images load. Local links/assets, image dimensions/alt text,
  unique IDs, translation keys, and pure-text translation containers were checked.
- JavaScript syntax and Git whitespace checks pass. Browser console has no errors
  or warnings during the checked interactions.
- CSS inspection confirms visible content without JavaScript, readable mobile
  navigation without JavaScript, and reduced-motion overrides. A file-protocol
  browser check was unavailable under the browser tool's URL policy.

No simulations were rerun and no performance/accessibility score is claimed.

## Maintenance

Edit homepage structure and French text in `index.html`, English text and behaviour
in `js/main.js`, and styling in `css/style.css`. The stylesheet contains the original
base rules followed by the homepage redesign overrides. Its HTML references use
content hashes to refresh cached CSS and JavaScript; update those hashes after
changing the corresponding asset.

Detailed case-study content remains in `projects/build_project_pages.py`; see
`projects/README.md` for its build command. The workspace Markdown project guide
remains `Projects/PROJECTS_DETAILED.md`.
