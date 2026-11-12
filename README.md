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

### Visual first

Pictures carry the information by default, and words are kept for the point, units and qualifiers.

- **Symbols for recurring things.** Claude finds what recurs across your sources (products, places, people, objects) and draws one symbol for each, in a colour shared by related things. A **Key** at the top of the board introduces each symbol once, with its name. After that, figures show the symbol instead of the name, and repeat it to show amounts ("about 2 of 10 cups"). Click any symbol to rename it, recolour it, redraw it with Claude, or swap it for an icon. Changes apply everywhere it appears.
- **A question for every board and figure.** The board states the question a reader should be able to answer. Each figure carries its own question above its title.
- **Faithful wording.** If a source says people *reported* something, or calls a number an *estimate*, the title and callout say so too.
- **A text version.** "The numbers behind the pictures," at the end of the board, lists every figure's data as a table. It's always included in exports.
- **One designed page.** The board reads like a finished infographic. It opens with the question, a headline that states the story, a short intro and the key. Figures sit in open panels led by their question, two compact ones can share a row, and one can be dark for contrast. The page closes with a takeaway, the sources with method notes, and the tables. Editing marks only appear on the figure you select.
- **Dot chart.** Two or three groups of things compared across categories (for example pads vs tampons by age), with each thing's own symbol as the marker.
- **Less text by default.** New boards start on "Less text". Switch to "More" to show the names beside the symbols.

## Where it runs

Info to Graphics is a single `index.html` with no build step. Open it in a browser or host it on any static host (GitHub Pages, Netlify).

The Claude features (building a board, "Ask Claude", reading images and reading links) only work when the page runs as an artifact on claude.ai, because they use the viewer's own Claude account. Everywhere else, the editor, file reading for PDF/Word/text, saving boards in the browser, and export still work.

## Infographic design

See the [visual communication research guide](docs/visual-communication-research.md) for choosing visual forms, turning source text into graphics, and reviewing whether a figure communicates its intended takeaway.

## Libraries

Loaded from CDNs: [Lucide](https://lucide.dev) icons, [pdf.js](https://mozilla.github.io/pdf.js/) and [mammoth.js](https://github.com/mwilliamson/mammoth.js). Fonts: Schibsted Grotesk and IBM Plex Mono from Google Fonts.
