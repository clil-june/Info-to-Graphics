# Info to Graphics

Drop in sources, say in a sentence or two what the infographic should show, and get back a finished infographic page. There's no editor and no customization: the app's job is to make one high-quality infographic per brief, at the standard of the hand-made reference in `references/harvard-period-products-visual/`.

## Using it

1. **Drop your sources** on the start page: PDF, Word (.docx), text, CSV, JSON or image files, a link, or pasted text.
2. **Name the information you're after**, for example "Where do blue whales feed?"
3. **Generate.** The infographic builds on screen as Claude draws it.
4. **Change it** in plain words ("Use fewer words"), or press **Try a different picture**. Up to eight versions are kept, so you can step back through them.
5. **Export** it as a standalone HTML file.

## How it makes an infographic

1. **One Claude call.** The prompt holds the sources, the question, the poster rules and two hand-made examples. Claude answers with one themed poster: the subject's look (background, texture, fonts, colours), a short headline and one central drawing. Places get a built-in world map with real coastlines.
   Before drawing, Claude plans the composition, picks one drawing style suited to the subject (blueprint, linocut, ukiyo-e, flat vector, Art Deco, constructivist poster, isometric, stained glass and others) and checks the picture against a list of real failure modes. The method and style rules are adapted for SVG from [claude-drawing-skill](https://github.com/cloveric/claude-drawing-skill) by cloveric (MIT).
2. **Shown as it is written.** The page re-draws about every 0.7 seconds while the answer streams in.
3. **Check the numbers.** The page lists any number it cannot find in the sources. This is a numeric lookup and does not validate every value's context or attribution.

The [visual communication guide](docs/visual-communication-research.md) describes the design criteria.

**Safety:** Claude's HTML is treated as untrusted. Only known tags, `ig-*` classes, safe inline styles and `http(s)` links survive. Scripts, event handlers, images and `url()` styles are removed.

## Where it runs

Info to Graphics is a single `index.html` with no build step.

Making and changing infographics, reading images and reading links all need Claude, so they only work when the page runs as an artifact on claude.ai (links also need the Claude desktop app). Opened anywhere else, the page shows the example and its saved infographics, reads PDF, Word and text files, and exports.

## Libraries

[pdf.js](https://mozilla.github.io/pdf.js/) and [mammoth.js](https://github.com/mwilliamson/mammoth.js) load from cdnjs only when a PDF or Word file is first added. Fonts come from Google Fonts: Varela Round and Inter for the app, and any family a poster names. The world map is Natural Earth 1:110m (public domain) from the `world-atlas` package, inlined.
