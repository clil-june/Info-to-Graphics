# Sieve

Sieve turns sources (files, links and pasted text) into a board of editable, icon-led figures: timelines, processes, hubs, cycles, pictograms, rings, bar charts, comparison tables, icon cards and simple illustrations.

## Using it

- **Add sources** on the left: drop PDF, Word (.docx), text, CSV, JSON or image files, paste a link, or paste text.
- **Build board from sources** asks Claude to lay out figures using only facts from your sources.
- **Edit** by clicking any text or icon on the board. Select a figure to change its form, layout or colour, or ask Claude to change it.
- **Export** the board as a web page, an SVG image, or an editable `.sieve.json` file you can open again later.

## Where it runs

Sieve is a single `index.html` with no build step. Open it in a browser or host it on any static host (GitHub Pages, Netlify).

The Claude features (building a board, "Ask Claude", reading images and reading links) only work when the page runs as an artifact on claude.ai, because they use the viewer's own Claude account. Everywhere else, the editor, file reading for PDF/Word/text, saving boards in the browser, and export still work.

## Libraries

Loaded from CDNs: [Lucide](https://lucide.dev) icons, [pdf.js](https://mozilla.github.io/pdf.js/) and [mammoth.js](https://github.com/mwilliamson/mammoth.js). Fonts: Schibsted Grotesk and IBM Plex Mono from Google Fonts.
