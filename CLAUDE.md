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

The live artifact is titled **Info to Graphics**. It's published from `index.html`, minus the outer `<html>`/`<head>`/`<body>` wrapper, which the artifact skeleton supplies. To update it, find it with the Artifact tool's list action and publish to its URL. Keep its declared capabilities: `sample` (with images), `downloads`, and `mcp` for `host:claude_browser` (`preview_start` and `get_page_text`). Only Claude can update or test the artifact, so record its state in `HANDOFF.md` for Codex.
