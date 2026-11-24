# Handoff

Last updated 2026-11-24 (Codex: simplified source list and removed the refinement panel; published by Claude Code as Artifact version 50).

## Simplified left panel (Codex, 2026-11-24)

- **Branch / PR:** `feature/four-elements`, [PR #2](https://github.com/clil-june/Info-to-Graphics/pull/2). Based on `ac47ce2`.
- **Change:** Source Library shows a simple list. Long names truncate at the last whole word that fits, with CSS ellipsis for a filename or URL that starts with an unbroken word wider than the row. Full names remain in tooltips and accessible text. Source removal, links, and notices that require action are available.
- **Removed:** The “Say what to change” field, quick suggestions, “Try a different picture,” and their event handlers. The main question and Generate controls still support new requests and canvas changes.
- **Verified:** In standalone Chromium, checked title truncation at desktop and 390 px widths, a short title and a long filename, and the full title in each tooltip. With a local sampler fixture, verified first generation and the format-only recomposition path from 16:9 to 4:5. The removed panel stays absent after generating.
- **Published (Claude Code, 2026-11-24):** on the owner's go-ahead, `index.html` from `99682dd` (Git blob `063e887`, 396,979 bytes, SHA-256 starting `61a92c7f250b40d8`) went to the existing Artifact as **version 50, publication ID `1795547882-a594`**. Capabilities were carried forward unchanged: `sample` with images, `downloads`, and `mcp` `host:claude_browser` with `preview_start` and `get_page_text`. **Verified:** a read-back of the live page file contains the file byte for byte, plus only the host's standard 531-character wrapper before it and `</body></html>` after it. The owner approved publishing after being told the version removes "Change it" and "Try a different picture". **Unverified:** the simplified panel and real generation inside claude.ai.
- **Earlier next step (done):** The previously recorded Claude Artifact was version 49 (`1795547407-0dba`). Publish the updated branch when requested and check it in the live Artifact.

## Light workspace palette (Codex, 2026-11-24)

- **Branch / PR:** `feature/four-elements`, [PR #2](https://github.com/clil-june/Info-to-Graphics/pull/2). Based on `5d6320c`.
- **Change:** The workspace has a light gray canvas (`#F2F3F3`), white panels, and pale gray fields. Primary actions use the welcome button's dark teal (`#00383D`) with white text. Secondary controls use dark teal text on white. Menus, tile selection, keyboard focus, and status colours use the light palette.
- **Verified:** In standalone Chromium, the welcome and workspace primary buttons match, the canvas and panels render in the specified colours, the format menu opens and closes from the keyboard, and selecting a gallery tile highlights it and enables Export. The change is limited to application CSS.
- **Published (Claude Code, 2026-11-24):** on the owner's go-ahead, `index.html` from `f9e633a` (Git blob `f989536`, 400,832 bytes, SHA-256 starting `563cfca3a7220382`) went to the existing Artifact as **version 49, publication ID `1795547407-0dba`**. Capabilities were carried forward unchanged: `sample` with images, `downloads`, and `mcp` `host:claude_browser` with `preview_start` and `get_page_text`. **Verified:** a read-back of the live page file contains the file byte for byte, plus only the host's standard 531-character wrapper before it and `</body></html>` after it. **Unverified:** the light workspace's appearance inside claude.ai, and the checks listed under Still open.
- **Earlier next step (done):** The previously published Claude Artifact was version 48 (`1795545659-523b`). Publish the updated branch's `index.html` to that Artifact when the owner requests it, retaining the existing capabilities.

## Project workspace and export (Codex, 2026-11-24)

- **Branch / PR:** `feature/four-elements`, [PR #2](https://github.com/clil-june/Info-to-Graphics/pull/2). GitHub rollback point `28af8ec`. The last recorded published Claude Artifact is version 47 (`1795533138-0f92`), built from `66d9612`.
- **Welcome:** Use the supplied warm paper and engineering-sketch artwork with a live headline and **create infographic** button. The background is embedded in `index.html`. The owner will supply the logo later.
- **Workspace:** Charcoal panels, pale cyan actions, projects and Source Library on the left, preview in the middle, and the current project's result gallery on the right. Mobile uses Edit, Infographic, and Results tabs. Each project retains its sources, question, canvas format, and generated history. Existing browser data is read from localStorage and carried into IndexedDB. Storage is local to the browser. The old fixed project and result limits are removed.
- **Export:** One selection downloads as PDF, PNG, or JPEG. Several selections create a multi-page PDF or a ZIP of full-size images in gallery order. A4 PDF pages use the physical A4 size. The three canvas sizes and generation prompts are unchanged.
- **Verified in the standalone browser:** welcome and workspace, creation and switching of named projects, saved results after reload, paste of multiple source links, generation and the final Done state with a sampler stub, responsive preview and gallery at 390 px, single JPEG plus batch PNG, JPEG, and PDF. Downloaded files were decoded and checked as 1920 × 1080 and 3508 × 4961 images and a two-page PDF with landscape and A4 pages.
- **Published (Claude Code, 2026-11-24):** on the owner's go-ahead, `index.html` from `450ff76` (Git blob `a2802a1`, 400,637 bytes, SHA-256 starting `0af04c41bae9c1b7`) went to the existing Artifact as **version 48, publication ID `1795545659-523b`**. Capabilities were carried forward unchanged: `sample` with images, `downloads`, and `mcp` `host:claude_browser` with `preview_start` and `get_page_text`. **Verified:** a read-back of the live Artifact contains the file byte for byte, plus only the host's standard 531-character wrapper before it and `</body></html>` after it. **Unverified:** real generation, link reading, project history (IndexedDB inside the claude.ai sandbox, with the localStorage fallback) and single or batch downloads in the live Artifact.
- **Still open:** Check real generation, link reading, local project history, and downloading in Claude.

## No stray lines, no text on objects, nothing redundant, at most three options (Claude Code, 2026-11-24, sixth change)

**Owner report** (fish and chips, 16:9, version 46): a cream line ran from the "Haddock" label straight across the cod. The bottom-right sentence "Sources name no single best" was unnecessary.
**Owner rules going forward:**
1. No weird elements floating around.
2. All the information is in the infographic, with nothing the picture already shows; five fish drawn already say there is no single best.
3. If there is no definitive top one, give at most three options.

**Cause of the line:** my version-45 fallback. When a label had no clean spot nearby, `clearArtwork` took the nearest clean spot anywhere and drew a pointer back. "Haddock" was moved above the cod and its pointer crossed the cod.

**What changed:**
- **Pointers:** new `pointerClear()` and `maskColour()`. A pointer is drawn, and a far spot accepted, only if walking from the label it crosses empty field and then enters one object and stays in it. It must never cross another object first and must be at most 30% of the drawing's smaller side (minimum 60 px). Otherwise that spot is rejected. In the grow-at-the-bottom fallback a pointer is drawn only if its path is clean.
- **Text on objects counts as an overlap.** Before, a label wholly on one solid colour was accepted, so text sitting inside a fish passed. Now a label may sit on a shape only if it is its backing:
  - marked `data-backing` (added to `SVG_ATTR`);
  - or a plain panel, at least 90% of its box filled (a rectangle or rounded rectangle), that holds the whole label. The radio's dial qualifies; a fish, plate or leaf does not.
  Candidate spots must also not be on an object.
- **Prompt:**
  - Rule 0 says text never sits on a drawn object; the only exception is a rectangular panel marked `data-backing`.
  - New 4d, no stray elements: every line belongs to an object or is a pointer to its own object by the shortest clear route, never crossing another object, label or pointer.
  - New 4e, nothing the picture already says.
  - New 4f: without a single definitive answer, at most three options in total, including "also used" or runners-up.

**What was verified** (built-in Chromium pane, standalone `index.html`, stand-in `window.claude` at `?stub=1`, 16:9 unless noted):
- `node --check` on the inline script.
- **Rebuilt fish slide 2** ("Haddock" written on the haddock under the cod): it moved 96 units down to just under the haddock. No pointer, no text on any object.
- **Fish slide 1, Birkin, philodendron, Monstera:** nothing cut off and no text on objects. The philodendron's names sit on the shelf panel, which is allowed.
- **Plate:** the label moved off the plate; its pointer crosses one object, the plate.
- **Owner's good radio:** nothing moved; its dial labels sit on the dial panel.
- **4:5 regression** (Queen 4, fly agaric, lines without dy, messy poster): 0 overlaps, 0 cut off. The messy poster got one pointer, which runs from field into a single object and is 31 units long.
- No console errors.

**Published** as Artifact version 47 (`1795533138-0f92`) from `66d9612`, capabilities carried forward (`sample` with images, `downloads`, `mcp` `host:claude_browser`).

**Unverified:** real Claude output in the live Artifact, including whether Claude follows 4d–4f and marks `data-backing`.

## Nothing cut off at the edge (Claude Code, 2026-11-24, fifth change)

**Owner report** (fish and chips, 16:9, version 45): the italic sentence at the bottom right ("Sources name no single b…") was cut off by the drawing's right edge. **Owner decision:** this must never happen again.

**Cause:** the label sat in empty space but ran past the SVG's right edge, which clips it. `fitLabels` fixes edge overflow only for plain labels and skips `[data-callout]` text, while `clearArtwork` only checked overlaps with artwork and other labels. A callout label running off the edge was handled by neither.

**What changed:**
- **`clearArtwork`, for every label block (callout or plain):**
  - A block wider than the drawing (less 8 px) is first broken onto two lines: its wide texts are split at the middle word into tspans with `dy="1.2em"`. If it is still too wide, all its text shrinks by 10% per step, up to 8 times.
  - A block past the left or right edge then counts as failing, like an overlap, and moves to the nearest spot inside the edges that is also clear of artwork and labels. Vertical overflow is still handled by growing the viewBox.
- **Pointer lines** are added only when a label is moved off a drawn object, not when it is moved in from an edge.
- **Rule 0 in `POSTER_RULES`** is now "nothing overlaps and nothing is cut off". New bullet: every word sits inside the viewBox at least 16 units from each edge; estimate widths (0.55 × font-size per character, 0.62 for bold, italic or wide fonts); break a long line into two tspans or shorten it.

**What was verified** (built-in Chromium pane, standalone `index.html`, stand-in `window.claude` at `?stub=1`, 16:9):
- `node --check` on the inline script.
- **Rebuilt fish slide:** the italic callout sentence that ran about 150 units past the right edge moved 110 units left and is fully visible. A plain label wider than the whole drawing was broken onto two lines and fits. No label cut off, on artwork or overlapping (checked independently at 1 px steps).
- **Regression in 16:9:**
  - Birkin, philodendron, plate and Monstera: 0 cut off, 0 on artwork, 0 overlaps. In the Birkin case "Super Atom", whose right edge was 2 px past the drawing, also moved inside.
  - Owner's good radio: nothing moved. The only checker hit is the side panel hidden under the dial.
  - No console errors.

**Published** as Artifact version 46 (`1795531761-bf1d`) from `934b448`, capabilities carried forward (`sample` with images, `downloads`, `mcp` `host:claude_browser`).

**Unverified:** real Claude output in the live Artifact. HTML text outside the SVG (headline, answer block) is not part of this check; `fitPresentation` and `fitArtboard` size it.

## No overlaps, ever: exact pixel check and rule 0 (Claude Code, 2026-11-24, fourth change)

**Owner report** (philodendron after a 4:5 → 16:9 switch, made with version 44): "Birkin / no climbing" sat across thin Birkin leaves, and "3 ft" touched a leaf. **Owner decision:** main elements, illustrations and text, never overlap, in any format or transition. It is a fundamental rule.

**Cause:** `clearArtwork()` judged a label by 21 sample points (a 7 × 3 grid). Thin leaves fell between the points, and stroked shapes (stems, measuring bars, outlines) were not tested at all.

**What changed:**
- **`clearArtwork()` is now async and exact.** New `artMask()` renders each drawing off-screen, at its shown size and with its resolved paint, but without its text, label groups and pointer lines. New `maskMixed()` then requires every pixel under a label block (1 px margin) to be one colour: the open field, or one flat backing shape. Anything that differs by more than 30 (summed RGB) counts as an overlap, whether it is a thin leaf, a stem, a stroke or a bar. Paint order is real, so a shape hidden under another doesn't count.
- **Labels against labels:** boxes are trimmed by 12% top and bottom for empty line spacing, and only a real overlap counts.
- **Where a failing or overlapping label goes:**
  - the nearest clean spot within about two label heights; it may step just past the drawing's top or bottom, and the drawing grows to hold it;
  - otherwise the nearest clean spot anywhere in the drawing, joined by a new straight pointer line (`line[data-pointer]`, ink colour) back to where it was;
  - if the drawing has no clean spot at all, the drawing grows at the bottom and the label goes there with a pointer.
  The old "backing patch" fallback is gone, because it covered the drawing.
- **Pointer lines** (straight lines, polylines and open stroked paths that end at a label) are marked `data-pointer` and left out of the mask.
- **`fitSoon`** runs `clearArtwork` after `fitLabels`, then `leaderContrast` and the re-fit. A newer run cancels an older one.
- **Rule 0 in `POSTER_RULES`,** the first rule for new posters, changes and format switches: nothing overlaps. Plan label areas before drawing, keep 8 units of empty space around labels, never put text across leaves, objects or shadows, re-place labels from scratch on a format change, and check each label's rectangle last. The format-switch rules also point to rule 0.

**What was verified** (built-in Chromium pane, standalone `index.html`, stand-in `window.claude` at `?stub=1`):
- `node --check` on the inline script.
- An independent checker, separate from the app's method, sampled every 2 px under each label block against every drawn element with `isPointInFill` and `isPointInStroke`.
- **16:9:**
  - Rebuilt Birkin case: before the fix the checker would have flagged it. "Birkin / no climbing" moved 39 units up, clear of the leaves; "3 ft" moved 15.6 up beside the bar. 0 labels on artwork, no pointer needed.
  - Rebuilt philodendron: small moves of 11–16 units. 0 on artwork.
  - Rebuilt plate and Monstera: labels moved to the nearest clean spot, with a pointer. 0 on artwork.
  - Owner's good radio: nothing moved. The checker's only hit is the side panel hidden completely under the dial, not a visible overlap.
- **4:5:** earlier hard cases (Queen 4, fly agaric, lines without dy, messy poster) had 0 overlaps and 0 labels outside.
- No console errors. Export clones the already-fitted page, so it carries the moved labels.

**Published** as Artifact version 45 (`1795511450-103d`) from `b1b610d`, capabilities carried forward (`sample` with images, `downloads`, `mcp` `host:claude_browser`).

**Unverified:**
- Real Claude output in the live Artifact, including a real 4:5 ↔ 16:9 switch.
- Very busy drawings, where the nearest clean spot may be far away and need a pointer.
- Whether the claude.ai sandbox allows drawing an SVG data-URL image to a canvas and reading its pixels. If it doesn't, `artMask` fails and the new `geomMask()` fallback takes over: it finds the topmost shape's paint at each point with `isPointInStroke` and `isPointInFill`, every 2 px with a 2 px wider margin. Which path runs in the live Artifact is unknown.
- **Fallback verified here:** `HTMLImageElement.prototype.decode` was forced to reject (8 renders blocked) and the same five 16:9 cases were run. An independent checker at 1 px steps found no label on artwork (the radio's hidden side panel aside), and the pixel path re-checked at 1 px was also clean.

## Faster changes (Claude Code, 2026-11-24, third change)

**Owner decision:** "Yes, faster changes". Changes and format switches use the quicker model; brand-new posters keep the strongest.

**What changed:**
- The `ask()` tier now depends on the request. Before, every request used `complex`.
- **Quicker `default` tier:**
  - "Change it" with the same question and sources (`kind === 'change' && sameAnswer`), including a format switch made there;
  - a format-only switch through Generate (`adaptFormat`).
- **`complex` tier, unchanged:** a new poster, a new question or new sources, and "Try a different picture" (a fresh illustration idea).
- `ask()` already falls back: if the quicker model's page fails `validPage`, the strongest model makes it.

**What was verified** (built-in Chromium pane, standalone `index.html`, stand-in `window.claude` at `?stub=1`, which records the requested `modelTier`): `node --check` passes. The four requests asked for these tiers: new poster `complex`; "Use fewer words" change `default`; switch from 4:5 to 16:9 via Generate `default`; "Try a different picture" `complex`. No console errors.

**Published** as Artifact version 44 (`1795510013-1657`) from `bbee240`, capabilities carried forward (`sample` with images, `downloads`, `mcp` `host:claude_browser`).

**Unverified:** how much faster real changes are in the live Artifact, and whether the quicker model's redraws keep the quality bar. If they don't, move `quick` back to `complex`, or keep the quicker model only for wording changes.

## Labels beside their objects, one-colour pointers, short text (Claude Code, 2026-11-24, second change)

**Owner report** (philodendron, Instagram, made with version 42): text was "all over the place": plant names collected under the shelf, far from their plants, and a note pushed into the shelf. The pointer had a white line with a dark outline. There was far too much text. **Owner decision:** these are rules for every infographic the model makes. A pointer line is one clear colour, never an outline. Text is short and concise.

**Cause:** Codex's `fitCallouts()` (restored from the backup) pushed each callout label straight down until it cleared the bounding box of all the artwork in its column, so labels ended up below the whole scene. It also drew every callout leader as a cream line on a dark halo. The prompt had no word budget for Instagram or A4 and allowed descriptions per item.

**What changed:**
- `fitCallouts()` and its halo drawing are removed. `clearArtwork()` now places every label block, plain `<text>` and callout `<g data-label>` alike. A block that straddles a shape's edge or truly overlaps another label is nudged at most about two label heights (minimum 24 px) to the nearest clean spot. If no spot is that close, it stays beside its feature and gets a solid backing (`rect[data-backing]`) in the colour it mostly sits on, or the field colour if that reads better. Straight `<line>` pointers, including `line[data-leader]`, follow a moved label.
- `leaderContrast()` covers callout leaders too. It uses one solid colour: the page ink when it has 3:1 everywhere along the line, otherwise the most visible of field, white or near-black. No casings or outlines.
- `POSTER_RULES` (used for new posters, changes and format switches alike) gains 4a–4c:
  - Labels are a name or value plus at most 4 words, never sentences, at most 2 lines and one qualifier.
  - Word budget outside the headline and source: Presentation 18, Instagram 24, A4 36. Drop the least important fact rather than shrink type.
  - A fact shared by all items is said once.
  - Scientific names, care tips and descriptions are left out unless the question asks for them.
  - Every label sits next to what it names: within about one label height, or joined by a short straight pointer. Never a row of names far from their objects.
  - Pointers are straight, 1.5–2.5 units, one solid colour with 3:1 contrast, no outline, dashes or arrowheads.
- The callout instructions no longer promise a two-tone stroke; the "casing is a legibility aid" sentence is replaced with "Pointer lines are one solid colour, with no outline or casing."

**What was verified** (built-in Chromium pane, the standalone `index.html` on the local static server with the stand-in `window.claude` at `?stub=1`, Instagram format):
- `node --check` on the inline script.
- The rebuilt philodendron problem: the shelf rect, two plants as `g[data-artwork]`, and callout labels straddling the shelf edge. Birkin and Super Atom moved 12.9 units down onto the shelf, directly under their own plants. The note moved 11.3 units below the shelf. The pale Heartleaf leader became the ink colour (`#1b5e20`). No halos or casings, no overlaps.
- Rebuilt plate: label nudged 29 units off the leaf; the pointer is one colour. Rebuilt Monstera: no clean spot within reach, so the label kept its place on a backing. Owner's good radio: nothing moved or re-coloured.
- Earlier hard cases (Queen 4, fly agaric, lines without dy, messy poster): 0 overlaps, 0 labels outside.
- The prompt sent contains 4a and 4b and no "two-tone" wording. The generation prompt without sources is about 33,600 characters. No console errors.
- **Caught and fixed during the work:** the first scripted edit matched a line that exists in both `fitLabels` and `clearArtwork` and cut part of `fitLabels` out; it still passed `node --check`. The file was restored from `6f91a39` and the edit redone, anchored to `clearArtwork`, before any of the checks above.

**Published** as Artifact version 43 (`1795509849-833d`) from `d36e42d`, capabilities carried forward (`sample` with images, `downloads`, `mcp` `host:claude_browser`).

**Unverified:** real Claude output in the live Artifact: whether it keeps to the word budget and places labels beside their objects, and how a backing patch looks on a real drawing.

**Generation time (owner asked to shorten it).** Nothing changed yet. The app asks the `complex` tier for new posters and changes. Speed levers: fewer words to write (the new budget helps a little), a quicker model tier for changes and format switches (possible quality cost), or a lower effort setting (the runtime allows it only when the owner names it). A failed page check runs a second full attempt, which doubles the wait. See Next step.

## Quality rules restored (Claude Code, 2026-11-24)

**Owner report:** new outputs had text on illustrations and on other text, pointer lines the same colour as what they cross, lists of facts under the picture, and odd drawing (Monstera leaves with pale wedges sticking out). Switching between landscape and portrait often broke the layout. The owner's good references: the 1960s radio, the banana timeline and the landscape healthy plate.

**Cause:** the 2026-11-23 rollback to `32843b6` dropped ten commits of quality work: the visual-answer check and the filter that removes text blocks below the figure, the illustrated examples, callout clearance and two-tone leaders, and the pencil screen. They were still on `backup/before-callout-rework-2026-11-23`.

**What changed:**
- `index.html`, `docs/visual-communication-research.md`, `README.md`, `AGENTS.md` and `CLAUDE.md` are back to the backup branch's state, with Codex's three-part Instagram layout (`53c86c5`) and the near-miss fallback (`e04ff08`) merged on top. Conflicts were resolved in favour of the backup's rules; the `ig-partition` template, `partitionOk()` and the docs paragraph were kept.
- **New `clearArtwork()`** (runs in `fitSoon` after `fitLabels`): a label whose visible backing changes under it (it straddles a shape's edge, judged by the topmost shape at 21 points with `isPointInFill`) moves by the shortest step to a place with one backing and no other label nearby. A straight `<line>` ending at the label follows it, and the drawing grows if the label moves past its top or bottom. A label wholly on one flat shape (the radio's dial) stays put.
- **New `leaderContrast()`** (runs after `fitCallouts`): a thin line (stroke 4 units or less) that ends at a label and has under 3:1 contrast with what lies under it along more than 20% of its length is re-coloured to the page ink, the field, white or near-black, whichever is most visible. If none reaches 3:1 everywhere, it also gets a contrasting casing underneath. Decorative strokes that don't end at a label keep their colour.
- **Prompt failure modes added:** cut-outs painted as wedges or spikes (cuts must stay inside the outline and show what is behind); pointer lines in the colour of what they cross; labels across a shape's edge.
- **Format proportions:** Instagram's drawing is about 400 × 300–340 (up to 420 with a one-line headline); A4 is about 400 × 420–460 (it was capped at a square, which left the empty band seen in the baby poster); the slide is about 400 × 360 beside an answer, or 800 × 320 when wide.
- **Format switches:** `refinePrompt` gets `fromFormat`. On a format change the opening says to keep facts, subject, palette and fonts and recompose the layout, and new `formatSwitchRules()` names both canvases and the old viewBox. It says not to reuse old coordinates, gives the landscape↔portrait restacking, and requires uniform scaling and labels re-placed and re-checked.

**What was verified** (built-in Chromium pane, the standalone `index.html` on the local static server with the stand-in `window.claude` at `?stub=1`, Instagram format):
- The inline script passes `node --check` (Node 14, with newer operators rewritten for the check only).
- The rebuilt plate problem: the label across the leaf edge moved 29 units up onto the plain plate; the pale pointer over the pale plate became near-black with a white casing; the "Beside the plate" note under the figure was removed. 0 label overlaps.
- The rebuilt Monstera problem: the label across two leaves moved below them. 0 overlaps.
- The owner's good radio (its SVG taken from `60's Music radio.html`): no label moved, no line re-coloured, viewBox unchanged.
- The earlier hard cases (rebuilt Queen 4, fly agaric, lines without dy, the messy poster): 0 overlaps, 0 labels outside the drawing.
- Switching an Instagram version to 16:9: the prompt sent had the new opening, the switch rules with the old viewBox `0 0 400 340`, and the landscape proportions.
- No console errors.

**Published** as Artifact version 42 (`1795508655-1549`) from `6f91a39`, capabilities carried forward (`sample` with images, `downloads`, `mcp` `host:claude_browser`).

**Unverified:** real Claude output in the live Artifact, especially: a landscape↔portrait switch; the A4 baby poster filling the page; Monstera leaves drawn with proper cut-outs; whether the moved label positions read well on real drawings (a label is moved, not rewritten, so it can end up farther from its feature). Pointer lines drawn as `<path>` don't follow a moved label (only `<line>` does).

## Three-part Instagram layout

- After the rollback, a generated plate still had white text overlapping pale artwork, detached quarter labels and extra copy below the figure. Generation and revision prompts now reserve distinct areas for independent objects, labels and leaders. The Instagram prompt keeps only the citation below the figure.
- For a whole with one upper and two lower parts, use `ig-partition`. The renderer keeps the artwork and all three labels in separate rows and columns, uses contrasting ink on a solid field, and renders only the figure, headline and citation. The generator still chooses the artwork and must place the correct sectors for each slot. Other layouts use their existing renderer.
- Verified in Chromium with a plate fixture at phone width: artwork and labels were disjoint, labels wrapped inside their positions, supplemental copy was removed, and the export clone preserved the result. Verified light and dark field contrast, rejection of malformed slots and normal layout dimensions.
- **Claude Code fix (2026-11-23):** `validPage()` no longer rejects a whole answer when an `ig-partition` figure misses the exact template (that ended in "The page came back empty"). The strict check moved to `partitionOk()`; `renderIG` uses the special layout only for an exact match and otherwise removes the `ig-partition` class, so the answer shows in the normal layout. A usable page still needs `header.ig-head` and a panel or hero figure.
  - **Verified** in the in-app Chromium preview of the local standalone `index.html` with the stand-in Claude (`?stub=1`), Instagram format, three answers in a row: a valid plate got the three-part layout with labels clear of the artwork; a near-miss (same plate with a `<text>` inside the drawing) was accepted as version 2 in the normal layout with its three labels shown; a normal poster rendered as version 3. No console errors.
  - **Published** as Artifact version 41 (`1795460889-0e3b`) from `e04ff08`, capabilities carried forward (`sample` with images, `downloads`, `mcp` `host:claude_browser`).
  - **Unverified:** real Claude output in the live Artifact.
- GitHub rollback point: `c9d034d`. The last recorded Claude publication is version 40 (`1795459555-c7fa`). Publish this change to the existing Artifact before testing the same plate brief with the original sources in Instagram format.

## Rollback status

- GitHub's working branch restores the code and design guides from `32843b6d4f039f6629edf5a20df1093a571e81d1`. The full pre-rollback state `9bae9c95e311f9ece9aec54760ef8411b1d7694f` is preserved on [`backup/before-callout-rework-2026-11-23`](https://github.com/clil-june/Info-to-Graphics/tree/backup/before-callout-rework-2026-11-23).
- Claude's separate restore point is Artifact version 36 (`1795442960-ce11`). To restore it, republish the exact `index.html` from `0c1def5e0faf1dbee1656a548ab8c5cd14977107` to the existing Artifact and verify the published version. The last publication recorded before this rollback is version 39 (`1795458342-d2f8`).
- **Done 2026-11-23 by Claude Code:**
  - **Published:** the exact `index.html` blob from `0c1def5e0faf1dbee1656a548ab8c5cd14977107` (Git blob `2166fffb918f8f416b525d814986a96f0585d26c`, 295,216 bytes, SHA-256 starting `79f3a982f6acc8cd`) went to the existing Artifact as **version 40, publication ID `1795459555-c7fa`**, labelled "Rollback to v36 code (0c1def5)".
  - **Capabilities:** carried forward unchanged (`sample` with images, `downloads`, `mcp` `host:claude_browser` with `preview_start` and `get_page_text`).
  - **Verified:** a read-back of the live Artifact contains that file byte for byte (the same SHA-256), plus only the host's standard 531-character wrapper before and `</body></html>` after.
  - **Note:** the live Artifact now runs the version 36 code, while GitHub's working branch holds the restored code from `32843b6`. These are different snapshots: `0c1def5` predates `32843b6`'s format adaptation.
- The entries below record earlier work and publications.

## Current task

**Owner decision (2026-11-23):** use the selected pencil sketch. The natural yellow pencil draws the chart on the app's blue field in a loop while generation runs. Show a centered **Done** confirmation once, after a complete result is ready, then reveal it.

**Owner report (2026-11-23):** the healthy-plate portrait has an oil bottle on top of the vegetable qualification. In both formats cream leaders lose contrast over the plate and the portrait vegetable label appears detached from its mark. Keep the primary quantities and their labels together, with their own reserved space ahead of any secondary labels.

**Owner decision (2026-11-23):** all necessary information belongs in the infographic itself, either drawn or directly labelled. Omit supplemental prose in Presentation, Instagram and A4. The healthy-plate A4 and Instagram examples added unrelated drinking and daily intake advice after the figure. Keep only the citation below the visual.

**Owner decision (2026-11-23):** one question leads to one takeaway and can require several essential facts. Keep each part of the answer in the visual or directly attached to its evidence. Use the same order in the guide and prompts: determine the complete answer, choose its visual encoding, compose for the format, and check with optional prose covered.

**Owner report (2026-11-23):** the developmental milestones presentation illustrated all four key skills. After changing only the format to A4, the response to a smile moved into a text block and the emphasis changed. Keep the visual answer when recomposing for a new format.

**Owner request (2026-11-23):** keep the question and format available in the editor after generation. Put the same picker beside Generate. Users can change the question, the format or both with the same sources. Revisions use the selected format. Opening a version restores its question and format.

**Owner request (2026-11-23):** Replace the format cards with a single button beside the link and file field. The button shows the selected format and opens a list with icons and the symbols 4:5, A4 and 16:9.

**Owner feedback on version 33:** the Monstera slide is much improved, but the leaf looks flattened to fit the grid and clear the text. Plan the illustration or chart for the selected aspect ratio before drawing. On the wide slide the stem can extend diagonally into the open space, with a leaf at its natural proportions and soil labels aligned on the other side of the cutaway.

**Owner feedback on version 32:** the artboard size is correct and the Instagram example is good. The Monstera slide gives the headline too much space, drops the final letter of “completely” onto its own line and leaves the illustration too small. Correct the Presentation layout at 1920 × 1080 px.

**Owner requirement (2026-11-22):** lock the artboard and graphic export at 1080 × 1350 px for Instagram, 1920 × 1080 px for Presentation, and 3508 × 4961 px for Print. Screen size and long content must not alter the output dimensions.

**Owner feedback on version 30:** Presentation and Instagram displayed almost the same illustration and information in different frames. Compose for the reading task, including the positions of objects and text, the hierarchy and type sizes, and the amount of supporting information.

**Owner decision (2026-11-22):** add a format choice to the start page. Presentation, Instagram and Print each set how much information to show and how large the text should be.

**Owner decision (2026-11-19, after Codex's `744413c`):** "Bring back bold colours". The poster again uses the moodboard's ONE bold, saturated colour field. Codex's readability rules (contrast against the actual surface, label sizes on phones) stay, now under `READABILITY_AND_PALETTE_V3` in [the guide](docs/visual-communication-research.md#text-readability-and-contextual-palettes).

**Typography update (2026-11-19):** apply `TYPOGRAPHY_BY_SUBJECT_V1` from [the guide](docs/visual-communication-research.md#typography-by-subject). The owner wants topic/story-aware font pairs (12 options), not an identical grid or one fixed pair for every subject. Typography only: illustration/palette work is deferred in this session.

**Owner's direction (2026-11-17):** "I want to ask for one piece of information and get one infographic depicting only that central piece of information with a lot less text and veering out of this monotonous formation of box after box." Runs were also "really really slow". The single-graphic poster is now the default output. The earlier long-page pipeline was removed from the code on 2026-11-19 (it is in git history before that date).

Earlier task: Apply the full-page visual approach developed in the Apollo 11 and US car color benchmarks to the infographic generator.

## Branch / PR

- The pencil loader update is in [PR #2](https://github.com/clil-june/Info-to-Graphics/pull/2). GitHub rollback point: `eadd6c8`. Live in version 39 (`1795458342-d2f8`).

- The callout update belongs to [PR #2](https://github.com/clil-june/Info-to-Graphics/pull/2). GitHub rollback point: `66c75d0`. The last recorded Artifact is version 38 (`1795455746-6776`, from `9252904`). Live in version 39 (`1795458342-d2f8`).

- The visual-only output update is in [PR #2](https://github.com/clil-june/Info-to-Graphics/pull/2). GitHub rollback point: `d1a3bd5`. Artifact version 37 (`1795449004-e33e`, from `1b9b004`) is the last recorded publication. The visual-only update is live in version 38 (`1795455746-6776`).

- The complete-answer update is on `feature/four-elements` ([PR #2](https://github.com/clil-june/Info-to-Graphics/pull/2)). The GitHub rollback point is `32843b6`, the parent of this update. Revert this update's commit to restore it while preserving branch history.
- Published as version 37 (`1795449004-e33e`) from `1b9b004`. The previous version is 36 (`1795442960-ce11`), published from `0c1def5`. To restore that published version after a later release, republish `index.html` from `0c1def5` with its existing capabilities.

- The editor format picker and version settings are live in version 36 (`1795442960-ce11`).

- The compact format picker is on `feature/four-elements`. Live in version 36 (`1795442960-ce11`).

- The instructions for drawing at the chosen aspect ratio are live in version 34 (`1795343842-b59c`). Watch for the Monstera-specific example being copied onto unrelated subjects.

- The slide layout corrections are live in version 33 (`1795343050-594e`).

- The fixed-dimension preview and PNG export are live in version 32 (`1795341792-f077`).

- Version 31 (`1795340031-8b1e`) includes the format selector, the Presentation and Instagram composition rules, and the drawn screen examples.

- **Artifact now live:** version `1795458342-d2f8` (version 39, "Anchored callouts + pencil screen (7785652)"), republished 2026-11-23 by Claude Code from `7785652`, which includes Codex's `eadd6c8` and `97299f1`; capabilities unchanged. Before that: version `1795455746-6776` (version 38, "Visual-only output (9252904)"), republished 2026-11-23 by Claude Code from `9252904`, which includes Codex's `ec5d72e`; capabilities unchanged. Before that: version `1795449004-e33e` (version 37, "Complete answer + illustrated examples (1b9b004)"), republished 2026-11-23 by Claude Code from `1b9b004`, which includes Codex's `32843b6` and `f05f223`; capabilities unchanged. Before that: version `1795442960-ce11` (version 36, "Format picker, editable versions, hero line (0c1def5)"), republished 2026-11-23 by Claude Code from `0c1def5`, which includes Codex's `10f6bb2`, `4e5a8e6` and `8408cec`; capabilities unchanged. Before that: version `1795344442-6558` (version 35, "Hero size, real colours, no eye-holes (02f19a1)"), which carried the stray ``, republished 2026-11-22 by Claude Code from `02f19a1`; capabilities unchanged. Before that: version `1795343842-b59c` (version 34, "Compose for target format (9f26a32)"), republished 2026-11-22 by Claude Code from `9f26a32` (Codex's composition-at-aspect-ratio rules); capabilities unchanged. Before that: version `1795343050-594e` (version 33, "Slide layout: whole words, bigger drawing (7f9bbb7)"), republished 2026-11-22 by Claude Code from `7f9bbb7`, which includes Codex's slide layout `05dab41`; capabilities unchanged. Before that: version `1795341792-f077` (version 32, "Fixed-size artboards + PNG export (50a41da)"), republished 2026-11-22 by Claude Code from `50a41da`, which includes Codex's fixed output dimensions `1d79478`; capabilities unchanged (downloads kept). Before that: version `1795340031-8b1e` (version 31, "Format compositions + drawn examples (1a0bafe)"), republished 2026-11-22 by Claude Code from `1a0bafe`, which includes Codex's screen compositions `1a0ffd5`; capabilities unchanged. Before that: version `1795337606-8b11` (version 30, "Label fitter makes room + output formats (c589751)"), republished 2026-11-22 by Claude Code from `c589751`, which includes Codex's output formats `5b8213a`; capabilities unchanged. Before that: version `1795336706-fed6` (version 29, "Answer first, each fact once (5b4d0c3)"), republished 2026-11-22 by Claude Code from `5b4d0c3`; capabilities unchanged. Before that: version `1795335948-c8f7` (version 28, "Circle and line positions fixed (710743c)"), republished 2026-11-22 by Claude Code from `710743c`; capabilities unchanged. Before that: version `1795115200-6af8` (version 27, "Multi-line labels fixed (a12d1de)"), which dropped every circle's cx and line's y2, republished 2026-11-19 by Claude Code from `a12d1de`; capabilities unchanged. Before that: version `1795114719-0bdb` (version 26, "Labels never overlap (60191c8)"), republished 2026-11-19 by Claude Code from `60191c8`; capabilities unchanged. Before that: version `1795113171-1050` (version 25, "Material colour palette (f92064c)"), republished 2026-11-19 by Claude Code from `f92064c`; capabilities unchanged. Before that: version `1795112140-b391` (version 24, "Bold colours back (01b4f1e)"), republished 2026-11-19 by Claude Code from `01b4f1e`; capabilities unchanged. Before that: version `1795111960-fcd8` (version 23, "Illustrated subjects + calm palettes (da0a865)"), republished 2026-11-19 by Claude Code from `da0a865`, which includes Codex's readability and palette update `744413c`; capabilities unchanged. Before that: version `1795110419-3636` (version 22, "Typography pairs, Google Fonts (dad6ec1)"), republished 2026-11-19 by Claude Code from `dad6ec1`, which includes Codex's typography update `7dd59b1`; capabilities unchanged. Before that it was version `1795108283-d1d0` (polar maps, `8c36123`). Before that it was version `1795107474-fecd` (house style, `798792a`). Before that it was version `1795104651-5c5b` (drawing styles, `f03bbaa`). Before that, it was republished from commit `21bb0e0` as version `1795103932-beef` (version 18, labelled "Optimisation pass (21bb0e0)"). Before publishing, the previous live version `1794993578-72c4` was checked to be byte-identical (ignoring line endings) to `index.html` at `7c58150`, so nothing edited only in the artifact was lost. Capabilities were carried forward unchanged: `sample` with images, `downloads`, `mcp` for `host:claude_browser` (`preview_start`, `get_page_text`). A read-back confirmed the new page is live.

- `feature/four-elements`, [PR #2](https://github.com/clil-june/Info-to-Graphics/pull/2).
- The Claude Artifact "Info to Graphics" was updated from this branch at commit `42ec716` on 2026-11-17 by Claude (version `1794929485-5eb5`, labelled "Mobile section review (42ec716)"). Its declared capabilities were kept: `sample` with images (needed by the mobile review), `downloads`, and `mcp` for `host:claude_browser`. Live validation is still pending.
- The Harvard visual reference remains in `references/harvard-period-products-visual/`.

## What changed

### Pencil generation screen (Codex, 2026-11-23)

- Added a responsive pencil animation with the chosen blue palette and natural pencil. It runs for Generate, Change it and Try a different picture. The waiting screen provides Stop and a still illustration for reduced-motion settings.
- A complete result stops the loop and opens the centered Done confirmation once before the infographic is revealed. Cancellation, errors and truncated results bypass the confirmation. Export controls return when the result is visible.

### Label hierarchy and leaders (Codex, 2026-11-23)

- Restated local line contrast, spacing and evidence hierarchy in the guide, generation prompt and revision prompt. Introduced SVG artwork and callout groups. Each grouped callout keeps its heading, value, qualifications and its own icon together.
- The renderer reserves space for marked artwork and shifts overlapping callout groups. Primary labels keep priority over secondary labels in the same column. A leader stays fixed at its evidence and follows the label edge at its other end. The light line and dark casing remain visible across light and dark fills, including in export.

### Visual-only output (Codex, 2026-11-23)

- Prompts, the guide and the three format examples keep all facts, qualifications and keys in the main visual. The footer contains the citation. A4 uses available space to improve the drawing and labels.
- New results are structurally pruned during streaming and before saving. The filter retains the theme, takeaway, visual and citation, removing independent notes, captions and closing blocks. Essential labels remain in the visual. Older saved versions keep their original layout.

### Illustrated examples and safeguards restored (Claude Code, 2026-11-23, owner-approved)

- **Review of Codex's `32843b6` and `f05f223`:** the format-adaptation and complete-visual-answer changes are kept. Still present: the hero rule, real colours, eye-holes, three levels, the bold field, the label fitter and the repetition check. Four things had weakened, and the owner chose "Restore and publish":
  1. **`comparisonExample(format)` drew small cup icons with plain bars** in all three formats, replacing the drawn moodboard examples (`EXAMPLE_SLIDE`, `EXAMPLE_FEED`, `EXAMPLE_OBJECT`). Those examples had stopped the earlier "maps and circles" drift.
  2. **The "no recognisable subject" failure mode was removed.**
  3. **The chart rule** allowed "a clearly labelled chart or diagram" without the subject.
  4. **The map rule** went from "the subject still appears as a large illustrated hero" to "when that clarifies".
- **Changes:**
  - **`COMPARISON_EXAMPLES`** draws Codex's same comparison and facts, with its headline "Brewed coffee has more caffeine" and source, in the house style: a coral field, cups seen from above with long hard shadows, a saucer under the espresso, and coffee beans as the marks (5 mg each: 19 for about 95 mg, about 13 for 63 mg; drawn as shapes, so no key is needed), plus the caption "One bean = 5 mg of caffeine". There is one layout per format:
    - **Instagram:** stacked, mug first and larger
    - **Presentation:** a wide side-by-side scene (`data-layout="wide"`)
    - **Print:** two columns, each cup above its beans

    `comparisonExample(format)` returns the matching one (Instagram for older formatless projects), and `formatExample()` is unchanged.
  - The failure mode "no recognisable subject: only circles, dots, plain bars, tiles or a bare map" is back.
  - The chart rule now says to build a chart from the real subject drawn in the house style, never from plain bars or dots alone.
  - The map rule adds back "the map is the stage, not the whole picture": the subject is drawn on or beside the map, and markers are small drawings of the subject where possible.


### Complete visual answer (Codex, 2026-11-23)

- The guide, README, agent instructions and working prompts agree on a complete visual answer. Each essential fact stays in the drawing or beside its evidence. Supporting text and word targets are secondary. The shared prompt includes a check with optional prose covered.
- All three prompt examples compare the same two coffee servings. The slide uses a wide drawing, Instagram stacks the comparison, and A4 aligns the two servings side by side. A4 can omit the question line. A separate key is optional when the marks need no further decoding. Palette rules choose accents from the subject and mood, with sufficient contrast required for text.
- The app compares the ready source inputs, question and format against the displayed version. A change of question or sources asks Claude to establish the answer again. Format-only changes preserve the complete visual answer. Older saved versions use the project's stored sources as their initial baseline because they previously shared one source list.

### Format adaptation (Codex, 2026-11-23)

- With an open version and the same question, switching format sends the previous artwork and current sources through the revision prompt. Generate, Change it and Try a different picture all use the visual-preservation instructions for this case. A new question can select different facts from the sources.
- The prompt and guide require each source-supported key fact to stay in the main illustration or in a direct label attached to its mark. The model can redraw, rearrange and shorten the labels. Notes below the visual are available for supplementary context.

### Restored hero line (Claude Code, 2026-11-23)

- **Cause of the stray `$1`** Codex removed in `10f6bb2`: Claude Code's Monstera-lessons edit replaced a line with a function that returned the literal text `$1` instead of the matched line, so that line was lost from `DRAWING_RULES`: "one hero: the subject itself (the animal, object, person, vehicle, food, building) drawn as a real illustration in the house style, large… A picture made only of dots, circles, bars or a bare map is not an illustration." This was live in version 35.
- **Fix:** the exact line is restored from `ef5825f~2`, just before the newer "the hero is the part that carries the answer" line.
- A search of `index.html`, the guide, README and HANDOFF found no other stray replacement tokens (the remaining `$1` in `svgSafe()` is an intended regex back-reference).


### Editor question and format (Codex, 2026-11-23)

- The same picker moves beside Generate on the editor screen. Changing an input sets up the next generation. Generate, Change it and Try a different picture use the question and format in the editor when clicked.
- Each new version stores its question, format and visual settings. Selecting a version restores those inputs and renders the original layout for export. Older versions without this metadata use the project’s previously saved question and format.

### Compact format picker (Codex, 2026-11-23)

- A button to the right of the source form displays the current format. The list opens below it and shows three proportion icons and their symbols. Screen readers have a name for each option. Choosing an option closes the list and saves the format with the project.

### Prompt cleanup (Codex, 2026-11-23)

- Removed the stray `$1` line from `DRAWING_RULES`. The hero rule remains in place. Inline JavaScript syntax and the one-line deletion were checked. The published Claude Artifact remains on version 35 pending a refresh.

### Lessons from three Monstera slides (Claude Code, 2026-11-22)

- **Owner's report,** with three outputs attached. The text placement and spreading now work, but "suddenly the main event, the plant pot, became small and the water is yellow". The owner wants a better version, and for the model to learn not to repeat these mistakes.
- **What went wrong:**
  1. **The answer's evidence was small:** the pot cutaway was pushed to the lower right while a big leaf took the left. This is the diagonal stem on the left from `9f26a32`'s Presentation example, copied literally.
  2. **The water took the amber accent colour.** No rule said real things keep their real colours.
  3. **Round leaf holes read as eyes, a face.**
  4. In the oldest output, the headline split "completel/y" and dwarfed the pot (fixed earlier, in `05dab41`).
- **Prompt (all formats, `DRAWING_RULES` and the palette rule):**
  - **Hero:** the part that carries the answer (the soil and pot cutaway for a watering question; the counted things for a count) gets about half the drawing or more and the centre of attention. Context objects stay smaller, simpler or cropped, and never push the hero into a corner.
  - **Real colours:** real things keep their real colours (water blue or clear, soil brown, leaves green). The accent marks the key label, number or a highlight, never repaints an object ("no yellow water, no blue leaves").
  - **New failure modes:** the answer-carrying part smaller than a context object or cornered; a real object in an unreal accent colour; round holes or dot pairs that read as eyes (cut slits or notches from the edge instead).
  - **Presentation example:** the Monstera-specific composition sentence is replaced by a general one: the evidence fills the centre at a generous size, labels are aligned beside the parts they name, and any context object is kept smaller.
- **Guide:** the Monstera worked example is replaced by these lessons, and the colour line is updated.
- **A corrected slide drawn by Claude Code** in the app (Presentation, 1920 × 1080), for the owner to compare: wide layout; headline "Water when the surface dries slightly"; a large terracotta pot cutaway as the hero, about 44–50% of the slide; a dry, cracked top layer; dark moist soil with blue drops and roots; two monstera leaves with edge slits (no holes); blue water from a watering-can spout onto the dry surface; and labels aligned to the layers ("Surface slightly dry: water now" in amber, "Below: moist, never soggy", "Never let it dry out completely" muted). It was deliberately **not** added as a prompt example, so a fresh Monstera run shows whether the rules work rather than whether Claude copies an example.


### Composition at the target aspect ratio (Codex, 2026-11-22)

- The drawing rules in `index.html` and the visual communication guide call for choosing the pose, viewpoint, crop or chart orientation and planning the labels before drawing. Resize artwork uniformly. If the shape and labels compete, adjust the composition and redraw.
- The Presentation prompt treats side-by-side and full-width arrangements as options and uses the Monstera cutaway as a concrete example. Drawn examples demonstrate the hierarchy and craft, with the composition chosen for the current subject.

### Presentation layout (Codex, 2026-11-22)

- Presentation headlines and prominent values wrap at word boundaries. The layout measures a side-by-side header first, fits it to a restrained type scale, and moves a longer header across the top if it needs more width. The same sizing runs in preview and standalone HTML and is included in the PNG snapshot.
- Illustration space is budgeted after the header, citation and any direct caption. Oversized empty SVG margins can be trimmed with edge clearance. The graphic keeps its aspect ratio.
- The Presentation prompt asks for a short takeaway, a properly framed illustration, qualifiers beside the relevant marks, and citation-only footers. The Monstera example uses “Water when the surface dries.” Instagram and Print keep their own prompts and layouts.

### Fixed output dimensions (Codex, 2026-11-22)

- The format selector, generation instructions, preview canvas and PNG export use the same fixed sizes. The content stays on a fixed design surface and scales uniformly to fit when it exceeds the available area.
- The PNG button renders the sanitized poster onto a bitmap of the exact width and height. The HTML button saves the same canvas proportions and the A4 print settings. Web fonts in PNG can fall back to local fonts if embedding is unavailable.

### Drawn examples for the screen compositions (Claude Code, 2026-11-22)

- **Review of Codex's `1a0ffd5`:** it parses, and `fitSoon()` is still called on render, streaming and the phone tab.
- **One risk, fixed with the owner's approval:** for Presentation and Instagram the prompt no longer included any drawn example (only the written bus description in `SCREEN_EXAMPLES`), and Instagram is the default. The drawn examples are what stopped the "only maps and circles" drift and carry the moodboard look.
- **New `EXAMPLE_SLIDE` and `EXAMPLE_FEED`,** drawn in the house style and following Codex's layouts and the owner's hierarchy rules. They are added after the matching `SCREEN_EXAMPLES` text, with a note not to copy the picture, colours or numbers. Print still gets the two original examples.
  - **`EXAMPLE_SLIDE` (Presentation):** the periods study. The headline is in words ("Gathered together, period days fill years of a life"), `<p class="ig-answer">≈ 7 years</p>` is the only place the number appears, and a compact 400 × 156 drawing has 39 year tiles with hard shadows, 6.96 of them red, labelled AGE 12, AGE 51 and "one tile = one year of life" at 16 units. Fonts are Manrope + Inter.
  - **`EXAMPLE_FEED` (Instagram):** coffee in a vertical reading order. A big mug from above with a long hard shadow, 19 bean symbols and "≈95 mg" (40 units) come first; below, a smaller, quieter espresso with about 13 beans and "63 mg" (26 units, muted ink). Secondary labels are 18–19 units, and the bean Key falls below the drawing. Fonts are Archivo + Inter.


### Composition by format (Codex, 2026-11-22)

- Presentation and Instagram now get distinct composition rules and examples in place of the same two HTML examples. The prompts instruct Claude to select supporting facts for the intended audience and draw for the reading direction. Generate, Change it and Try a different picture share these format rules.
- Presentation can place a large text value in the answer block beside a compact figure, or above a wide figure. Instagram places the key value beside its mark in the artwork and can put one short comparison or explanation below. The screen styles control the position and type sizes of these roles. Both bring the graphic ahead of its optional symbol key. Keep units and necessary qualifiers beside the claims they describe.
- Composition settings are carried through streaming, saved versions and HTML export. The new composition styles apply to newly generated or revised versions. Print still uses its A4 layout and page settings. See [Compose for the output format](docs/visual-communication-research.md#compose-for-the-output-format).

### Label fitter rewritten: make room, keep order, bars move with labels (Claude Code, 2026-11-22)

- **Owner's report** (screenshot, then the export `D:StudiesYear 4Semester 1AI StudioEngine Buildqueen 4.html`): "Knebworth (Stevenage), 1986" overlapped the heading "For comparison: Queen's next-biggest crowds" and was crossed by the comparison bars. "I've told you should never ever happen."
- **Cause, read from the export: the old `fitLabels()` made it worse.**
  - "fans, reported · each head = 1,000" (16) touched the 62-unit "250,000". It was shrunk and wrapped to two lines, which made it taller, so it hit the heading.
  - The smaller label always gave way. The heading (15 bold) was smaller than the items (16), so it was shrunk to 10.5, wrapped, and pushed down past all three items, ending below them.
  - Only text moved. The items' bars (`M25 490h210` and so on) stayed put, so moved text landed across them.
- **New `fitLabels()`:**
  - **Normalising** each label into one movable piece is kept: split multi-position tspans, stack colliding lines.
  - **Label off the left or right edge:** shrink to 85%, wrap to two lines, shrink to 75%, nudge inside. This is the only place line-breaking is used.
  - **Two labels on the same row overlapping:** the smaller is shrunk to 80% once.
  - **Every other overlap MAKES ROOM:** the lower label and everything at or below it move down together, preserving order and each label's own bar. "Everything" means all texts plus the "marks": direct children of the svg that are thin (at most 14 units tall and at least 3× wider than tall: bars, rules, underlines) and placed symbols `g[data-sym]`. Big illustration shapes and the map never move.
  - **A bar or rule cutting through a label** also counts. It must overlap by more than 6 px and 15% of the label's width, so a leader line touching a label's end, or a label sitting inside its own bar, doesn't count. The lower of the two and everything below it move down.
  - **Stroke thickness is counted** for marks: a stroked line's own box has no height, which first left the last bar clipped at the bottom edge.
  - **The drawing's `viewBox` grows** to hold everything that moved, strokes included.
  - Up to 400 passes, one fix per pass. A make-room always resolves its pair, because everything below moves equally.

### Output formats (Codex, 2026-11-22)

- The start page offers Presentation (16:9), Instagram (4:5, the default for new projects) and Print (A4 portrait). The choice is saved with the project. Saved posters without a format keep their legacy layout.
- Generate, Change it and Try a different picture all use the selected format. The prompt varies the density, supporting detail and expected graphic label sizes. The preview and standalone HTML share the format-specific layout and type sizes. Presentation can place a compact figure beside the heading or a panoramic drawing below it.
- The Print export includes A4 page size and 12 mm page margins. The browser can print it or save it as PDF.

### Answer first, every fact once, clear secondary level (Claude Code, 2026-11-22)

- **Owner's rules,** from the Queen poster:
  - The question asked for the ONE biggest concert, but the answer appeared twice: headline "Rock in Rio, January 1985: 250,000 fans", and again in the drawing as "Rock in Rio, Rio de Janeiro / 12 January 1985 / 250,000".
  - Hyde Park and Knebworth were unclear.
  - The owner wants, as rules: the information answering the question is the clear number 1 in the hierarchy; no repetition (each fact once, very clear); secondary information clearly secondary.
- **Prompt (`POSTER_RULES`):**
  - **Rule 1:** the answer (the number, place, date, name or thing asked for) is level 1: largest, boldest, in the accent colour, where the eye lands first, with nothing competing.
  - **Rule 4, "Every fact once, in three clear levels":**
    - Each fact appears exactly once on the page. The headline answers in words, and the drawing carries the key number once as its largest label. Every other label, the caption and the closing line only add; no number, name, place or date is repeated.
    - **Level 2** (comparison or runners-up) appears only if it helps, at most 3 items. Its numbers are at most half the size of the answer's, in the muted secondary ink, smaller or simpler, placed after or below the answer, under one short heading saying what it is (for example "For comparison: Queen's next-biggest shows"), one line per item ("Hyde Park, London, 1976 · 150,000+").
    - **Level 3:** notes, units and source, smallest.
  - **Rule 10 failure modes:** a repeated number, name, place or date; a supporting item as big, bold or bright as the answer; a comparison with no heading.
  - **Format hints:** the figcaption and closing line must add something new, never repeat.
- **Examples fixed to follow the rule:**
  - The periods example's headline "Periods add up to about seven years." repeated the drawing's "≈ 7 years"; it is now "Gathered together, periods fill years of a life."
  - The coffee example's caption repeated the Key's "5 mg"; it is now "Typical servings".
- **App check:** `checkNumbers()` also returns `repeated`, the numbers (same rules as the number check, so "1 in 5", 100% and small whole numbers are ignored) that appear more than once in visible text, excluding the Key and hidden symbol definitions. The stage shows "Shown more than once: … Each fact should appear once" when there are any.


### Lost circle and line positions (Claude Code, 2026-11-22)

- **Owner's report** (exported "Queen 2.html", Rock in Rio poster):
  1. The fan figures were headless, or their heads were in the wrong place.
  2. "Something weird on the left top."
- **Cause (a regression from the multi-line label fix, `a12d1de`):** adding `dx dy` to `SVG_ATTR` lost a space, so the list read `… x2 y2cx cy …`. `y2` and `cx` were no longer allowed, so the sanitizer removed every circle's `cx` and every line's `y2`.
  - The fans' head circles (`cx="16"`) fell to x = 0.
  - The stage lights and the singer's head piled up at the drawing's top-left corner.
  - This affected live version `1795115200-6af8`.
- **Fixes:**
  - The space is restored.
  - A guard after `SVG_ATTR` checks at load that the core geometry attributes are allowed (d, x, y, dx, dy, x1, y1, x2, y2, cx, cy, r, rx, ry, width, height, points, transform, viewBox, fill, stroke), and logs a console error naming any that are missing.


### Multi-line labels no longer overlap (Claude Code, 2026-11-19)

- **Owner's report** (with a screenshot of a fly agaric poster): two-line labels printed on top of themselves ("white spots" over "or warts", "gills free" over "of the stem"). "Make it never happen again ever! no matter where the text is on the page or what size it is."
- **Cause:** the sanitizer's `SVG_ATTR` allowed `x`/`y` but not `dx`/`dy`. Claude's line breaks (`<tspan x="…" dy="1.2em">`) lost their `dy`, so both lines sat on one baseline. `fitLabels()` compared whole `<text>` elements and couldn't see lines colliding inside one.
- **Fixes in `index.html`:**
  - `dx` and `dy` are now allowed on SVG elements.
  - `fitLabels()` normalises every label before fitting:
    - A `<text>` whose tspans each carry their own `y` is really several labels, so it is split into separate `<text>` elements (keeping fill, size, weight, anchor) and each is fitted independently.
    - Inside one label, lines (tspans with their own `x`) that land on each other get stacked with `dy="1.25em"`.
  - Line spacing for app-made and repaired breaks is 1.25em (was 1.15em, whose line boxes touched by about 2 px).
  - The pass limit is raised to texts² × 4 + 40. A label that has used its three steps can only move, so the loop always ends clean.
  - The live preview now runs `fitSoon()` too, so overlaps don't flash up while the poster is being written.


### Labels never overlap (Claude Code, 2026-11-19)

- **Owner's report:** in the last output, labels overlapped and were unreadable. "Make sure that if text doesn't fit you make it smaller or go down a row so that this won't happen ever."
- **`fitLabels()` in `index.html`** guarantees this in the app, not only in the prompt. After a poster is on screen, it measures every SVG `<text>` in the hero or illustration drawings. A label that overlaps another label, or crosses the drawing's left or right edge, is fixed in this order:
  1. 85% of its size
  2. broken into two balanced lines (`tspan`s at the same x, `dy="1.15em"`)
  3. 70% of its size, never below 10 units
  4. only then moved: down below the label it hits, or sideways back inside

  The smaller label gives way, so big numbers keep their size. If labels end up past the top or bottom, the drawing's `viewBox` grows. The fitter is safe to run repeatedly: the original size is kept in `data-fs0` and the step reached in `data-fit`.
- **`fitSoon()`** runs it after the poster is shown, again after web fonts finish loading (`document.fonts.ready`, `loadingdone`), and again when the phone "Infographic" tab is shown. It uses the next frame **or a 150 ms timer**, because frames don't run in background tabs; the first test missed this.
- Export copies the fixed drawing.
- **CSS:** the headline, question, closing line, caption and footer use `overflow-wrap:anywhere; hyphens:auto`, so a long word wraps instead of spilling out.
- **Prompt:** the failure-mode list now asks Claude to estimate label widths (about 0.55 × font-size per character, 0.62 for bold or wide fonts), keep 4 units between labels and inside the edges, and break long labels into two tspans.
- **Not handled:** text overlapping drawn shapes. That is often intended (a value on a bar); only text-on-text and text-off-edge are fixed. Labels in the round polar map's markers are fixed like any other text.


### Material Design colour palette (Claude Code, 2026-11-19)

- **Owner's request:** "expand the color palette using the material design color system so that the outputs will be more versatile and that the color will vary in accordance with context", linking m2.material.io's colour system page. The page was read in the browser pane (it needs JavaScript, so WebFetch only returned the title).
- **`index.html`, app side:**
  - `MATERIAL` holds the full 2014 palette exactly as published: 19 hues in colour-wheel order, 50 to 900 plus A100 to A700.
  - `MATERIAL_HEX` maps tokens such as `teal-700` to hex. `colorValue()` accepts hex or a token (and the `gray` spelling).
  - Tokens resolve in the sanitizer for SVG `fill`, `stroke`, `stop-color` and the map attributes, in `readTheme()`, in `expandMaps()` (including `data-fill` country colours) and in `posterSymbols()` (`data-color`).
- **`index.html`, prompt:** `READABILITY_AND_PALETTE_V2` becomes **`V3`**, and its palette paragraph is now a Material colour theme:
  - **Primary:** the bold field's hue comes from the subject's own world, with hue suggestions per kind of subject and "do not default to blue".
  - **Field tone:** set by the mood (300 to 900).
  - **Variants:** shadow and highlight tones are two to four steps darker or lighter in the same hue.
  - **Secondary:** the accent's harmony (analogous, complementary or triadic) follows the mood.
  - **Other roles:** a surface or cream colour, and real data colours kept.
  - **"On" colours:** a per-hue list of the lightest tone that carries white text at 4.5:1, computed at load from the palette with `luminance()`.
  - **Unchanged:** Codex's contrast and label-size rules. Map hints say tokens work there too.
- **Guide** section 9 has a new "Material Design colour theme (V3)" subsection. **README** mentions it.


### Bold colour field back (Claude Code, 2026-11-19)

- **Owner's choice,** asked directly after Codex's calm-palette rule (`744413c`) and the moodboard disagreed: "Bring back bold colours".
- **`index.html`:**
  - `READABILITY_AND_PALETTE_V1` is renamed `READABILITY_AND_PALETTE_V3` everywhere, so the change is visible.
  - Its palette paragraph ("calm palette… low to moderate saturation") is replaced by the moodboard field: ONE bold, saturated field (cobalt, sky, coral, teal, burnt orange, mustard, deep navy, deep plum, or a strong subject hue), 3 to 5 colours, a dark shadow tone, cream or white, one small warm accent, and real data colours kept.
  - New ink rule: cream or white on deep fields at any size; near-black or deep navy for small labels on bright fields, with cream there only for large text.
  - Codex's contrast thresholds and label-size rules are unchanged.
  - Rule 8's colour line and rule 6's wording say "bold" again.
- **Guide section 9** has the owner-decision note (V2). "Pick colours from the story" is rewritten for a bold field, and the calm sample palettes are replaced by bold pairs with computed WCAG ratios: navy/cream 13.20, teal/navy 7.25, burnt orange/near-black 4.78, and coral/cream 3.27 (large text only).
- **README** says "one bold, saturated colour field" again.


### Illustrated subjects back (Claude Code, 2026-11-19)

- **Combined with Codex's `744413c`** (readability and contextual palettes), which landed first. Kept Codex's palette, label and contrast rules, and my hero rule, maps-as-stage paragraph, 30,000-character guidance (now inside Codex's reworded SVG line) and coffee example (described without a colour, in line with Codex's example wording).
- **Open decision for the owner:** Codex's rule asks for calm, low-to-moderate saturation palettes, while the moodboard (twelfth change) and the coffee example use a bold saturated field (coral #C23F28). The examples now say the palette rule decides colours, but an example still steers. Either adjust the coffee example to a calmer field, or bring back the bold field if that is the wish.

- **Owner's report:** since the moodboard there had been more contextual graphics, but in the latest outputs they had mostly disappeared: "it's mostly maps and circles".
- **Likely causes, all in the prompt:**
  1. The polar-bear fix's strict "under about 15,000 characters" limit made a rich illustration the first thing to cut.
  2. "If one physical thing repeats many times, define it once" invited the hero itself to become a 32×32, 2–8-shape symbol.
  3. "Whenever the fact is about places, draw a map" with nothing requiring the subject to appear, so a map with dots was enough.
  4. Both prompt examples were abstract: a grid of tiles, and a row of circles from Earth to the Moon.
- **Changes in `index.html`:**
  - **Hero rule:** the subject itself (animal, object, person, vehicle, food, building) is drawn as a real illustration; a picture of only dots, circles, bars or a bare map is not an illustration.
  - **Repetition:** small repeated objects sit next to the hero, not instead of it.
  - **New failure mode:** "no recognisable subject".
  - **Symbols** are for SMALL repeated marks only and never for the hero.
  - **Length guidance** is now about 30,000 characters, with the detail spent on the hero and repeated marks kept cheap. The cut-off warning still catches long answers.
  - **Maps:** used only when WHERE is the answer, and "the map is the stage, not the picture": the subject appears as an illustrated hero on or beside the map, and markers can be small drawings of the subject. Size, amount, time or comparison facts draw the subject instead of a map.
  - **`EXAMPLE_SPACE` (circles) is replaced by `EXAMPLE_OBJECT`**, an object illustration in the moodboard's coffee style. It answers "Which has more caffeine: an espresso or a mug of coffee?" on a coral field: a mug and an espresso cup from above, with crema, a shine sliver and long hard shadows, and caffeine counted in coffee beans (a `bean` symbol placed with `<g data-sym>`, one bean = 5 mg): 19 for the mug (about 95 mg), about 13 for the espresso (63 mg). The fonts are Archivo + Inter, an approved pair. Source: USDA FoodData Central (brewed coffee 8 fl oz, espresso 1 fl oz).

### Text readability and contextual palettes (Codex, 2026-11-19)

- Added guide section 9 with WCAG contrast thresholds, mobile SVG label sizing, palette roles and three sample palettes.
- Added `READABILITY_AND_PALETTE_V1` to the shared poster rules. Generate, Change it and Try a different picture receive the policy. Updated the related layout instructions and removed the old saturated-field requirement and fixed SVG label minimum. Examples illustrate markup and composition.

### Typography pairs: Google Fonts only (Claude Code, 2026-11-19, after Codex's typography update)

- **Reviewed** Codex's `7dd59b1` (`TYPOGRAPHY_BY_SUBJECT_V1`, 12 pairs). It parses and doesn't touch the house style, maps or symbols.
- **Problem: General Sans would never load live.** It is only on Fontshare, and a claude.ai artifact only allows stylesheets from Google Fonts, so that pair would always fall back to Inter.
- **Replacement: Plus Jakarta Sans,** on the owner's request ("find replacements in google fonts but keep the font pairings similar"). Five fonts were compared side by side in the browser at 52 px: General Sans, Figtree, Plus Jakarta Sans, Hanken Grotesk and Onest. Plus Jakarta Sans was the closest (similar width, crisp geometric shapes, single-storey g, straight-tailed y), with Figtree a slightly rounder second. The pair is now **Space Grotesk + Plus Jakarta Sans**, updated in:
  - `TYPOGRAPHY_PAIRS`
  - the guide's table, with a note explaining why it was swapped
  - `TYPOGRAPHY_RULES` and the guide ("All catalogue families load from Google Fonts")
  - `fontLinks()`, whose Fontshare branch was removed
  - README
- **Other fixes:**
  - The prompt examples now use approved pairs: periods, Manrope + Inter; space, Space Grotesk + Plus Jakarta Sans. Before, they used DM Serif Display + DM Sans and Syne + Space Grotesk, which Claude might copy.
  - The leftover "Fraunces with DM Sans" suggestion in rule 6 (nature) was removed.
- **Note:** Special Gothic Condensed One and Secular One have only one weight. The app requests each weight separately, so that's harmless.


### Topic-aware typography (Codex, 2026-11-19)

- Added the 12 approved headline/text pairs and topic/tone selection rules to the guide, with the stable anchor `TYPOGRAPHY_BY_SUBJECT_V1`.
- Embedded the same catalogue and policy in `index.html` via `TYPOGRAPHY_PAIRS` / `TYPOGRAPHY_RULES` in `POSTER_FORMAT`, which reaches Generate, Change it and Try a different picture. It takes precedence over older mood menus and example fonts. Ordinary revisions preserve their current fonts unless typography or subject/tone changes.
- Added matching Claude/Codex session anchors and a README link. Script coverage takes priority; Hebrew gets defined sans-serif alternatives and RTL.
- SVG labels now inherit the text family instead of the display family. Added General Sans's Fontshare provider link (also used by export); Google Fonts remains the provider for the other pairs. Local fallbacks remain for offline use.
- No fixed grid or colour palette was introduced, and no illustration/map/source-processing behavior was changed.
- **Artifact not republished by Codex.** The live version recorded below still predates this typography update. Claude Code must publish the updated branch before the next live generation.

### Polar-bear bug fixes (Claude Code, 2026-11-19, thirteenth change)

- **Owner's report:** the polar-bear poster had "a weird line across the map and no polar bears". The house style itself "works well".
- **The line.** In the world-atlas data, Russia, Fiji and Antarctica jump from +180° to −180° longitude. On the flat Natural Earth map that jump was drawn as a straight line across the whole map, at the Bering Strait's latitude. `expandMaps()` now cuts each ring at the seam and closes each piece along the map's edge; a pole-enclosing ring (Antarctica) closes through the pole. Routes over the seam now keep going instead of jumping back across the map.
- **Round polar maps.** The flat map turns the Arctic into a thin strip, so `data-map="arctic"` / `"antarctic"` is new: an azimuthal equidistant map looking down on the pole, out to `data-rim` (default 55), with `data-rotate` (longitude at the bottom for the Arctic, at the top for Antarctica), a circular clip, sea and graticule. Markers and routes use the same `data-lon`/`data-lat`. The prompt tells Claude to use it for polar subjects and never to show polar regions on the flat map.
- **The missing bears, most likely cause.** An HTML tag inside `<svg>` (the prompt's own `<i data-sym>` symbol tag, or a `<b>` in a label) makes the browser's parser close the drawing there, so every shape after it is dropped. New `svgSafe()` runs before parsing:
  - `<i data-sym>` becomes `<g data-sym>`
  - `<b>`/`<strong>` and `<i>`/`<em>` become bold or italic `<tspan>`
  - `<span>` becomes `<tspan>`
  - `<br>`, `<p>`, `<div>` and `<small>` are removed

  It also handles an unclosed drawing (still streaming, or cut off).
- **Symbols inside drawings.** `<g data-sym="id" data-size="18" transform="translate(x y)">` (or with `data-lon`/`data-lat`) now draws the defined symbol centred there, coloured with its colour and with an accessible name. The prompt encourages this for things that repeat many times, which keeps answers short. It also says never to put HTML tags inside the svg, and to keep the answer under about 15,000 characters.
- **Cut-off answers.** Another possible cause: a long answer cut off before the bears. `ask()` now records `lastCut` (the runtime's `truncated` flag, or a kept partial answer). `wasCut()` also flags a figure or svg that was never closed. The version stores `cut`, and the stage shows a warning: "The drawing was cut off…".
- The numbers note is hidden when no numbers were checked, and it uses the singular for one number.
- **Not confirmed:** which of the two causes hit the owner's poster. The poster itself wasn't available, since it lives in the owner's browser storage.


### Moodboard house style (Claude Code, 2026-11-19, twelfth change)

- **Owner's request:** 17 reference images as "a moodboard for how I want the style of the infographics outputs".
- **What they share:**
  - flat mid-century poster illustration
  - one bold saturated colour field (cobalt, sky, coral, teal, orange, mustard, navy)
  - 3 to 5 colours
  - crisp hard-edged flat shapes, with no outlines, gradients or glows
  - light as hard geometry: lit and shade planes split by a clean edge, long hard diagonal cast shadows, one or two cream shine slivers
  - one large, simplified, often cropped hero object with lots of empty field
  - bold viewpoints (top-down, three-quarter, side, close-up)
  - repetition patterns (lemons, blueberries, umbrellas)
  - stripes as accents, a little wit, a fine print grain
- **In `index.html`:**
  - `DRAWING_RULES` rule 8 is now the house style (always used unless the user asks for another look). It replaces the 16-style menu from the eleventh change, which can be found in commit `f03bbaa`. The composition plan (7), craft (9) and failure checks (10) remain, re-aimed at the house style (for example, failure mode: gradients, glows, outlines or too many colours creeping in).
  - Rule 6 (art direction) now says that the subject chooses the colour field, palette, hero object and typefaces, not the drawing language. Its examples are rewritten as flat colour fields.
  - New `grain` texture: fine SVG noise drawn by the app as a data-URI background (Claude's own markup still can't use `url()`). It is listed first and suggested for the house style.
  - Both prompt examples were redrawn in the house style:
    - `EXAMPLE_POSTER`: sky field, 39 year tiles with hard shadows, 6.96 of them red
    - `EXAMPLE_SPACE`: navy field, a flat Earth with a hard night side, and a to-scale row of 30 Earths to the Moon
    They are about 7.7k characters together, down from 21.5k, so the prompt went from about 38.9k to 21.9k characters with a short source.
  - The SVG notes say that the colour field is the background and that gradients are normally unnecessary.


### Drawing method and styles from claude-drawing-skill (Claude Code, 2026-11-19, eleventh change)

- **Owner's request:** "implement this skill in the model", pointing at https://github.com/cloveric/claude-drawing-skill (MIT).
- **What that skill is:** a Python (numpy + Pillow) raster painting library with 83 styles, plus a method: plan the composition, script the scene, then render, look and fix 2–4 times against a per-style list of failure modes. The library can't run in the browser, so only the method and the style knowledge were adapted, as prompt rules for SVG.
- **In `index.html`:**
  - `DRAWING_STYLES` holds 16 styles that work as SVG shapes: flat vector, editorial print, blueprint, linocut, ukiyo-e, constructivist/Bauhaus, Art Deco, letterpress, isometric, stained glass, illuminated manuscript/old map, Greek black-figure, paper cut-out, golden-age comic, synthwave and a clean diagram sheet. Each has the subjects it fits and its rules, condensed from the skill's `docs/PRINCIPLES.md` and translated to SVG (for example, misregistration is a copy shifted 1–2 px, and Ben-Day dots are one path of tiny circles).
  - `DRAWING_RULES` replaces the old rule 7 ("Illustration craft") in `POSTER_RULES` with four rules:
    - 7: plan the composition (layers, one focal point, a third empty, the accent in 1–2 places, label placement)
    - 8: choose ONE style and keep to its rules
    - 9: craft within the style (gradients only where the style allows; hatching and dots as one path with many subpaths)
    - 10: check the drawing against real failure modes before writing (accidental reads, competing focal points, labels crossing things, too many colours, mechanical spacing, floating objects)
  - The prompt is about 5,400 characters longer (33.5k → 38.9k with a short source).
- **README** credits the skill.
- **Not done:** the skill's render-look-fix loop. The app makes one call, and the old screenshot review was removed for speed. It could come back as an optional "Polish the drawing" button that renders the SVG, shows it to Claude with the chosen style's failure list, and asks for one fix pass.


### Optimisation and clean-up (Claude Code, 2026-11-19, tenth change)

- **Faster opening.** pdf.js and mammoth.js (about 1 MB) no longer load before the app can respond. `loadLib()` adds them from cdnjs only when a PDF or Word file is first added. Schibsted Grotesk (no longer the UI font) was dropped from the start-up font link. Boot no longer renders the example poster hidden behind the start page.
- **Storage can't fill up.** Every draft and infographic used to stay in `localStorage` forever, with full source text, and none could be reopened since Recent was removed. `saveNow()` keeps the 12 most recent projects (newest first, the open one always kept). If the browser still refuses the save, it drops the oldest until it fits, and shows the "could not save" toast only if the open project alone doesn't fit.
- **Dead code removed (about 33 KB, 370 lines).** Removed: `RULES`, `FORMAT`, `planPrompt`, `composePrompt`, `sanitizePlan`, `EXAMPLE_HTML`, `EXAMPLE_ENTITIES`, the phone review (`reviewImages`, `inspectLayout`, `repairLayout`, `checkLayout`, `REVIEW_BUDGET_MS`), `coverageOf`/`planCovered`/`sourceMarkup`, `parseJSON`, `openProject`, the hidden title input and project picker, the review/coverage banners, and the `plan`/`review` fields. The `ig-*` CSS for long pages is kept, so older saved pages still render if a way back is added.
- **"Change it" prompt.** It is poster-only now and no longer repeats every symbol's SVG as JSON (the page's own `ig-symdefs` already has them). The JSON is only added for a page without symbol definitions.
- **"Try a different picture"** described the first `svg` on the page, which could be a symbol definition. It now uses the hero drawing's `aria-label`.
- **Live preview** skips a re-render when no new text has arrived.
- **README** rewritten to describe the one-call poster, not the removed plan/compose/review pipeline.
- `index.html`: 269.6 KB → about 234 KB (104 KB of that is the inline world map).


### Several links as sources (Claude, 2026-11-18, ninth change)

- **Owner's report.** After adding a link on the start page, dropping a second link "didn't process as a source, it was weird".
- **Cause, reproduced with a stand-in `mcp`.** Two links were read at the same time. The `tabId` regex didn't match the browser tool's "(tabId seed)" wording, so `get_page_text` read whichever tab was in front, and both sources got the second page's text.
- **Fixes.**
  - `readLinkQueued()` reads links one at a time.
  - The `tabId` regex also accepts a space separator.
  - A link already added is refused with a toast.
  - On the start page, a link dropped or pasted into the pill becomes a source at once (`insertFromDrop`/`insertFromPaste`). The drop handler runs in capture, prefers `text/uri-list` and stops the input from also inserting the text.
- **Verified** in headless Chromium with a stand-in `mcp`. Typed link + Enter, a dropped second link and a pasted third link gave calls in order (preview, get_page_text with `tabId`, then the next link), each source got its own page title, the duplicate was refused, and there were no page errors.
- Published to the Artifact as version `1794993578-72c4`.
- **Unverified:** a real drag of a link from another browser window in the Artifact, and real tab ids from the desktop browser tool beyond the first ("seed").

### Recent list removed (Claude, 2026-11-17, eighth change)

- The owner said the Recent list on the start page is unnecessary, so its markup, CSS and code are gone. Earlier projects stay in browser storage but can't be reopened from the UI; `openProject()` is kept, unused.
- **Verified:** `node --check`, plus the start page → Generate → workspace flow in headless Chromium at 1920 and 390 px (status "Done in 1 second.").
- Published to the Artifact as version `1794938489-34f5`.

### Start page proportions (Claude, 2026-11-17, seventh change)

- **Owner's request.** "Make everything a bit smaller in ratios more similar to the reference image."
- **How.** Every start-page size is now written in mockup pixels times `--s = clamp(0.6px, min(0.05208vw, 0.0926vh), 1.15px)`, that is, one 1920×1080 mockup pixel scaled to the window. Phones (under 700 px wide) get fixed readable sizes.
- **Verified in headless Chromium:**
  - at 1920×1080: pill 930×70, box 930×162, button 168×77, matching the mockup
  - at 1440×900 the measurements are 697×52, 121 and 126×58; at 1280×720 the screen is about two-thirds of the mockup size; a screenshot at 1440 was inspected
  - phone at 390 px: 342-wide fields
- Published to the Artifact as version `1794938424-3b19`.

### Start page and cleaner workspace (Claude, 2026-11-17, sixth change)

- **Owner's request.** The opening page should look like their mockup (`Info-to-Graphics_first_page.png`), and the sidebar should be much cleaner.
- **Start page `#home`.** It follows the mockup:
  - a full-screen brand blue `#1F5796` background, with the title "Info-to-Graphics" in Varela Round
  - a white pill "Drop file or link" with a paperclip to choose files
  - a translucent box "Name the information you're after"
  - a black "Generate" pill
- **How the start page behaves.**
  - A file can be dropped anywhere on the page. Pasting a link and pressing Enter adds a link source; other typed text, or a paste over 200 characters, becomes a text source. Added sources show as chips.
  - Generate waits for sources to finish reading, then opens the workspace and starts the run.
  - Earlier infographics are listed under "Recent".
  - Boot always opens the start page, and empty abandoned drafts are dropped from storage.
- **Workspace.**
  - The header is a blue bar with the wordmark (it returns to the start page), New and Export. The title input and project picker are hidden.
  - The sidebar has three unnumbered sections: Sources (compact chips, with "+ Add" revealing drop, link and paste), "The information you're after" with a black Generate pill, and "Change it" (a chat-style input with a send button, chips, and "Try a different picture").
  - Progress is a single line showing the current step, the timer and Stop. The long explanatory note was removed.
  - `addLink()` was split out of the link form so the start page can reuse it, and `newProject()` now opens the start page.

### Built-in world map and open-ended fonts (Claude, 2026-11-17, fifth change)

- **Owner feedback on three live outputs.** Apollo 11 was "really good"; red cars were good but "a bit schematic". Blue whales first came back as a list, and when asked for a map, the hand-drawn coastlines were poor. The owner always wants map-like visuals, but at higher quality, and wants more variety in fonts.
- **Built-in world map.** `WORLD_TOPO` is Natural Earth 1:110m countries from the `world-atlas@2` npm package (public domain, about 104 KB inline). `expandMaps()` replaces `<g data-map="world">` with real country shapes in the Natural Earth projection.
  - `data-view` sets the lon/lat crop and `data-box` sets the placement. Style comes from `data-land`, `data-sea`, `data-stroke` and `data-graticule`, and `data-fill="Country:#hex;…"` colours countries by name, with `COUNTRY_ALIAS` covering USA, UK, DRC and others.
  - Any element with `data-lon`/`data-lat` is translated to its projected position. `<path data-route="lon,lat …" data-curve>` gets a curved path.
  - Sea and clip are cropped to the projected view. The app adds the clip after sanitizing, and the map attributes are allow-listed.
- **Prompt changes.**
  - Whenever the fact is about places, the model must draw a map, never a list, and never draw coastlines itself.
  - It should crop tightly to the region that matters.
  - The craft rules now say to draw objects from their most recognisable view (a car from the side, not as a top-down box).
- **Fonts: any Google Fonts family.** `data-font`/`data-body` accept any family name matching `^[A-Za-z0-9 ]{2,39}$`.
  - `ensureFont()` loads regular, 700 and 900 as separate requests, so families missing a weight still load.
  - `FONT_GROUPS` lists about 100 families in 10 moods (including 14 Hebrew-capable fonts). It's shown to the model as ideas, with an instruction to pick a pairing for this subject and avoid habits.
  - `FONT_KIND` picks the fallback stack.
- **Export fixes.** The exported HTML is titled from the version's own headline; before, a stale project title such as "The source page never loaded…" leaked through. Font links are de-duplicated.

### Subject-themed art direction and illustration craft (Claude, 2026-11-17, fourth change)

- **Owner feedback.** Posters "look like a two year old's drawing". If the article is about space, the background, fonts and look should feel like space, and the same for any subject.
- **Theme in the reply.** The model sets the theme on `div.ig-symdefs`: `data-bg`, `data-bg2` (vertical gradient), `data-ink`, `data-muted`, `data-accent`, `data-font`, `data-body`, `data-texture` and `data-dir="rtl"`.
  - `readTheme()` and `applyTheme()` read it from the raw markup on every render, so each version keeps its own look. Only hex colours, the `FONTS` allow-list and the `TEXTURES` list are accepted.
  - If the ink doesn't contrast with the background, a light or dark ink is chosen automatically.
  - Dark backgrounds recolour the panel, track and ghost colours.
- **Fonts.** `FONTS` holds 22 Google families, including the Hebrew-capable Rubik, Heebo, Frank Ruhl Libre and Secular One. `ensureFont()` loads each one only when it's first used, and export links the theme's fonts.
- **Textures.** `TEXTURES` are CSS-only: stars, grid, dots, paper, lines, waves, glow and none.
- **Gradients are allowed in drawings.** The sanitizer now accepts `defs`, `linearGradient`, `radialGradient`, `stop`, `id` (on gradients only) and `fill`/`stroke="url(#id)"`. Gradient ids are prefixed per render so two renders never share them, and any other `url()` is still dropped.
- **Prompt changes.**
  - `POSTER_RULES` rule 6 maps subjects to art directions (space, ocean, food, history, sport, health, tech, nature), plus Hebrew handling.
  - Rule 7 sets the illustration craft: layered shapes with shadow and highlight, curved paths, one light direction, cast shadows, gradients, true proportions, depth, a restrained palette and leader-line labels.
  - The drawing element budget went from about 250 to about 400.
- **Two hand-made examples in the prompt.** `EXAMPLE_POSTER` (the periods poster, refined with gradients and shadows on a paper texture) and new `EXAMPLE_SPACE` ("Thirty Earths would fit in the gap": a dark star field, Orbitron with Space Mono, the Earth and Moon drawn with gradients and a to-scale strip; NASA figures 384,400 km, 12,742 km and 3,475 km).
- **Tier.** The poster, change and different-picture calls are back on `complex` first (better drawing), with a `default` fallback.

### One question, one picture (Claude, 2026-11-17, third change)

- **One Claude call per run.** `posterPrompt()` asks for a single poster: the question, a headline of at most 12 words, ONE central graphic in `figure.ig-hero` (preferably one free-form SVG drawing of the real subject, with a 400-wide viewBox), an optional closing line, and the source.
  - `POSTER_RULES` covers: one fact only, finding the real-world picture, no boxes, cards or panels, under 30 words outside the headline, and exact numbers.
  - It uses `modelTier: 'default'`, falling back to `complex`.
- **Symbols ride along in the same reply.** The model can define them in `div.ig-symdefs` (`svg[data-def][data-name][data-color]`, plus `data-accent`). `posterSymbols()` turns them into project entities, and CSS hides the block. When a poster has symbols, the key is titled "Key".
- **New example.** `EXAMPLE_POSTER` was made by hand from the Harvard notes: "Periods add up to about seven years." It shows 39 year-pages, each with a thin red strip, gathered into 7 red pages. It's the in-prompt standard and the bundled example (`exampleV: 2`, so stored old examples are replaced).
- **Validity and rendering.** `validPage` accepts `figure.ig-hero` in place of panels, and `renderIG` adds `.ig--poster`. SVG may use `font-style`.
- **UI changes.**
  - Step 2 is now "Ask for one thing to show", with a matching placeholder.
  - The progress steps are read, draw, check, with no plan step.
  - "New layout" is now "Different picture", which reruns with a note to use a different picture idea.
  - The change chips are new.
  - Refine uses the poster format when the current version is a poster.
- **No longer called** (code kept): `planPrompt`, `composePrompt`, `sanitizePlan`, `EXAMPLE_HTML`, `EXAMPLE_ENTITIES`, `coverageOf`, and the phone review functions.

### Faster, sturdier generation (Claude, 2026-11-17, second fix)

- **Why.** The owner reported that after the first fix "the model just isn't working" and asked for it to work and be quicker. A good run made up to five sequential Claude calls (plan, compose, inspect, repair, inspect), all on `modelTier: 'complex'`, with up to 170k characters of sources, and nothing visible happened until the very end.
- **The run is now two calls:** plan, then compose.
  - The plan uses `modelTier: 'default'` and up to 60k characters of sources (it was `complex` and 170k). Refine sends up to 50k (it was 120k).
  - Compose stays `complex`.
- **Fallback.** A new `ask()` helper makes each call. If a call fails (but not by stopping, refusal, consent or prompt size) or returns something unusable, it tries once on the other tier: plan goes default → complex, compose goes complex → default. A rejected call whose partial `e.text` is already usable is kept.
- **The plan is read as text** and parsed with `parseJSON()` instead of `sample.json`, so a stray sentence around the JSON no longer fails the run. The stage shows how many characters of the plan have arrived.
- **Live build.** Compose, refine and new layout stream with `onText`. `livePreview()` re-renders the partial page about every 0.7 s, so the infographic builds on screen as it is written. On error the stage is restored.
- **Phone screenshot review removed from the run.** `checkLayout`, `inspectLayout` and `repairLayout` are still in the file but are no longer called. Stored versions that carry review states still display them.
- **Errors** now include the code for unknown failures ("Something interrupted the request (code)"), and there is new copy for `timeout`.

### Fix: generation stopped discarding usable pages (Claude, 2026-11-17)

- **Problem.** After `42ec716`, a run threw away the whole infographic unless the composed page had exactly one `.ig-panel` per plan section, in order, each with its exact `data-section` ID. Otherwise it showed "Some planned sections are missing. Try again with a shorter brief." The owner reported that the app "doesn't work anymore". A stand-in sampler reproduced it: a well-formed page without exact IDs failed after three calls.
- **Coverage is now a note, not a gate.** `coverageOf()` lists planned sections whose IDs are absent from the page.
  - The page is always shown if it's usable (`validPage`), with a "Not on the page: …" note naming them.
  - A page with no IDs at all gets no note (coverage unknown).
  - `planCovered()` is kept as a wrapper.
- **Compose retries only when the page is unusable,** not for coverage. A good run is plan plus one compose before review.
- **Review time budget.** `REVIEW_BUDGET_MS` is 4 minutes from the start of the run.
  - Past it, the review is skipped ("skipped to keep the wait short").
  - If the budget runs out after the first inspection, the repair isn't attempted and the issues are reported.
  - If it runs out after the repair, there's no re-inspection ("fixed N sections; no time left to check the fixes").
- **New layout** no longer fails on coverage either; it carries the same note.

- Synced the research guide with the subject-shaped marks, visual-first opening, all-section review and prose reduction rules.
- The generator plans each section's relationship, visual encoding and direct labels. Composition checks that every planned section appears once in order. Complex drawings can use the existing safe SVG vocabulary with direct labels.
- The app captures mobile sections with and without explanatory prose. It sends the paired PNGs to Claude if images are available, replaces only flagged sections in one repair pass, and reviews again. The UI reports remaining issues or unavailable review.
- Kept named bar labels visible on phones. The exported HTML opens offline with fallback fonts and closed disclosures.

## What was verified

### Callouts, overlap regressions and pencil screen (Claude Code, 2026-11-23)

- Built-in Chromium pane, standalone page, stand-in `window.claude`:
  - **Wiring:** `fitSoon()` runs `fitLabels()` (ordinary labels; it skips `[data-callout]` text and treats `g[data-artwork]` and `g[data-callout]` as non-marks) and then `fitCallouts()`, which avoids artwork and ordinary text.
  - **Four earlier hard overlap cases,** under the strict per-line check with stroke widths counted: the owner's rebuilt Queen 4, the fly agaric two-line labels, lines without `dy` plus a multi-position text, and the deliberately messy poster. All had 0 overlaps, 0 bars crossing text and 0 text outside (6, 4, 7 and 12 lines). No regressions.
  - **The pencil screen** (with the stand-in slowed to 7 s): `#generationScreen` showed the pencil drawing a pie chart on the blue card with "Generating…", the timer and Stop, and the infographic stayed hidden. On "Try a different picture", Done appeared once at about 7.1 s for about a second, then the result was revealed (version 2) and the export buttons were enabled.
  - No console errors.
- Callout groups with real `data-callout` markup were not exercised beyond Codex's own fixture checks.


### Pencil generation screen (2026-11-23)

- Chromium with a stand-in sampler held a generation open across a complete drawing loop. Done appeared exactly once after the reply was accepted, and the infographic became visible afterward. Cancelled a revision and verified that its late answer could not replace the displayed infographic. Refusal and a truncated answer both skipped Done.
- Tested the result and confirmation on a 390 px mobile viewport and verified that reduced-motion mode leaves the drawing still. The live Claude Artifact has not yet been updated or verified.

### Label hierarchy and leaders (2026-11-23)

- Chromium rendered an annotated plate fixture in Presentation, Instagram and A4. A label initially overlapping the plate cleared it by 6 SVG units. The oil icon and its text moved together below the primary label with the same clearance. The evidence anchors stayed fixed, the other endpoints followed their label edges, and the two-tone lines and their endpoints survived in the export clone. Repeated fitting was stable at the final size.
- Confirmed both generation and adaptation prompts include priority groups and local contrast along the full leader. Production Claude generation remains unverified.

### Visual-only output, browser check (Claude Code, 2026-11-23)

- Built-in Chromium pane, standalone page, stand-in `window.claude`:
  - **A deliberately cluttered poster** (an `ig-q` question, an `ig-deck` paragraph, a figcaption, an aside inside the figure and another after it, and an `ig-take-t` closing line) came out with all of these removed. The headline, the SVG and the citation were kept, and no blocks were left outside the head, hero and footer.
  - **The updated `COMPARISON_EXAMPLES`,** run through the editor picker in Presentation, Instagram and Print: 0 label overlaps each. The Instagram version was inspected by eye: still the illustrated cups and beans, with the "1 bean = 5 mg of caffeine" key inside the drawing.
  - Earlier safeguards are still present in the prompt code: the hero rule, real colours, eye-holes, no-recognisable-subject, map-as-stage, chart-from-real-subject, the bold field, `fitLabels`, the repetition check and the `SVG_ATTR` guard.
  - No console errors.


### Visual-only output (2026-11-23)

- The inline script parsed and ran in a DOM test with a stand-in sampler. Tested the three format prompts and examples, the output filter, preservation of direct qualifiers and citations, the editor's Generate button, same-question format adaptation and all three locked canvas sizes.

### Restored examples and safeguards (2026-11-23)

- Built-in Chromium pane, standalone page, stand-in `window.claude` returning each illustrated example. The test used Codex's own flow: Generate as 16:9, then switch the editor picker to 4:5 and Generate, then to A4 and Generate (3 versions).
  - In each format the prompt contained that format's illustrated example (its viewBox and the "One bean = 5 mg" caption), no bar-chart example, the plain-shapes failure mode and the map rule.
  - Each render had 0 label overlaps and "All 2 numbers on the page appear in your sources". The 16:9 and A4 versions were inspected by eye.
  - No console errors.
- **Unverified:** real Claude output in the live artifact, especially the four-milestone A4 format switch Codex asks to check.


### Complete visual answer (2026-11-23)

- Inline JavaScript parses. A Node harness with a stand-in DOM and sampler exercised first generation, format-only adaptation of a four-part answer, ordinary edits, alternate illustrations, changes to the question and source text, source addition/removal, legacy records and retries. The runtime PNG canvas sizes and download wiring match the rollback point.
- Checked the same quantities and serving sizes in each of the three SVG examples, their proportional scales and label colours against the field. Headless Chromium could not start in this environment. Claude's output quality still needs a live Artifact test.

### Format adaptation (2026-11-23)

- Inline JavaScript parses. A Node harness with simulated DOM and sampler checked format-only Generate and Change it, alternate composition, whitespace-only question edits, question-only and combined changes, initial generation, legacy versions and retries. A prompt check confirmed that the previous illustration with all four milestones reaches Claude with the visual-preservation rule. Output dimensions and export handlers match the previous implementation.

### Format picker and per-version settings (2026-11-23)

- Built-in Chromium pane, standalone page, stand-in `window.claude`:
  - **Start page:** the compact format button reads "4:5" with a portrait icon beside the source field; its list shows 4:5, A4 and 16:9 with shape icons, and Escape closes it.
  - **Version 1:** generated as 4:5 with the question "Which has more caffeine, an espresso or a mug of coffee?".
  - **Version 2:** the editor picker set to 16:9 and the question changed; the next Generate made a Presentation version, and the prompt used the 16:9 rules.
  - **Back to version 1:** the question, the "4:5" button and the 4:5 artboard (ratio 0.80) were restored.
  - No console errors.
- **Unverified:** the same in the live artifact; exporting from a mixed-format history.


### Editor question and format (2026-11-23)

- The script parses. A Node harness with simulated DOM controls and sampler verified question-only, format-only and combined changes, revisions, alternate compositions, the live preview format, switching history, legacy versions, and retry after a failed request. An HTML parser confirmed one picker with its editor placement target. Output dimensions and export handlers were checked against the previous code.
- **Unverified (needs a Claude artifact test):** generating and revising across formats in the published Artifact, browser layout and exporting the displayed version from a mixed-format history.

### Compact format picker (2026-11-23)

- The script parses. A Node harness with stubbed DOM controls verified opening, choosing a format, saving and restoring the selection, arrow-key movement, focus return, and dismissal via Escape, outside clicks and focus leaving the picker. The HTML structure check confirmed the source form and its attachment button, the format control beside it, and the three visible symbols.
- Browser appearance and interaction in the published Claude Artifact are unverified.

### Monstera lessons (2026-11-22)

- Built-in browser pane, stand-in `window.claude`:
  - **The corrected slide** rendered in Presentation with 0 label overlaps and the drawing at 44% of the slide; inspected by eye.
  - **Generate in Presentation, Instagram and Print:** each prompt contained the hero rule, the real-colours rule and the eye-holes failure mode, and no Monstera wording outside the user's own sources and question. Prompt lengths were 30,076, 31,850 and 34,882 characters. No console errors.
- **Unverified:** a fresh real Monstera generation in the live artifact with these rules.


### Composition at the target aspect ratio (2026-11-22)

- The inline script parses. A Node harness verified that the composition rules reach the Generate and Change it prompts in Presentation, Instagram and Print and that the Presentation prompt includes the Monstera example. The canvas sizes are intact.

### Presentation layout (2026-11-22)

- Inline script syntax is valid. A Node regression harness with simulated DOM metrics checked the screenshot headline, a short headline, a wide numeric slide, repeat fitting, no cropping of overflowing drawings, and format isolation. The fixed-dimension export checks also passed with a canvas mock for all three sizes.
- **Browser check by Claude Code (2026-11-22),** built-in Chromium pane, standalone page, stand-in `window.claude`, Presentation format:
  - **A Monstera-like slide** with the long headline "Water your monstera only when the topsoil has dried out completely": 2 headline lines, no word split across lines (each word's line boxes measured), the header stacked across the top, the drawing 35% of the slide, 0 label overlaps, and the content fitting the 1920 × 1080 frame with no artboard scaling.
  - **`EXAMPLE_SLIDE`:** 0 split words, 0 overlaps, the drawing 47% of the slide, fits the frame, inspected by eye.
  - The order in `fitSoon()` is `fitPresentation` → `fitArtboard` → `fitLabels` → `fitPresentation` again if the viewBox grew → `fitArtboard`, so the two fitters cooperate.
  - **Change:** `EXAMPLE_SLIDE`'s headline was 9 words, against the new 3–6 word rule, and is now "Periods fill years of a life". "≈ 7 years" stays only in `ig-answer`.
- **Unverified:** a new Claude generation of the owner's Monstera slide in the live artifact.

### Fixed output dimensions (2026-11-22)

- Inline JavaScript parses. A local Node harness exercised the format sizes, preview scaling at two widths, fitting overflow, exact width and height passed to the PNG rasterization path, and the HTML proportions and print settings for all three formats.
- **Checked by Claude Code (2026-11-22), built-in Chromium browser pane, standalone page with the stand-in `window.claude` returning `EXAMPLE_FEED` in Instagram:**
  - the format labels read 1920 × 1080, 1080 × 1350 and 3508 × 4961 px
  - the preview frame ratio was 0.800 (4:5), and the labels had 0 overlaps after artboard scaling
  - the PNG button produced a 1080 × 1350 `image/png` of 1,386 KB, captured instead of downloaded; inspected by eye: headline in Archivo (font embedding worked locally), grain present, layout as in the preview, content uniformly scaled to fit
  - no console errors
- **Still unverified:** PNG export inside the claude.ai artifact (its content-security rules may block fetching fonts, so they fall back, or the foreignObject canvas may be treated differently); Presentation and Print PNGs; the Print HTML on one A4 page.

### Screen examples (2026-11-22)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, stand-in `window.claude`:
  - **Instagram** returned `EXAMPLE_FEED`: composition "feed", 4 lines, 0 overlaps, 0 text outside, all numbers found, inspected by eye. The prompt contained the drawn feed example, the bus text, and neither the slide example nor the Print pair.
  - **Presentation** returned `EXAMPLE_SLIDE`: composition "slide", `ig-answer` "≈ 7 years", 3 lines, 0 overlaps, 0 outside, inspected by eye. The prompt contained the drawn slide example and not the feed one.
  - The answer wraps to two lines only in the narrow browser pane.
- **Unverified:** real Claude output in the live artifact in both formats.


### Composition by format (2026-11-22)

- Inline script parses. A local Node harness checked different rules and examples for all three generation paths, retention of style and source rules, version metadata, streamed and saved layout hooks, symbol key order, and earlier-version and Print fallbacks. The export serializes those same rendered styles and attributes.
- Live Claude output and final on-screen layout remain unverified. The code checks confirm how the app requests and renders the roles, while the actual placement of illustrated shapes and labels inside the SVG is generated by Claude.

### Rewritten label fitter (2026-11-22)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, stand-in `window.claude`. The **owner's real Queen 4 drawing** was rebuilt as Claude wrote it: the old fitter's sizes, wraps, transforms and viewBox growth were removed, leaving the original 16/15 label sizes. Three earlier problem posters ran too (the fly agaric two-line labels; lines without `dy` plus a multi-position text; the deliberately messy one with stacks, an edge overflow and a long headline word).
- The strict check measured every line separately; marks were measured including half their stroke width:

  | Poster | Lines checked | Overlaps | Bars crossing text | Text outside | Bars outside |
  | --- | ---: | ---: | ---: | ---: | ---: |
  | Queen 4 | 6 | 0 | 0 | 0 | 0 |
  | Fly agaric | 4 | 0 | 0 | 0 | 0 |
  | Lines without dy | 7 | 0 | 0 | 0 | 0 |
  | Deliberately messy | 12 | 0 | 0 | 0 | 0 |

- Queen 4 kept its reading order (number, unit line, heading, Hyde Park, São Paulo, Knebworth) and every original font size, with each bar under its own item. Inspected by eye. No console errors.
- The first run of the new fitter left the last bar clipped at the bottom, because stroke widths weren't counted; this was fixed.
- **After rebasing onto Codex's output formats (`5b8213a`):** the same Queen 4 drawing in the **Instagram** and **Presentation** formats, 6 lines each: 0 overlaps, 0 bars crossing text, 0 text or bars outside, and no console errors. Print was not run.
- **Unverified:** a fresh real generation in the live artifact.

### Output formats (2026-11-22)

- Inline JavaScript parses. A Node harness exercised the selector state, the default for existing drafts, all three prompt paths, format metadata on the rendered article and the export markup, including A4 CSS only for Print. Legacy posters keep their original rendering mode.
- Browser layout and pagination are unverified in this session. Local Chromium could not launch in the execution environment. Live Claude generation is unverified.

### Hierarchy and repetition (2026-11-22)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, stand-in `window.claude` returning a poster that repeats like the owner's Queen poster (headline "Rock in Rio, January 1985: 250,000 fans" plus labels repeating 1985 and 250,000, and a Key with two "Fan, 10,000 people" symbols):
  - the stage showed "Shown more than once: 1985, 250,000", and 10,000 was not flagged
  - the prompt contained the level-1 rule, the once rule, the level-2 example heading and the new failure modes
  - the corrected periods headline and coffee caption were in the prompt; the old headline was gone
  - no console errors
- **Unverified:** whether real Claude output in the live artifact now follows the hierarchy (re-run the Queen question).


### Circle and line positions (2026-11-22)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, stand-in `window.claude` returning a Queen-style test poster (the fan symbol from the owner's file with `cx="16"` restored, stage lights, the singer's head and a `<line>` with `y2`):
  - the circles kept `cx` (120, 200, 280, 200)
  - the line kept `x2`/`y2`
  - all 10 placed fans and the key's fan have their head at `cx=16`
  - no console errors, so the guard found nothing missing
  - inspected by eye
- **Unverified:** a real run in the live artifact. Posters made with version `1795115200-6af8` keep their misplaced shapes when exported; re-generating or re-opening them in the fixed app re-sanitizes the saved markup. Exported files can't be repaired after the fact.


### Multi-line labels (2026-11-19)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, local server, stand-in `window.claude`. The check measured every line separately (each tspan with an `x`, otherwise the whole text) against every other line and against the drawing's edges:
  - **The owner's fly agaric case rebuilt** (two-line labels with `dy="1.2em"`): 4 lines, 0 overlaps, 0 outside, and it looked right by eye.
  - **Lines with `x` but no `dy`, plus one `<text>` holding three separately positioned tspans and an extra label on top:** 9 lines, 0 overlaps, 0 outside. The tspans were split into separate labels.
  - **During streaming:** sampled 4 times while the stand-in wrote the answer, with 0 overlaps each time.
  - No console errors.
- **Unverified:** the live artifact with real Claude output.


### Label fitting (2026-11-19)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, local server, stand-in `window.claude` returning a deliberately bad poster: two labels on top of each other, a stack of four, a label running past the right edge, a caption hitting a 40-unit number, two labels at the bottom edge, and a headline with a very long word.
  - **Before** `fitLabels()` ran: 9 overlapping pairs and 1 label outside.
  - **After:** 0 overlapping pairs, 0 labels outside, the big number untouched, the drawing grown from 300 to 354.1 units, and the headline inside the card. Inspected by eye.
  - The first attempt never ran because `requestAnimationFrame` doesn't fire in a background tab; this was fixed with the timer fallback.
- **Unverified:** a real overlapping output in the live artifact.


### Material palette (2026-11-19)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, local server, stand-in `window.claude` returning a poster written entirely in tokens. Each one resolved:

  | Token | Became |
  | --- | --- |
  | field `teal-800` | `#00695C` |
  | ink `teal-50` | `#E0F2F1` |
  | accent and symbol colour `amber-A200` | `#FFD740` |
  | gradient stops `cyan-A100` / `cyan-900` | `#84FFFF` / `#006064` |
  | `blue-gray-900` | `#263238` |
  | sea `light-blue-100` | `#B3E5FC` |
  | land `green-700` | `#388E3C` |
  | Norway `deep-orange-500` | `#FF5722` |

  The poster was inspected by eye. The prompt contains the Material theme rules and the computed "on" list (for example teal 700, blue 700, indigo 400; yellow, amber and orange none).
- **Unverified:** whether real Claude output in the live artifact now varies its colours with the subject and uses tokens correctly.


### Bold field back (2026-11-19)

- WCAG contrast computed in Node for 14 field/ink pairs; it is the basis of the ink rule (for example coral/cream 3.27, burnt orange/cream 3.33, coffee red #C23F28/cream 4.67).
- `node --check` (Node 14) on the extracted inline script: parses. No "calm", "low to moderate" or "V1" palette wording is left in the code, guide or README.
- Built-in browser pane, stand-in `window.claude`: the Generate and Change it prompts contain the bold-field rule, the ink rule, `READABILITY_AND_PALETTE_V3`, the 4.5:1 contrast rule and the hero rule; no V1 or calm wording; no console errors.
- **Unverified:** real output colours and label contrast in the live artifact.


### Illustrated subjects (2026-11-19)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, local server, stand-in `window.claude` returning the coffee example:
  - the prompt contains the hero rule, "The map is the stage", the coffee example and no "15,000"; its length was 27,038 characters
  - the poster rendered with 32 bean symbols drawn inside the svg, the app's Key box and "All 2 numbers on the page appear in your sources"
  - a first render had the mug's bottom bean row touching "≈95 mg" and a duplicate in-drawing bean note cut off at the edge; both were fixed, and a measured check found 0 bean/label overlaps
  - inspected by eye
- **Unverified:** whether real Claude output in the live artifact now draws illustrated subjects again (for example, a re-run of the polar-bear question).

- Readability and palette update: local inline JavaScript syntax and evaluated prompt checks for generation, revision and an alternate picture. Benchmarks and actual renderer contrast still need inspection in the live Artifact.

### Google-Fonts-only typography (2026-11-19)

- Every catalogue and Hebrew family was requested from the Google Fonts CSS API (curl): all return 200 except General Sans (400), which is why it was replaced.
- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane on the local server: all 24 families (the 12 pairs plus the Hebrew pairs) loaded with the same per-weight URLs the app builds (`document.fonts.check` true for all).
- With the stand-in `window.claude`, the generated prompt contains `TYPOGRAPHY_BY_SUBJECT_V1` and "Space Grotesk + Plus Jakarta Sans", both examples' approved pairs, and no "General Sans", "Fontshare" or "Fraunces with". No console errors.
- **Unverified:** real Claude pair choice and fonts loading inside the live artifact; Hebrew; "Change it" keeping the pair.


### Typography anchor (2026-11-19)

- Local checks: inline JavaScript syntax; generated prompts for all three entry points contain the anchor and all 12 pairs; the guide catalogue matches the runtime catalogue; provider URL routing and font fallback stacks; `git diff --check`.
- **Unverified (needs a Claude Artifact test):** actual family/weight loading under CSP (especially Fontshare), real Claude pair selection, live Generate/Change it/Try a different picture behavior and exported-font appearance. No live generation or Artifact publication was performed by Codex.

### Polar-bear fixes (2026-11-19)

- `node --check` (Node 14) on the extracted inline script: parses.
- A Node scan of the map data found the seam jumps: Russia 4, Fiji 2, Antarctica 1.
- Built-in browser pane, local server, stand-in `window.claude` returning three test posters:
  - **An Arctic map** with 10 bears placed by `<i data-sym>` inside the svg and a `<b>` inside a `<text>`. All 10 bears were drawn and the text after them survived. The map was round (circle clip), with Greenwich at the bottom and the Bering Strait at the top, and was inspected by eye.
  - **A flat map** with view "-180 40 180 84". The longest straight segment in the country paths is 9 px (it was about 400 px), and no line was visible.
  - **An answer cut inside the svg.** The cut-off warning showed and all 10 bears were still drawn (the first version of the fix missed unclosed drawings and was corrected).
  - No console errors.
- **Unverified:** a real polar-bear run in the live artifact.


### House style (2026-11-19)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, local server, stand-in `window.claude` that returns the two new examples:
  - the prompt contains the house style and no longer the 16-style menu; its length was 21,898 characters
  - both examples rendered, with grain on the field; at first the grain was too strong (the sky field looked grey) and it was reduced
  - the periods poster: "All 6 numbers appear in your sources"
  - the space poster flags "30" as expected, since it is derived and not in the test source
  - both were inspected by eye
- **Unverified:** real Claude output in the live artifact (how closely it follows the house style), and whether the data-URI grain shows inside the claude.ai artifact (if it's blocked, the field is simply flat).


### Drawing styles (2026-11-19)

- `node --check` (Node 14) on the extracted inline script: parses.
- Built-in browser pane, local server, stand-in `window.claude`: the prompt sent to `sample` contains the composition plan, the style list (checked for Editorial print and Blueprint) and the failure-mode list. A hand-made preview poster that follows the new rules (the app's example question "How much of a life is spent on periods?", Editorial print style: 508 dots, one per period from age 12 to 51, and a lifeline with a solid ≈6.96-year block) rendered with "All 7 numbers on the page appear in your sources". It was checked by eye and fixed twice, for hatching coverage and an empty band above the drawing. The poster was drawn by Claude Code following the rules; it is **not** output from the app's model.
- **Unverified:** how real Claude output in the live artifact responds to the new rules (style choice, quality, speed).


### Optimisation pass (2026-11-19)

- `node --check` (Node 14, with `||=` rewritten for that old parser only) on the extracted inline script: parses.
- Claude desktop app's built-in browser (Chromium) on a local copy served by a small Node server, with a stand-in `window.claude` (streamed `sample` returning a themed map poster, and a fake `mcp` browser):
  - plain start: start page shown, no pdf.js or mammoth script loaded, no console errors
  - a generated test PDF added through the file picker: pdf.js loaded on demand and the text was read ("ready")
  - a typed link, a pasted second link and a duplicate: `preview_start`/`get_page_text` called in order with tab ids t1 then t2, each source titled from its own page, duplicate refused with a toast
  - Generate: poster rendered with theme, map (country paths, marker, curved route), prefixed gradient ids and "Numbers checked"
  - "Change it" and "Try a different picture" gave versions 2 and 3; the change prompt had the page and no old FORMAT; the different-picture note used the hero's aria-label
  - storage: 20 stored projects were capped to 12 on the next save, with the open draft kept; with `setItem` made to refuse anything over 4 million characters, saving dropped the oldest projects until it fit (12 → 3), kept the open one and showed no error
- **Unverified:** everything in the live artifact (real generation, fonts, links, and pdf.js loading under the artifact's CSP); phone width and export after this change (that code wasn't touched); the artifact was republished afterwards (see Branch / PR), but nothing was run in it.


- Sixth change (Claude, 2026-11-17):
  - `node --check` on the inline script.
  - Headless Chromium on the standalone `index.html` with a stand-in streaming sampler, at 1920×1080 and 390×844: start page → type a text source + Enter → question → Generate → workspace with the poster, status "Done". Screenshots were inspected against the mockup.
  - The make/again/change regression passes when the workspace is opened through "Recent".
  - Published to the Artifact as version `1794937804-8e38`.
  - **Unverified:** Varela Round loading in the Artifact (fonts were blocked in the test, so it fell back to Arial), drag-and-drop of real files onto the start page, and link reading from the start page in the Artifact.

- Fifth change (Claude, 2026-11-17):
  - `node --check` on the inline script.
  - Headless Chromium on the standalone `index.html`. A stand-in whale poster using `data-map` (whole world, graticule), three `data-lon/lat` markers and a `data-route` rendered with correct coastlines and borders, markers in the right oceans, and a curved route, at 1440 and 390 px; screenshots were inspected. The make/again/change regression passes, and both examples render with no errors.
  - Published to the Artifact as version `1794935983-59f8` with capabilities unchanged.
  - **Unverified:** whether real Claude output uses the map syntax well, Google font loading in the Artifact (font requests were blocked in the test), `data-fill` country matching beyond a few names, and regional crops near the poles or the antimeridian.

- Fourth change (Claude, 2026-11-17):
  - `node --check` on the inline script.
  - Headless Chromium on the standalone `index.html` (external requests blocked, so the fonts fell back):
    - the periods example renders on its paper texture
    - a stand-in reply of the space example renders with a dark gradient and stars, `--dsp` set to Orbitron, 5 gradients with prefixed ids, and no page errors or sideways scroll at 1440 and 390 px; screenshots were inspected
    - the make, different-picture and change flow still passes (`complex` calls)
  - Published to the Artifact as version `1794934447-98f7` with capabilities unchanged.
  - **Unverified:** Google fonts actually loading inside the Artifact, real Claude output quality and theme choices, and speed on the `complex` tier.

- Third change (Claude, 2026-11-17):
  - `node --check` on the inline script.
  - Headless Chromium on the standalone `index.html`. The new example renders at 1440 and 390 px with no page errors and no sideways scroll; screenshots were inspected.
  - Same setup, with a stand-in streaming sampler:
    - make → one call (`default:poster`); headline visible mid-stream; a 10-cell pictogram with 2 filled from the defined symbol; key "Menstrual cup"; symdefs hidden; the number check passes
    - default tier failing → `complex` fallback
    - "Different picture" and "Use fewer words" each make one call and add a version
  - Published to the Artifact as version `1794933475-7a83` with capabilities unchanged.
  - **Unverified:** real Claude output quality and speed for posters in the Artifact.

- Second fix (Claude, 2026-11-17):
  - `node --check` on the inline script.
  - Headless Chromium on the standalone `index.html` with a stand-in streaming sampler:
    - normal → calls `plan:default`, `page:complex`; done, with the half-written headline visible mid-stream
    - compose rate-limited on complex → retried on default, done
    - plan not JSON twice → calls `plan:default`, `plan:complex`, then "Claude’s plan came back incomplete"
    - compose rejected with a usable partial text → kept
    - unknown error → "Something interrupted the request (weird_thing)" and the previous page restored
  - Published to the Artifact as version `1794932535-04a8` with capabilities unchanged.
  - Tried to run the live Artifact in the owner's desktop browser pane. It loaded, but the pane isn't signed in to claude.ai, so Claude was unavailable there.
  - **Unverified:** a live Claude run in the Artifact (speed, quality, whether `onText` streams there as documented).

- Fix (Claude, 2026-11-17):
  - `node --check` and `git diff --check` passed.
  - Headless Chromium with a stand-in sampler (images off):
    - untagged page → shown, no note
    - page missing one planned section → shown with "Not on the page: By age"
    - fully tagged page → shown
    - unusable reply → one retry, then "The page came back empty"
  - The example still renders at 1440 and 390 px with no errors, all 61 numbers found, and no sideways scroll.
  - Published to the Artifact as version `1794931746-6e26` ("Never discard a usable page; time-capped review"), with capabilities unchanged.
  - **Unverified:** the review time-budget paths (not exercised), and the whole flow with live Claude in the Artifact.
- Inline JavaScript syntax and `git diff --check`.
- Standalone Chromium at 390 px. The bundled example renders and exports HTML with closed details and no external stylesheet.
- Before publishing to the Artifact (Claude, 2026-11-17): the standalone `index.html` at `42ec716` loaded in headless Chromium at 1440 px and 390 px with no page errors. The example rendered 5 panels, the number check reported all 61 numbers found, and the page width at 390 px was 390. The Artifact itself wasn't opened after publishing.
- Chromium using a mock of the Artifact sampler. Verified real PNG capture, section count, prose hiding, targeted replacement, second review, a missing-section composition retry, the review-unavailable state, and cancellation.

## Still open

- **Unverified (needs a Claude artifact test):** the generated A4 result after a format-only change. Check that all four core milestones are visible in the illustration or direct labels.

- **Unverified (needs a Claude artifact test):** generation with the new composition instructions. Review a fresh Monstera slide for its leaf silhouette and label alignment, and a wide chart for faithful comparisons.

- Readability and palette update published (`1795111960-fcd8`). The prompt does not measure rendered contrast. Inspect the actual rendered text colours and local SVG backgrounds during validation, including any colours adjusted by the theme code.

- Typography update published (`1795110419-3636`). Verify `TYPOGRAPHY_BY_SUBJECT_V1` in the actual prompt; check topic selection and Hebrew/font loading. GitHub changes alone do not update the live app.

- **Unverified (needs a Claude Artifact test)** Live sampling, receipt of generated PNG files, runtime iframe/canvas restrictions, end-to-end generation quality, latency and Artifact publication.
- Linked sources use a plain-text extraction. Add structured tables, figure captions and visual chart data to the source intake so coverage can be verified against the full source.
- The number check matches values, not their units, populations or source locations. Add evidence-linked validation for those claims and keep regression inputs for Apollo 11, the car color study and a new topic.

## Next step

Published as version 39. Run one real generation and one revision; check that the pencil runs through the wait, Done appears once, and the result then opens. Test Stop on a real generation.

Published as version 39. Regenerate the healthy-plate brief in Presentation and Instagram. Check the vegetable qualification is clear of the bottle, the main quantities keep their order, and the lines remain readable at the rim of the plate and visibly reach the correct label.

Published as version 38 (`1795455746-6776`). Retest the healthy-plate brief in Presentation, Instagram and A4 with the same sources. Confirm that the plate and labels contain the complete answer and the source citation follows the figure.

Published as version 37 (`1795449004-e33e`). From the four-milestone presentation, switch to A4 with the same question and sources and run Generate. Repeat from the presentation with Change it. Cover the notes below the illustration and locate head and chest lift, babbling, smiling back, and reaching and grasping in the illustration or its direct labels. Compare with the version recorded above if the new result is weaker.

Publish the editor picker to the existing Artifact. Generate 4:5, then generate 16:9 from the same question. Switch between versions and check that the editor shows the right question and format and that the resulting export has the selected version’s dimensions.

Publish the start-page format picker to the existing Claude Artifact and check it in a browser at phone and desktop widths. Choose each format and confirm its symbol is reflected in the button.

Published as version 34 (`1795343842-b59c`). Regenerate the Monstera on the same brief in Presentation and check that the leaf uses open space with its natural silhouette. Review a wide chart for intact scales, alignment and readable labels.

Published as version 33 (`1795343050-594e`). Regenerate the owner's Monstera slide using the same source and brief. Check the headline and illustration on the 1920 × 1080 PNG, then verify a wide numerical slide and a fresh Instagram output.

Published as version 32 (`1795341792-f077`). In the live artifact, generate and download a PNG in each mode, confirm the exact dimensions in file properties, and check the edges and source line on a long example. Confirm the standalone Print HTML fits on one A4 page.

The composition rules and drawn screen examples are published (see Branch / PR). Generate the same source and question in Presentation and Instagram, ideally the car colours brief. On a large screen check for one strongly emphasized answer and one dominant visual. On a phone check for a vertical reading path, labels attached to their marks, and a supporting comparison only if it helps. Inspect both the preview and the exported HTML.

Also generate the same brief in Print to compare density, and verify that a browser prints the A4 export on one page.

Published as `1795336706-fed6` (hierarchy and no-repetition rules on top of the earlier fixes). Re-run the Queen concert question: heads and stage lights in place, the answer once and on top, Hyde Park and Knebworth as a clearly labelled comparison. Re-run the poster whose labels overlapped to confirm they are now readable. Run three different subjects to see the colours vary with context, then re-run the polar-bear question and one object subject to check that illustrated subjects are back. For the readability and palette update, measure text contrast and inspect annotation size on a phone-sized Apollo or map example, plus a warm-toned subject. Check a colour/label revision and the HTML export.

**Done 2026-11-19:** the typography update is published (artifact version `1795110419-3636`, with Plus Jakarta Sans in place of General Sans). Still to do in the live artifact: Test two different topics, Change it (pair preserved unless requested), Try a different picture, and a Hebrew example. Confirm the selected fonts really load. Only then mark the live behavior verified.

Previous next step (retained for context):

The artifact is live at version `1795108283-d1d0`. Re-run the polar-bear poster (it should now use the round Arctic map and show the bears), then run a few real posters (one place-based, one food or object, one about people) to see how closely real output follows the moodboard house style, and whether the grain shows in the artifact. In it, add a PDF to confirm the on-demand reader loads there. Then carry on with the step below.

Earlier: 
The owner tries a few one-question posters in the live Artifact and reports how long they take and whether the pictures are good. Tune `POSTER_RULES` and the example from what comes back. A second hand-made example on a different subject may help stop the model copying the calendar idea. Older note: The owner tries a run in the live Artifact while signed in, and reports the time or the exact error text (it now includes the error code). If layout problems on phones come back, consider bringing the screenshot review back as an optional button rather than an automatic step. Then run the two benchmarks without manual corrections. Inspect the opening, middle and final sections on a phone. Confirm the review status, source coverage and timing before merging.
