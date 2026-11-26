# Info to Graphics

Drop in sources, say in a sentence or two what the infographic should show, and get back a finished infographic page. The app's job is to make one high-quality infographic per brief, at the standard of the hand-made reference in `references/harvard-period-products-visual/`.

## Using it

1. Click **create infographic** to open the workspace. Use **New Project** to name a project. Click the current project name in the left panel to switch projects or rename the current one.
2. **Add your sources.** Drop files or choose them with the paperclip. Paste one or more links or source text into the same field, then press **Enter** or **Generate** to submit any text still in the field. Supported files include PDF, Word (.docx), text, CSV, JSON, and images. Open **Source Library** to see the sources for the current project. Long names fit on one line, with the full name available on hover.
3. **Name the information you're after**, for example “Where do blue whales feed?”, and choose the canvas format next to **Generate**.
   - **Presentation (1920 × 1080 px, 16:9)** for projection. Show the shortest accurate answer in large type and one dominant visual. Use a side-by-side composition or a wide figure where the subject calls for it.
   - **Instagram (1080 × 1350 px, 4:5)** for reading top to bottom on a phone, with values placed directly on the artwork. This is the default.
   - **Print (3508 × 4961 px, A4)** for one portrait page, with room for a larger illustration and clearer labels.
4. **Generate.** A pencil draws in a loop while Claude works. A successful generation briefly shows **Done** and then opens the infographic. Use **Stop** to cancel.
5. **Keep working in the project.** Selecting a result in the right panel opens its preview and loads its question and canvas format. When only the format changes, **Generate** uses that version and asks Claude to keep the complete answer in the illustration and direct labels. Update the question or sources and click **Generate** to request a new result. The browser saves projects, sources, drafts, and version history locally.
6. **Export.** Click one or more results to select them. Pick **PDF**, **PNG**, or **JPEG** beside **Export**. PDF places each selected infographic on its own page. PNG and JPEG retain the original pixel dimensions. If you select multiple images, they are downloaded together in a ZIP.

## How it makes an infographic

1. **One Claude call.** The prompt holds the sources, the question, the poster rules, the selected format and an example of its composition. Claude identifies the complete answer, chooses a main visual that carries every essential fact, then composes it for the target format. A single answer can include both sides of a comparison or every step of a sequence. Places can use a built-in world map with real coastlines.
   Every poster uses one house style taken from the owner's moodboard: flat mid-century poster illustration with one bold, saturated colour field (built as a Material Design colour theme from the 2014 Material palette, chosen for the subject and mood), hard-edged flat shapes, light and shadow as hard geometric shapes, 3 to 5 colours and a fine print grain. The subject guides the palette, the hero object and the typefaces. Large colour fields stay restrained, and the prompt asks Claude to check text against its local background. Before drawing, Claude plans the composition and afterwards checks the picture against a list of real failure modes, a method adapted from [claude-drawing-skill](https://github.com/cloveric/claude-drawing-skill) by cloveric (MIT).
2. **Generation screen.** The pencil animation runs during generation. The app reveals the finished result after one completion confirmation.
3. **Check the answer.** All necessary facts belong in the graphic or its direct labels. The footer holds the citation. The prompt asks Claude to check completeness, contrast and label placement. The app separately looks up matching numbers in the source text.

The [visual communication guide](docs/visual-communication-research.md) describes the design criteria. [Typography by subject](docs/visual-communication-research.md#typography-by-subject) defines 12 topic-aware headline/text pairs (anchor `TYPOGRAPHY_BY_SUBJECT_V1`), selected for the story and tone rather than a fixed grid. This policy is embedded in the generation prompts. All catalogue families load from Google Fonts. [Text readability and contextual palettes](docs/visual-communication-research.md#text-readability-and-contextual-palettes) defines the contrast, mobile label sizing and palette rules used by those prompts. A published Claude Artifact must be updated from this branch before it uses these rules.

**Safety:** Claude's HTML is treated as untrusted. Only known tags, `ig-*` classes, safe inline styles and `http(s)` links survive. Scripts, event handlers, images and `url()` styles are removed.

## Where it runs

Info to Graphics is a single `index.html` with no build step.

Making and changing infographics, reading images and reading links all need Claude, so they only work when the page runs as an artifact on claude.ai (links also need the Claude desktop app). Opened anywhere else, the page can open the built-in example and its saved projects, reads PDF, Word and text files, and exports.

## Libraries

[pdf.js](https://mozilla.github.io/pdf.js/) and [mammoth.js](https://github.com/mwilliamson/mammoth.js) load from cdnjs only when a PDF or Word file is first added. Fonts come from Google Fonts: Varela Round and Inter for the app, and the poster's selected families. The world map is Natural Earth 1:110m (public domain) from the `world-atlas` package, inlined.
