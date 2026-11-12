# Handoff

Last updated: 2026-11-12 by Claude

## Current task

**Latest (2026-11-12, later):** the owner said the app's output still looked like "a generic schematic bunch of boxes". It must look and work by the rules of the hand-made period-products infographic (`references/harvard-period-products-visual/`). The board now renders as one designed page; see "Board as a designed page" below.

Put everything worked out by hand on the Harvard period-products infographic into the app itself (owner's request, 2026-11-12: "All we've been discussing now should be happening within the Info to Graphics app"). This resumes the app work that PR #3's handoff marked as paused.

The owner's standing default, now in `CLAUDE.md` and `AGENTS.md`: **prefer visual representation over text.** Recurring things become drawn symbols, a key introduces them once, and charts use the symbols instead of names. Follow `docs/visual-communication-research.md` when designing or reviewing generation.

Built on top of the earlier four-element work: McCandless's information, story, goal and visual form. The app follows the framework's meaning, not his graphic.

## Branch / PR

- Branch: `feature/four-elements`. Pull request: https://github.com/clil-june/Info-to-Graphics/pull/2 (app changes).
- PR #3 (`docs/visual-communication-guide`, https://github.com/clil-june/Info-to-Graphics/pull/3) is **merged into this branch** (commit `b2298ef`). It adds the research guide, the visual-first default and the Harvard visual reference. Merging #2 brings in #3 too; #3 can also be merged on its own first.
- The live Claude artifact "Info to Graphics" was republished from this branch on 2026-11-12, labelled "Symbols for recurring things (PR #2)". It runs code that isn't merged yet.

## What changed

### Board as a designed page (latest)

- **Page structure.** The board (`#sheet.poster`) is one page, in this order:
  1. a question pill
  2. a large headline that states the story (`brief.story`)
  3. a deck paragraph (`brief.deck`)
  4. the key
  5. figures as open panels
  6. a takeaway band (`brief.takeaway`, `brief.takeawayText`, plus a row of the board's symbols)
  7. a sources footer with method notes (`brief.footnote`)
  8. the tables

  The page uses Bricolage Grotesque headlines and Inter body text, as the hand-made version does.
- **Editing aids moved off the page.** The audience, the health count and the example notice sit in a tools row above the page (`#boardTools`), so they're left out of exports. Figure numbers, element marks, source tags and header icons only show on the selected figure.
- **Figures.**
  - Each figure's question is its heading (an uppercase kicker), with a 34px headline title.
  - `width: "half"` puts two figures side by side. `tone: "dark"` gives one dark panel. Both are set in the inspector under "On the page".
  - Default-coloured figures take the board's colour (the first entity's), or the colour of the entity their highlight is about.
- **Charts restyled** after the hand-made version:
  - **Bars:** symbol labels, 30px bars, bold values.
  - **Numbers:** large numbers, no boxes.
  - **Pictograms:** larger symbols, plus a `show` field ("19%") printed instead of "1.9 of 10".
  - Units like "%" no longer get a space.
- **New dot chart** (`type: "dots"`): two or three series across groups on one scale. Each series' own symbols are the markers, joined by a gap line, with rounded value labels, a per-group "leads" chip and a highlighted group with a callout. Claude is told to use it instead of "compare" when the cells would be numbers.
- **Prompts** ask for `deck`, `takeaway`, `takeawayText`, `footnote`, `width`, `tone`, `show` and the dot chart.
- **Example board (v3):** follows the hand-made layout, with half-width reusables and a dark night panel side by side, and the dot chart by age.
- **Export:** the HTML export is now just the page.
- **Fixed during the render check:**
  - Every figure's colour was being forced to blue.
  - Half-width pictogram rows split into two columns (the highlight note was forcing a second grid column).
  - Symbol rows wrapped.
  - A stray comma appeared in the source line.

### This session: visual-first in the app (all in `index.html`, plus `README.md`)

- **Entities (symbols for recurring things):**
  - Boards have `entities: [{id, name, color, svg, icon}]`.
  - Items and compare rows can carry `entity: <id>`. Their symbol then replaces the icon everywhere: tiles, nodes, bars, pictogram and icon-stack cells, compare rows.
  - The item is coloured with the entity's colour.
  - A label that only repeats the entity's name is hidden on "Less" and "Some" text, and shown on "More".
- **Key and symbol editor:**
  - A **Key** strip under the board brief lists every symbol with its editable name.
  - Clicking a symbol anywhere opens a **Symbol** editor: rename, recolour (8 colours), **Redraw with Claude** (optionally describing how it should look), or **Use an icon instead**. Changes apply everywhere it appears.
- **Symbol drawings** are small SVGs (viewBox 32×32) drawn by Claude. They're coloured only with the words `acc`, `paper` and `none`, and pass through the existing illustration sanitizer, which now also allows `fill-opacity`, `stroke-opacity`, `stroke-dasharray` and `fill-rule`.
- **Reader question:** the board brief has a question (shown above the story). Each figure has `brief.question`, shown as a kicker above its title and editable in the inspector.
- **Text equivalent:** "The numbers behind the pictures" sits at the end of the board, collapsed in the app and open in exports. It builds one table per figure from the figure's data, and doesn't need Claude.
- **Exports:** symbol spans keep `role="img"` and the entity name as `aria-label`.
- **Prompts:** a VISUAL FIRST block:
  - list the recurring things as entities with drawn symbols and colour families
  - link items to them
  - prefer pictograms and icon stacks
  - choose the form by relationship (from the guide)
  - keep "reported / said / estimated", denominators and units
  - never add a causal link

  Board generation returns `brief.question` and `entities`. New entities are merged by id, and existing ones are kept. Figure edits and new boards get the existing entity list so the ids are reused.
- **Defaults:** new boards start on **Less text**.
- **Example board:** replaced Bauhaus with the Harvard period-products study (summarised notes with the numbers from the study). It has seven entity symbols (regular tampon, super-absorbent tampon, pad, panty liner, cup, period underwear, pads-or-tampons) and five figures, all with questions. Stored example boards without entities are swapped for it.
- **Fixes found in the render:**
  - Bars got squeezed when their label was hidden.
  - Symbols on non-highlighted items were faded.
  - Symbols were enlarged by 35% inside tiles and rows.

### Earlier on this branch (four-element briefs, before PR #3)

- **Board brief and figure brief:** story, goal and visual idea; four-element marks with boring, useless and eye-candy labels; **Fill what's missing with Claude**.
- **Focus item and callout** on every figure type.
- **Styles:** road timeline, icon-stack bars, one big number.
- **Fixes:** "null" text in the inspector, and sideways scrolling on phones.
- **Harvard checkpoint:** the text-labelled v1 is in `references/harvard-period-products/`.

### From PR #3 (merged in)

- `docs/visual-communication-research.md`, linked from `README.md`, `CLAUDE.md` and `AGENTS.md`.
- The visual-first default in `CLAUDE.md` and `AGENTS.md`.
- `references/harvard-period-products-visual/`: the hand-made reference with product drawings, a reader question, tables and attribution.

## What was verified

| Check | How / where | Result |
|---|---|---|
| Board renders as one page (latest) | Headless Chrome, standalone `index.html`, 1440px, one look, nothing selected | Question, headline, deck, key, panels, half-width pair with dark panel, dot chart, hero number, takeaway band and footer all render with no errors. Web fonts were blocked offline, so fallback fonts showed. |
| Fixes after that look | Same page, measured, not looked at again | Half-width pictogram rows are one column and don't wrap (27px). Question colours follow the board and entities (crimson, teal). Source line has no stray comma. |
| Phone width (latest) | Headless Chrome, 390px | 390px |
| Inline script parses | `node --check` on the script in `index.html` | Passed |
| New example board renders, no page errors | Headless Chrome, standalone `index.html`, 1440px wide, light mode, one look | Passed. Key with 7 drawn symbols, symbols in bars, pictograms and compare rows. 12 repeated names hidden. Question kickers shown. 5 tables. |
| Symbol editor opens from the key | Same render, clicked the cup in the key | Passed. Inspector shows "Symbol" with preview, name, colours, redraw and icon options. |
| Bars after the label fix | Same page, measured | Bar track 688px wide (it was squeezed before the fix) |
| Phone width | Headless Chrome, 390px | 390px, no sideways scroll |
| Icon names used | Checked against Lucide 0.460.0 | Passed |

### Unverified

- **Latest page layout:**
  - not looked at after the last fixes
  - dark mode, the phone layout, the mid-width layout and the real web fonts not looked at
  - whether Claude fills `deck`, `takeaway`, `footnote`, `width`, `tone`, `show` and dot charts
  - the exported HTML's look
- **All Claude features** (need a test in the Claude artifact):
  - whether Claude returns `entities` with usable SVG symbols, links items to them, writes questions, and keeps "reported" wording
  - **Redraw with Claude**
  - **Fill what's missing**
  - building a board, Ask Claude, reading images
- **Visual checks:**
  - the render wasn't looked at again after the last three fixes; only the bar width was measured
  - dark mode and the phone layout weren't looked at for the new key and tables
  - the mid-width layout (761–1100px)
- **Editing edge cases:**
  - "Use an icon instead" for a symbol, and the icon picker clearing the drawing
  - converting a figure to another form keeping its entity links
  - undo across symbol edits
- **Export:** files (HTML, SVG, `.board.json`) weren't opened; the downloads capability and the fallback weren't tested.
- **Loading data:**
  - real PDF, Word and HTML files
  - reading links through `host:claude_browser`
  - old saved boards: the swap from the Bauhaus example to the Harvard example

## Checkpoints

- **Harvard study v1:** the hand-made, text-labelled benchmark. It's on a Claude Design canvas titled "Period Products Infographic" (private to the owner), in the version labelled "Checkpoint: Harvard study v1". A copy is in `references/harvard-period-products/`.
- **Harvard study, visual:** the same canvas, with product drawings and the guide fixes. These are the versions labelled "Product glyphs replace product names" and "Guide review: question, tables, attribution". A copy is in `references/harvard-period-products-visual/`. It's the target for what the app's generator should now produce.

## Still open

- Test generation in the artifact with the Harvard article (the owner's link) and compare it with `references/harvard-period-products-visual/`.
- Ideas the hand-made reference has that the app doesn't yet:
  - a pads-versus-tampons dot chart by age (the app uses a compare table)
  - a takeaway band
  - a source footer on the board
- Test reading a link in the Claude desktop app.
- Decide whether to host the standalone page on Netlify (Claude features stay off there).

## Next step

Open the Info to Graphics artifact on claude.ai and press **Start my own**. Add the Harvard article (link or pasted text) and press **Build board from sources**. Check:

- Does a key with drawn symbols appear?
- Do the charts use the symbols instead of names?
- Does each figure have a question?
- Is "say/reported" kept?
- Is the table section correct?

Record the result here, then review and merge PR #3 and PR #2.
