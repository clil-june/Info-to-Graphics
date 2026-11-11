# Handoff

Last updated: 2026-11-11 by Claude

## Current task

Set up a shared Claude and Codex workflow: `CLAUDE.md`, `AGENTS.md` and this file. `README.md` stays the project guide.

## Branch / PR

- Branch: `workflow/claude-codex-handoff`
- Pull request: https://github.com/clil-june/Info-to-Graphics/pull/1

## What changed

- Added `CLAUDE.md` and `AGENTS.md`. Both tell the assistant to read `README.md` and `HANDOFF.md` at the start, check which branch has the latest work, and update and push `HANDOFF.md` with the changes before handing back.
- Added this `HANDOFF.md`.
- No changes to `index.html` or `README.md` in this branch.

Already on `main` before this branch:
- `d58d349`: first version of the app (then called Sieve). Visual-first board: icons on every item, plus pictogram, rings, cycle, hub, timeline, process, compare, bars, icon cards and illustration forms.
- `a3c77ae`: renamed the app to Info to Graphics. Boards saved under the old browser storage key (`sieve.v3`) still load. Exported board files now end in `.board.json`.

## What was verified

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

## Next step

Review and merge this pull request. Then open the Info to Graphics artifact on claude.ai, add one real PDF and one link, press **Build board from sources**, and record the result here.
