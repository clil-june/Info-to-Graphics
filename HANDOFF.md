# Handoff

Last updated: 2026-11-12 by Codex

## Current task

Add the shared visual communication research guide and use it when designing or reviewing infographic generation. Application changes are paused at the user's request.

Done: the shared Claude and Codex workflow (`CLAUDE.md`, `AGENTS.md` and this file), merged into `main` through PR #1. `README.md` stays the project guide.

Earlier development proposal, paused: making the boards more unique and context-aware, using David McCandless's "What Makes a Good Visualization?" diagram (informationisbeautiful.net) as the framework. Its four elements are information (data), story (concept), goal (function) and visual form (metaphor). A figure missing its story is "boring", one missing its goal is "useless", and one with only data and visuals is "eye candy". Two directions were proposed, and the owner hasn't chosen yet:
1. Make the four elements Claude's brief for every figure. Each figure gets a story-based title, a stated goal and a visual metaphor taken from the subject. Claude rejects its own "boring" or "useless" figures, and each figure shows a small four-element indicator.
2. Add a new editable overlap (Venn) figure type with 2–4 sets.

Credit McCandless for the framework, and don't copy his graphic into the app or repo.

## Branch / PR

- This update: branch `docs/visual-communication-guide`, pull request https://github.com/clil-june/Info-to-Graphics/pull/3 (documentation only).
- Also open: `feature/four-elements`, https://github.com/clil-june/Info-to-Graphics/pull/2. This is the four-element brief work (direction 1 above), built and pushed before the pause, plus the Harvard study benchmark checkpoint. It's not merged. Its own `HANDOFF.md` has the details and what's unverified. It also rewrites this file, so whichever pull request merges second will need its `HANDOFF.md` reconciled.
- Merged: `workflow/claude-codex-handoff` → `main`, https://github.com/clil-june/Info-to-Graphics/pull/1

## What changed

- Added `docs/visual-communication-research.md` as a reference for turning source text into effective infographics.
- Linked the guide from `README.md` and added the same standing design and review instruction to `AGENTS.md` and `CLAUDE.md`.

Previously merged in PR #1:

- Added `CLAUDE.md` and `AGENTS.md`. Both tell the assistant to read `README.md` and `HANDOFF.md` at the start, check which branch has the latest work, and update and push `HANDOFF.md` with the changes before handing back.
- Added this `HANDOFF.md`.
- Added a session-start recap step to both files (owner's request). After reading `HANDOFF.md` and checking the latest branch or PR changes, the assistant gives the user a short recap before editing anything: what we worked on last time, what we decided, what actually changed and the next step. It also flags anything pending or unverified.
- No changes to `index.html` or `README.md` in this branch.

Already on `main` before this branch:
- `d58d349`: first version of the app (then called Sieve). Visual-first board: icons on every item, plus pictogram, rings, cycle, hub, timeline, process, compare, bars, icon cards and illustration forms.
- `a3c77ae`: renamed the app to Info to Graphics. Boards saved under the old browser storage key (`sieve.v3`) still load. Exported board files now end in `.board.json`.

## What was verified

The guide and all three relative references were checked. This update is documentation only.

| Check | How / where | Result |
|---|---|---|
| Inline script parses | `node --check` on the script in `index.html` after the rename | Passed |
| Example board renders, no page errors | Headless Chrome, 1440px wide, on the standalone page, before the last fixes | Passed |
| Icon names used in code exist | Checked against Lucide 0.460.0 | Passed |

### Unverified

- **The fixes made after that render.** These are the hub labels sitting above or below their nodes, clicking a pictogram row to change its symbol, and the trimmed comparison rows. Their syntax was checked, but they weren't rendered.
- **All Claude features** (need a Claude artifact test): building a board, "Ask Claude" on a figure, Claude-drawn illustrations, reading image sources.
- **Reading links** through `host:claude_browser`. Needs the Claude desktop app. The tool argument names and the result shape the page reads were never seen in a real call.
- **Export:**
  - HTML, SVG and `.board.json` output were never opened.
  - The `downloads` capability (in the artifact) was not tested.
  - The plain browser-download fallback (in the standalone page) was not tested.
- **Reading files:** PDF, Word and HTML were not tested with real files.
- **Layouts:** phone layout (under 760px), the mid-width layout and dark mode were not looked at.
- **Old boards:** loading boards saved under the old storage key was not tested.
- **Artifact vs `index.html`:** whether the live claude.ai artifact matches `index.html` exactly. The artifact copy doesn't have the browser-download fallback. It saves through the `downloads` capability instead, which is expected.

## Still open

- Test the Claude features in the artifact with a real source.
- Test reading a link in the Claude desktop app, and fix the argument and result handling if needed.
- Take one look at the phone layout and dark mode.
- Decide whether to host the standalone page on Netlify (Claude features stay off there).

## Still open (new)

- Owner to choose direction 1, direction 2, or both for the McCandless work.

## Next step

Keep the generator and UI work paused until the user resumes it. When work resumes, consult the visual communication research guide and use its Bauhaus benchmark to review the proposed changes. Separately, open the Info to Graphics artifact on claude.ai, add one real PDF and one link, press **Build board from sources**, and record the result here.
