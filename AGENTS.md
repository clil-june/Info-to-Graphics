# Instructions for Codex (and other agents)

This repo is shared between Codex and Claude. Both follow the same workflow.

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

When designing, changing, or reviewing infographic generation, consult [the visual communication research guide](docs/visual-communication-research.md). Use it to identify the reader's question, choose a visual form that fits the source, and check that the result communicates the intended takeaway.

## Before handing work back

1. Update `HANDOFF.md`: Current task, Branch / PR, What changed, What was verified, Still open, Next step.
2. Commit it together with the code changes and push the branch to GitHub, so the other assistant and the owner see both.
3. If work is still in progress, put the branch name and pull request link in `HANDOFF.md`.

## What you can and can't verify

- You can test the standalone `index.html` in a browser: editor, board rendering, icons, PDF/Word/text reading, saving in the browser, export.
- You can't test the Claude features (building a board, "Ask Claude", reading images, reading links). They only run inside the Claude artifact on claude.ai. If you change that code, mark it **unverified (needs a Claude artifact test)** in `HANDOFF.md`, and don't describe it as working.
- The project is one file, `index.html`, with no build step. Libraries load from CDNs.
