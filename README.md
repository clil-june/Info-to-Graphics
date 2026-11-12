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

Two Claude calls, then a check:

1. **Plan the story.** Claude reads the sources and the brief, then writes a plan with:
   - the reader's question and a headline that answers it
   - an intro with the denominator
   - the things that recur, each with a drawn symbol and a colour
   - 3–6 sections, each with its own question, a title that states its point, the form that fits the relationship, the exact numbers, a highlight and a callout
   - a takeaway, the source line and method notes
2. **Compose the page.** Claude lays out the plan in the app's page format (the `ig-*` classes in `index.html`). It's shown the Harvard page as its model of quality.
   - The app draws the data-driven parts itself, from the values: bar lengths, pictograms (repeated symbols, partly filled for fractions), dot charts (gridlines, gap lines and value labels), the key of symbols, and the takeaway's row of symbols. Positions and counts are exact, not eyeballed.
3. **Check the numbers.** Every number on the page is looked up in the sources, allowing for rounding. The page shows "Numbers checked" or lists any number to double-check.

The rules Claude follows, taken from `docs/visual-communication-research.md`, McCandless's "What Makes a Good Visualization?" and the Venngage guidance:
- Start from the reader's question.
- Titles state the point.
- Copy numbers exactly, with units and denominators, and keep "reported", "said" and "estimated".
- Visual first: symbols replace names.
- Choose the form by the relationship.
- One highlight per section, and less clutter.
- Compact sections side by side, with at most one dark panel.
- End with a takeaway, then sources and method notes, then the numbers as tables.

**Safety:** Claude's HTML is treated as untrusted. Only known tags, `ig-*` classes, safe inline styles and `http(s)` links survive. Scripts, event handlers, images and `url()` styles are removed.

## Where it runs

Info to Graphics is a single `index.html` with no build step.

Making and changing infographics, reading images and reading links all need Claude, so they only work when the page runs as an artifact on claude.ai (links also need the Claude desktop app). Opened anywhere else, the page shows the example and its saved infographics, reads PDF, Word and text files, and exports.

## Libraries

Loaded from CDNs: [pdf.js](https://mozilla.github.io/pdf.js/) and [mammoth.js](https://github.com/mwilliamson/mammoth.js). Fonts from Google Fonts: Bricolage Grotesque and Inter for the infographic, Schibsted Grotesk and IBM Plex Mono for the app.
