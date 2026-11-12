# Info to Graphics

Info to Graphics turns sources (files, links and pasted text) into a board of editable, icon-led figures: timelines, processes, hubs, cycles, pictograms, rings, bar charts, comparison tables, icon cards and simple illustrations.

## Using it

- **Add sources** on the left: drop PDF, Word (.docx), text, CSV, JSON or image files, paste a link, or paste text.
- **Build board from sources** asks Claude to lay out figures using only facts from your sources.
- **Edit** by clicking any text or icon on the board. Select a figure to change its form, layout or colour, or ask Claude to change it.
- **Export** the board as a web page, an SVG image, or an editable `.board.json` file you can open again later.

## Design approach

Every figure is built around the four elements from David McCandless's ["What Makes a Good Visualization?"](https://informationisbeautiful.net/visualizations/what-makes-a-good-data-visualization/):

- **Information:** facts from your sources. Each figure is tagged with the sources it uses.
- **Story:** the one point the figure makes. Titles state that point ("Dessau was its longest home") rather than naming a topic ("Years per city").
- **Goal:** what the viewer can understand or decide after seeing it.
- **Visual idea:** a form that echoes the subject, such as a winding road for a journey, rows of the subject's own icon for counts, or one oversized number when one number is the story.

Each figure keeps these in an editable **brief**. It also highlights the item that carries the story, with a short callout on it. Four small marks in the figure header show which elements are present. A missing one is named: no story is *boring*, no goal is *useless*, and neither is *eye candy*. **Fill what's missing with Claude** completes the brief. The board as a whole has a one-sentence story and an audience at the top.

The app uses McCandless's framework but doesn't include his graphic.

## Where it runs

Info to Graphics is a single `index.html` with no build step. Open it in a browser or host it on any static host (GitHub Pages, Netlify).

The Claude features (building a board, "Ask Claude", reading images and reading links) only work when the page runs as an artifact on claude.ai, because they use the viewer's own Claude account. Everywhere else, the editor, file reading for PDF/Word/text, saving boards in the browser, and export still work.

## Infographic design

See the [visual communication research guide](docs/visual-communication-research.md) for choosing visual forms, turning source text into graphics, and reviewing whether a figure communicates its intended takeaway.

## Libraries

Loaded from CDNs: [Lucide](https://lucide.dev) icons, [pdf.js](https://mozilla.github.io/pdf.js/) and [mammoth.js](https://github.com/mwilliamson/mammoth.js). Fonts: Schibsted Grotesk and IBM Plex Mono from Google Fonts.
