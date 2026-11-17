# Handoff

Last updated 2026-11-17 (Claude: blue start page from the owner's mockup, cleaner sidebar).

## Current task

**Owner's direction (2026-11-17):** "I want to ask for one piece of information and get one infographic depicting only that central piece of information with a lot less text and veering out of this monotonous formation of box after box." Runs were also "really really slow". The single-graphic poster is now the default output. The earlier long-page work below is kept in the code, but new runs no longer use it.

Earlier task: Apply the full-page visual approach developed in the Apollo 11 and US car color benchmarks to the infographic generator.

## Branch / PR

- `feature/four-elements`, [PR #2](https://github.com/clil-june/Info-to-Graphics/pull/2).
- The Claude Artifact "Info to Graphics" was updated from this branch at commit `42ec716` on 2026-11-17 by Claude (version `1794929485-5eb5`, labelled "Mobile section review (42ec716)"). Its declared capabilities were kept: `sample` with images (needed by the mobile review), `downloads`, and `mcp` for `host:claude_browser`. Live validation is still pending.
- The Harvard visual reference remains in `references/harvard-period-products-visual/`.

## What changed

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

- **Unverified (needs a Claude Artifact test)** Live sampling, receipt of generated PNG files, runtime iframe/canvas restrictions, end-to-end generation quality, latency and Artifact publication.
- Linked sources use a plain-text extraction. Add structured tables, figure captions and visual chart data to the source intake so coverage can be verified against the full source.
- The number check matches values, not their units, populations or source locations. Add evidence-linked validation for those claims and keep regression inputs for Apollo 11, the car color study and a new topic.

## Next step

The owner tries a few one-question posters in the live Artifact and reports how long they take and whether the pictures are good. Tune `POSTER_RULES` and the example from what comes back. A second hand-made example on a different subject may help stop the model copying the calendar idea. Older note: The owner tries a run in the live Artifact while signed in, and reports the time or the exact error text (it now includes the error code). If layout problems on phones come back, consider bringing the screenshot review back as an optional button rather than an automatic step. Then run the two benchmarks without manual corrections. Inspect the opening, middle and final sections on a phone. Confirm the review status, source coverage and timing before merging.
