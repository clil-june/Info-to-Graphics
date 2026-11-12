# Handoff

Last updated: 2026-11-12 by Claude

## Current task

The owner judged the app's output "far inferior" to the hand-made period-products infographic (`references/harvard-period-products-visual/`). They asked to **remove the customization and make the app a generator**: drop sources, give an outline prompt, receive a high-quality infographic.

Done on this branch: `index.html` has been rewritten as that generator. The earlier board editor (figure types, inspector, brief and element marks, symbol editor, styles) is gone from the app; it's still in the git history (`feature/four-elements` before commit "One-shot generator").

Standing rules that still apply:
- `CLAUDE.md` and `AGENTS.md`: prefer visual representation over text, and follow `docs/visual-communication-research.md`.
- The Harvard reference is the quality bar.

## Branch / PR

- Branch: `feature/four-elements`. Pull request: https://github.com/clil-june/Info-to-Graphics/pull/2.
- PR #3 (`docs/visual-communication-guide`, https://github.com/clil-june/Info-to-Graphics/pull/3) is merged into this branch. Merging #2 brings it in too.
- The live Claude artifact "Info to Graphics" was republished from this branch on 2026-11-12, labelled "One-shot generator (PR #2)". It runs unmerged code.

## What changed

### The generator (latest, `index.html` rewritten)

- **App:**
  - Left rail: **1 · Drop your sources** (files, links, pasted text), **2 · Say what it should show** (an outline prompt), then **Make the infographic**.
  - After that: **3 · Ask for a change** (free text plus suggestion chips) and **New layout**.
  - The right side shows the finished page, the number check and the version list. Up to 8 versions are kept per infographic.
  - Header: name, switch between infographics, New, Export (standalone HTML).
  - Phones get two tabs.
  - Saved in the browser (`localStorage`, key `info-to-graphics.v2`).
- **Pipeline:**
  1. `planPrompt` → `sample.json`, `modelTier: 'complex'`. The plan holds the question, headline, deck, entities (symbols as 32×32 SVGs using `acc`, `paper` and `none`), 3–6 sections (question, title, form, layout, tone, exact data, focus, callout, evidence quote), takeaway, source and method.
  2. `composePrompt` → `sample`, `'complex'`. Claude writes the page HTML in the `ig-*` format, with `EXAMPLE_HTML` (the Harvard page) as its model.
  3. `checkNumbers`: every number in the rendered text must appear in the sources, allowing rounding. Integers up to 10 and 100 are skipped as phrasing.
  - **Change** uses `refinePrompt` (sources, current page, instruction). **New layout** re-composes from the plan.
- **Page format and design system (`#igcss`):** a single light printed look, built from the hand-made page:
  - header with a question pill, headline (`ig-h1`) and deck
  - auto-generated key
  - panels with a question kicker, a title stating the point and a denominator line
  - `ig-row` for two side by side; `ig-panel--dark`
  - bars, pictograms, big numbers, dot chart, timeline, steps, cards, table, quote, illustration
  - callouts, takeaway band, footer, and "The numbers behind the pictures" details
- **Renderer:** `renderIG` sanitizes, then `expandIG` draws the data-driven parts exactly from values:
  - bar tracks and fills (`--v` / `--max`)
  - pictogram cells, partly filled for fractions (`data-n`, `--v`)
  - dot charts: gridlines, ticks, gap line, value labels (`--lo`, `--hi`, `--v`)
  - symbol glyphs, the key and the takeaway's row of symbols
- **Sanitizer:** an allow-list of HTML and SVG tags and attributes, classes limited to `ig-*`, inline styles without `url(`, `expression`, `javascript:` or `@import`, and `http(s)` links only (opened in a new tab). Scripts, event handlers and images are dropped.
- **Example:** the Harvard study rebuilt in the format, with 7 product symbols. It's both the first-open example and the model given to Claude.
- **Removed:** Lucide icons (symbols are drawn), the board editor and all its inspector controls.
- `README.md` was rewritten for the generator.

### Earlier (still on this branch, superseded in the app)

Four-element briefs, symbols for recurring things with a key and editor, a board rendered as a page, and the dot chart in the editor. All of it lives in the history. The ideas carried over into the generator's rules and format.

## What was verified

| Check | How / where | Result |
|---|---|---|
| Inline script parses | `node --check` on the script in `index.html` | Passed |
| Example renders like the hand-made page | Headless Chrome, standalone `index.html`, 1440px, one look | Passed. Question, headline, key (7 symbols), symbol bars, side-by-side pictograms with dark night panel, dot chart by age with gap lines and labels, hero numbers, takeaway with symbol row, footer, data tables. |
| Number check on the example | Same page | "All 61 numbers on the page appear in your sources" (after fixing false alarms from table cells running together) |
| Sanitizer against a hostile page | Headless Chrome, stored version with `<script>`, `<img onerror>`, `onclick`, `javascript:` link, `url()` style, SVG `<script>` and `onload`, an unknown class | Nothing ran (`window.PWNED` unset); 0 scripts, images or `on*` attributes; the link's href removed; no `url()`; the unknown class dropped |
| Phone width | Headless Chrome, 390px | 390px |

### Unverified

- **Generation with Claude:** the plan call, the compose call, whether Claude's pages match the example's quality, whether its symbols are recognisable, how long it takes (two `complex` calls), Change, New layout, reading images.
- **The last two fixes** (night pictogram symbol size, dot-chart top padding) weren't looked at again.
- **The format's other forms:** timeline, steps, cards, quote, illustration and table panels were never rendered; the example doesn't use them.
- **Export:** the HTML file wasn't opened; the `downloads` capability and the browser fallback weren't tested.
- **Reading sources:** real PDF and Word files; reading links through `host:claude_browser`.
- **Layout:** dark mode (app chrome only; the infographic is light by design) and the mid-width layout weren't looked at.
- **Storage:** the browser storage limit with many long sources.

## Checkpoints

- **Harvard study v1** (text-labelled, hand-made): Claude Design canvas "Period Products Infographic", version "Checkpoint: Harvard study v1". Copy in `references/harvard-period-products/`.
- **Harvard study, visual:** the same canvas, versions "Product glyphs replace product names" and "Guide review: question, tables, attribution". Copy in `references/harvard-period-products-visual/`. This is the quality bar, and the app's `EXAMPLE_HTML` reproduces it in the generator's format.

## Still open

- First real runs in the artifact. Use the Harvard article (the owner's link) and one unrelated source, and compare them with the reference.
- If quality falls short, tune these first: `RULES`, `FORMAT`, the example, or a third "critique and fix" pass before showing the page.
- Netlify hosting stays undecided (generation needs claude.ai).

## Next step

Open the Info to Graphics artifact on claude.ai and press **Start my own**. Add the Harvard article (link or pasted text), write a one-line brief, and press **Make the infographic**. Record:

- the time taken
- the number check result
- whether the page reads like the reference

Then review and merge PR #2.
