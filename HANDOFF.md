# Handoff

Last updated: 2026-11-12 by Claude

## Current task

Make the boards more unique and context-aware using the *meaning* of David McCandless's "What Makes a Good Visualization?" diagram (informationisbeautiful.net). The owner asked explicitly for the app to understand the idea, **not** to build the diagram itself. The diagram's four elements are information, story, goal and visual form. A figure without a story is boring, one without a goal is useless, and one with only data and visuals is eye candy.

Direction chosen: direction 1 from the last handoff, the four elements as the brief for every figure. Direction 2 (a Venn figure type) was dropped, because the owner doesn't want the diagram rebuilt.

## Branch / PR

- Branch: `feature/four-elements` (from `main` at `9a82f5b`)
- Pull request: https://github.com/clil-june/Info-to-Graphics/pull/2
- The live Claude artifact ("Info to Graphics") was republished from this branch so the Claude features can be tested. It runs code that isn't merged yet.

## What changed

All in `index.html`, plus a "Design approach" section in `README.md`:

- **Board brief:** a strip at the top of the board with a one-sentence story and who the board is for. Both are editable. It also counts how many figures have all four elements.
- **Figure brief:** each figure stores `brief: {story, goal, metaphor}`, `focus` (an item index, or a column for compare) and `callout`.
  - The inspector has a Brief section with story, goal, visual idea, source tags, a highlight picker and the callout.
  - When something is missing, a **Fill what's missing with Claude** button appears.
- **Four-element marks:** four marks in each figure header (information, story, goal, visual idea), plus a label for what's missing ("Boring: no story", "Useless: no goal", "Eye candy: no story or goal", "Unsourced", "No visual idea"). Clicking a mark opens that field. These are hidden in exports.
- **Focus and callout:**
  - The item that carries the story is highlighted and the other items are muted.
  - A callout pill sits on the highlighted item.
  - Works for every figure type. For compare it highlights a column.
- **New visual styles:**
  - Timeline **Road**: nodes alternate above and below a winding path.
  - Bars **Icon stacks**: rows of the item's own icon, with an "icon = N" key.
  - Numbers **One big number**: a hero first number.
  - A "Visual style" control in the inspector switches between them.
- **Prompts:**
  - Claude is taught the four-element model.
  - It writes the board brief first, then figures whose titles state the point.
  - It picks forms and icons that echo the subject.
  - It reworks or drops figures that are boring, useless or just decoration.
  - Every figure edit also receives the board's story and audience.
- **Example board:** rewritten with briefs, story titles, focus and callouts, the road timeline and the hero number. Boards saved under the old example are swapped for the new one. User boards are untouched.
- **Fixes:**
  - "null" text showed in the inspector when a figure was selected (an older bug).
  - The phone layout scrolled sideways (page 726px wide on a 390px screen), caused by the road timeline's width and the header buttons.

## What was verified

| Check | How / where | Result |
|---|---|---|
| Inline script parses | `node --check` on the script in `index.html` | Passed |
| Example board renders, no page errors | Headless Chrome, standalone `index.html`, 1440px wide, light mode | Passed. Story strip, element marks, highlights and callouts, road timeline, hero number all render. |
| Adding a Bars figure and switching it to Icon stacks | Same desktop render, clicked through the UI | Passed. The new empty figure shows "Eye candy: no story or goal". |
| Inspector Brief section for a selected figure | Same desktop render | Passed. After the fix, no "null" text (checked by reading the inspector text). |
| Phone width (390px), dark mode | Headless Chrome, standalone page | Dark mode renders. Page width is 390px after the fixes (measured). The phone layout wasn't looked at again after the fixes. |
| Icon names used in the new code exist | Checked against Lucide 0.460.0 | Passed |

### Unverified

- **All Claude features, including the new prompts** (need a Claude artifact test):
  - whether Claude actually returns briefs, story titles, focus, callouts and styles
  - building a board, "Ask Claude", **Fill what's missing with Claude**, illustrations, reading images
- **Reading links** through `host:claude_browser` (desktop app).
- **Export:** HTML, SVG and `.board.json` output weren't opened. The `downloads` capability and the browser-download fallback weren't tested.
- **Reading files:** PDF, Word and HTML with real files.
- **Mid-width layout** (761–1100px).
- **Phone layout:** a visual look after the overflow fix.
- **Old saved boards:** loading boards saved under the old storage key, and swapping the old example board for the new one.
- **Board brief from Claude:** whether Claude's board-level brief fills the story strip on generation.

## Still open

- Test the four-element generation in the artifact on a real source, and judge whether the boards feel more engaging.
- Test reading a link in the Claude desktop app.
- Decide whether to host the standalone page on Netlify (Claude features stay off there).
- Possible next visual styles: process as a path, a hub drawn as the subject's own object, a scale or balance for comparing two options.

## Next step

Open the Info to Graphics artifact on claude.ai, press **Start my own**, add one real PDF or pasted article, and press **Build board from sources**. Check:
- Do the titles state points?
- Is one item highlighted per figure?
- Are any figures flagged? Is a road timeline or icon stack chosen where it fits?

Record the result here, then review and merge the pull request.
