# Info to Graphics

Drop in sources, say in a sentence or two what the infographic should show, and get back a finished infographic page. There's no editor and no customization: the app's job is to make one high-quality infographic per brief, at the standard of the hand-made reference in `references/harvard-period-products-visual/`.

## Using it

1. **Drop your sources:** PDF, Word (.docx), text, CSV, JSON or image files, a link, or pasted text.
2. **Say what it should show.** A short outline, for example: "The main findings for design students. Compare the products, show how use changes with age, and end with what it means."
3. **Make the infographic.** This takes a minute or two.
4. **Ask for a change** in plain words ("Use fewer words", "Make the age section the main story"), or press **New layout**. Every version is kept, so you can step back through them.
5. **Export** the page as a standalone HTML file.

The app opens on an example made from the Harvard period-products study.

## How it makes an infographic

1. **Plan the whole page.** The plan identifies the main evidence for the opening and the relationship, drawing or chart, direct labels, and qualifications for each findings section.
2. **Compose the HTML.** Claude uses the page format and reusable visual components in `index.html`. The renderer turns declared numbers into bars, pictogram fills and dot positions. It also supports annotated SVG diagrams for routes, mechanisms and sequences.
3. **Review the rendered page.** When Claude can receive images, the app captures each visible section at 390 px, once as shown and once with explanatory prose hidden. Claude identifies specific problems. The app makes one targeted repair pass and captures the page again. The result shows whether review passed, still flagged an issue, or was unavailable.
4. **Check the numbers.** The page reports numeric strings it cannot match in the sources. This is a numeric lookup and does not validate every value's context or attribution.

The [visual communication guide](docs/visual-communication-research.md) describes the generation and review criteria. HTML export keeps supplementary details collapsed and uses local font fallbacks offline.

**Safety:** Claude's HTML is treated as untrusted. Only known tags, `ig-*` classes, safe inline styles and `http(s)` links survive. Scripts, event handlers, images and `url()` styles are removed.

## Where it runs

Info to Graphics is a single `index.html` with no build step.

Making and changing infographics, reading images and reading links all need Claude, so they only work when the page runs as an artifact on claude.ai (links also need the Claude desktop app). Opened anywhere else, the page shows the example and its saved infographics, reads PDF, Word and text files, and exports.

## Libraries

Loaded from CDNs: [pdf.js](https://mozilla.github.io/pdf.js/) and [mammoth.js](https://github.com/mwilliamson/mammoth.js). Fonts from Google Fonts: Bricolage Grotesque and Inter for the infographic, Schibsted Grotesk and IBM Plex Mono for the app.
