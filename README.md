# Info to Graphics

Drop in sources, say in a sentence or two what the infographic should show, and get back a finished infographic page. The app's job is to make one high-quality infographic per brief, at the standard of the hand-made reference in `references/harvard-period-products-visual/`.

## Using it

1. **Drop your sources** on the start page: PDF, Word (.docx), text, CSV, JSON or image files, a link, or pasted text.
2. **Name the information you're after**, for example "Where do blue whales feed?"
3. **Choose an output format** with the button beside the source field. It shows the selected format and opens a list with three options.
   - **Presentation (1920 × 1080 px, 16:9)** for projection. Show the shortest accurate answer in large type and one dominant visual. Use a side-by-side composition or a wide figure where the subject calls for it.
   - **Instagram (1080 × 1350 px, 4:5)** for reading top to bottom on a phone. Place values directly on the artwork, then add a short comparison or explanation if it helps. This is the default.
   - **Print (3508 × 4961 px)** for one portrait page, with room for a short explanation or method note.
4. **Generate.** The infographic builds on screen as Claude draws it.
5. **Keep working in the editor.** The editor opens with the displayed version’s question and format. When only the format changes, **Generate** uses the open version and asks Claude to keep the complete answer in the illustration and direct labels. When the question or sources change, Claude establishes the answer from the current inputs. Use **Change it** to add a specific edit or **Try a different picture** for another composition. Up to eight versions are kept, each with its own question and format.
6. **PNG** saves an image at the exact selected dimensions. **HTML** saves a standalone page with the same canvas proportions. For Print, open the HTML in a browser and print or save it as a PDF on A4.

## How it makes an infographic

1. **One Claude call.** The prompt holds the sources, the question, the poster rules, the selected format and an example of its composition. Claude identifies the complete answer, chooses a main visual that carries every essential fact, then composes it for the target format. A single answer can include both sides of a comparison or every step of a sequence. Places can use a built-in world map with real coastlines.
   Every poster uses one house style taken from the owner's moodboard: flat mid-century poster illustration with one bold, saturated colour field (built as a Material Design colour theme from the 2014 Material palette, chosen for the subject and mood), hard-edged flat shapes, light and shadow as hard geometric shapes, 3 to 5 colours and a fine print grain. The subject guides the palette, the hero object and the typefaces. Large colour fields stay restrained, and the prompt asks Claude to check text against its local background. Before drawing, Claude plans the composition and afterwards checks the picture against a list of real failure modes, a method adapted from [claude-drawing-skill](https://github.com/cloveric/claude-drawing-skill) by cloveric (MIT).
2. **Shown as it is written.** The page re-draws about every 0.7 seconds while the answer streams in.
3. **Check the answer.** The prompt asks Claude to check that the whole answer is visible with supporting prose covered, and to review contrast and label placement. The app separately looks up numbers in the source text. That lookup only checks for matching values.

The [visual communication guide](docs/visual-communication-research.md) describes the design criteria. [Typography by subject](docs/visual-communication-research.md#typography-by-subject) defines 12 topic-aware headline/text pairs (anchor `TYPOGRAPHY_BY_SUBJECT_V1`), selected for the story and tone rather than a fixed grid. This policy is embedded in the Generate, Change it and Try a different picture prompts. All catalogue families load from Google Fonts. [Text readability and contextual palettes](docs/visual-communication-research.md#text-readability-and-contextual-palettes) defines the contrast, mobile label sizing and palette rules used by those prompts. A published Claude Artifact must be updated from this branch before it uses these rules.

**Safety:** Claude's HTML is treated as untrusted. Only known tags, `ig-*` classes, safe inline styles and `http(s)` links survive. Scripts, event handlers, images and `url()` styles are removed.

## Where it runs

Info to Graphics is a single `index.html` with no build step.

Making and changing infographics, reading images and reading links all need Claude, so they only work when the page runs as an artifact on claude.ai (links also need the Claude desktop app). Opened anywhere else, the page shows the example and its saved infographics, reads PDF, Word and text files, and exports.

## Libraries

[pdf.js](https://mozilla.github.io/pdf.js/) and [mammoth.js](https://github.com/mwilliamson/mammoth.js) load from cdnjs only when a PDF or Word file is first added. Fonts come from Google Fonts: Varela Round and Inter for the app, and the poster's selected families. The world map is Natural Earth 1:110m (public domain) from the `world-atlas` package, inlined.
