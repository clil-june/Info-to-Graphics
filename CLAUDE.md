# Instructions for Claude

This repo is shared between Claude and Codex. Both follow the same workflow.

## Start of a session

1. Read `README.md`. It is the project guide.
2. Read `HANDOFF.md`. It has the current task, what changed, what was verified, what is open and the next step.
3. Check which branch has the latest work before changing anything:
   ```
   git fetch origin
   git branch -r --sort=-committerdate
   ```
   If `HANDOFF.md` names a branch or pull request, continue there. Don't start a new branch from `main` while that work is open.
4. Look at the latest changes on that branch or pull request (`git log`, the diff, and any PR comments). `HANDOFF.md` may be behind what was pushed.
5. Before editing anything, give the user a short recap in the chat:
   - what we worked on last time
   - what we decided or concluded
   - what actually changed (commits, files)
   - what the next step is

   Say clearly if a change is still pending (unmerged, unpushed) or hasn't been verified. If `HANDOFF.md` and the branch disagree, say so instead of guessing.

## Infographic design and review

### Required anchor before the next generation: TYPOGRAPHY_BY_SUBJECT_V1

Read [Typography by subject](docs/visual-communication-research.md#typography-by-subject). Choose from its 12 topic-aware pairs according to the story and tone, with script-capable alternatives when needed; do not impose one font pair or one grid on every infographic. Exception (owner decision, 2026-11-26): the Flat Isometric drawing style uses one fixed family, Plus Jakarta Sans (`FLAT_ISOMETRIC_TYPE_V1`); see [Flat Isometric style](docs/visual-communication-research.md#flat-isometric-style). Keep `TYPOGRAPHY_PAIRS` / `TYPOGRAPHY_RULES` in `index.html` synchronized with that section. The anchor overrides older font mood menus and example typography only.

Before generating in the live Claude Artifact, publish the updated branch's `index.html` to the existing Artifact with its capabilities preserved, then record the version in `HANDOFF.md`. Reading GitHub does not update the Artifact or its generation prompt. Preserve its current pair on ordinary revisions unless the user requests a typography change or changes the subject/tone.

When designing, changing, or reviewing infographic generation, consult [the visual communication research guide](docs/visual-communication-research.md). Use it to identify the reader's question, choose a visual form that fits the source, and check that the result communicates the intended takeaway.

**Default (owner's standing preference): prefer visual representation over text.** Apply this to every source you turn into an infographic:

- Put each essential part of the answer in the main visual or in direct labels attached to its evidence. Omit supplemental prose and reserve the footer for the citation.
- When a recurring object is useful as a mark, give it a recognizable symbol with a consistent meaning and colour. Place any key inside the visual. A repeated symbol can represent a count when its unit is clear.
- Keep words where they carry meaning: headlines and the takeaway, units and denominators, and qualifiers such as "reported", "estimated" or "about".
- Give every symbol an accessible name, so the piece still reads without the pictures.
- Reference example: the Harvard period-products infographic, where a tampon, pad, liner, cup and period underwear replace the product names.

## Before handing work back

1. Update `HANDOFF.md` (format below).
2. Commit it together with the code changes and push the branch to GitHub, so the other assistant and the owner see both.
3. If work is still in progress, put the branch name and pull request link in `HANDOFF.md`.

## HANDOFF.md format

Keep these headings: **Current task**, **Branch / PR**, **What changed**, **What was verified**, **Still open**, **Next step**.

- Under **What was verified**, say how and where each check ran, for example `node --check` on the inline script, headless Chrome on the standalone `index.html`, or a live Claude artifact.
- Anything not actually checked goes under **Unverified**. Don't describe something as working unless it was run.

## Where things can be tested

- **Standalone `index.html`** (local browser, headless Chrome, GitHub Pages, Netlify): editor, board rendering, icons, PDF/Word/text reading, saving in the browser, export. Here `window.claude` doesn't exist, so the Claude features stay switched off.
- **Claude artifact on claude.ai**: the only place to test building a board, "Ask Claude", reading images and reading links (the last needs the Claude desktop app). These use the viewer's Claude account through the artifact runtime.

## Claude-specific note

The live artifact is titled **Info to Graphics**. It's published from `index.html`, minus the outer `<html>`/`<head>`/`<body>` wrapper, which the artifact skeleton supplies. To update it, find it with the Artifact tool's list action and publish to its URL. Keep its declared capabilities: `sample` (with images), `downloads`, and `mcp` for `host:claude_browser` (`preview_start` and `get_page_text`). Publish the six Flat Isometric reference images in `references/flat-isometric/prompt/` beside the page, at the same paths; Isometric generations fetch and send them. The Flat Isometric SVG asset library (`assets/flat-isometric/`) is inlined into `index.html` by `tools/build_iso_library.py`; re-run it after changing the library, and never hand-edit the `ISO_LIBRARY` line. Only Claude can update or test the artifact, so record its state in `HANDOFF.md` for Codex.
