# Visual communication research for Info to Graphics

12 November 2026 · Research brief and reference guide

[Generation instruction for the app](#generation-instruction-for-the-app) defines the current one-question product. The full-document examples and benchmarks in this guide show techniques for larger editorial projects.

## 1. The design problem

Info to Graphics starts with prose, tables, or other documents. The design task is to identify what the reader should understand, extract evidence at the right level, and encode the relationships that answer the question. A polished result can still fail if the model selects the wrong relationship upstream. Munzner's nested model is a useful guide because it places the domain problem and data abstraction before visual encoding and implementation. Brehmer and Munzner further distinguish why the reader is doing a task, what goes in and comes out, and how the task is performed. [Munzner](https://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/) · [Brehmer and Munzner](https://pubmed.ncbi.nlm.nih.gov/24051804/)

Three jobs commonly get called text visualization:

| Job | What is represented | Useful output |
| --- | --- | --- |
| Explain the meaning of one text | Events, conditions, claims, examples and their relationships | An annotated timeline, process, argument map, comparison or illustrated explanation |
| Inspect the text itself | Wording, repetition, attribution and nearby context | Highlighted passages, concordance, Word Tree or aligned excerpts |
| Analyze a corpus | Topics, terms, entities, counts, changes and differences across documents | A document-by-theme matrix, trend chart, filtered network or overview with access to passages |

A chart of mentions measures the text or collection. A chart of facts reported in the text measures the subject. Put the unit of analysis and counting rule in view. Close reading retains passages and local context. Distant reading aggregates or abstracts across the collection. The strongest interfaces can move between them. [SoS TextVis](https://www.mdpi.com/2073-431X/8/1/17) · [Hearst, Information Visualization for Text Analysis](https://searchuserinterfaces.com/book/sui_ch11_text_analysis_visualization.html) · [Text Visualization Browser](https://textvis.lnu.se/)

## 2. How to turn prose into a visual explanation

### Identify the evidence before choosing a layout

1. **State a reader question.** Write a question with an observable answer: “Which test steps caused delays?”, “How did the school change across cities?”, or “What does this design claim depend on?” Record the audience and context of use.
2. **Extract the relevant units.** A unit can be an event, a time interval, a claim, an observation, a person, a quantity with units, or a step with conditions. Keep original wording or a source locator for each item.
3. **Identify the relation.** A link may indicate chronological order, ownership, shared occurrence, causation claimed by a source, support, contradiction, or a condition. Record the direction and qualifiers. Distinguish the source author's claim from the model's synthesis. A text that reports a belief or a disputed claim supplies evidence of the attribution. It may supply no evidence that the claim is true.
4. **Choose the visual form and write the reading order.** Decide what should be recognized first, what is needed to verify it, and which details can sit behind interaction. Keep exact wording where the nuance is essential. Use a compact text note for an inference too uncertain to encode graphically.
5. **Validate the encoded result.** Check that numbers, node identities, dates, arrows, labels, missing states and citations survive transformation. If the brief changes, revisit the relationship and evidence.

Rhetorical Structure Theory offers a vocabulary of relations such as evidence, condition, concession, cause and elaboration. Use it as a lens for identifying relationships in passages. The application can use a small set of well-defined relations without attempting to implement a full RST parser. The W3C PROV model is a useful reference for recording where derived statements came from. An app can start with document ID, page or passage locator, and status. [Mann and Taboada, RST definitions](https://www.sfu.ca/rst/01intro/definitions.html) · [W3C PROV-DM](https://www.w3.org/TR/prov-dm/)

### Keep what makes a statement true

| Source passage (synthetic) | Faithful visual encoding | Typical error |
| --- | --- | --- |
| “The team moved in 2025. The workshop opened in 2026.” | Two events on the same time axis | A causal arrow that the text never asserted |
| “If the inspection fails, return to assembly.” | A labeled branch from the inspection and a return loop | One straight sequence or an unlabeled loop |
| “Four of ten participants mentioned the latch.” | Four of ten with the denominator and the counting unit | An implied 40% failure rate |
| “A technician reported that the latch slowed assembly.” | An attributed observation, with a passage reference | A measured delay or universal causal finding |
| “A was easier to carry; B was quicker to set up.” | Options against separate criteria, with words or supporting measurements | An invented overall score |
| “A and B appear in the same report.” | A clearly labeled co-mention, if the question is about text occurrences | A relationship such as “works with” |

When normalizing, keep date precision, period, denominator, unit, comparison group, and population. Keep “may,” “estimated,” “reported,” and “under these conditions” where they change the claim. Explicitly represent zero, missing, not applicable, and unresolved conflict. Compare conflicting reports with their dates and methods before aggregating. For a multi-document corpus, document deduplication and the definition of a mention before counting.

### Use the picture and the words for different jobs

An illustration can make a mechanism, location, or physical relationship legible. For example, an annotated drawing of a hinge can identify the pivot and the release control, while a separate chart quantifies setup times. Place labels near the feature they name. Use comparison photographs taken from equivalent viewpoints if the reader must inspect a design difference. Use diagrams or verified imagery for details that carry technical or historical meaning. A generated scene may illustrate a concept. It cannot establish what a real object looked like or how it behaved.

Text can identify, define, quantify, contextualize, qualify, and guide attention. Put a takeaway in the title when supported. Place a local explanation beside the mark or event it describes. Put units and denominators where the reader needs them. Stokes and colleagues studied preferences and takeaways for annotated univariate line charts. Their participants often preferred the more heavily annotated examples in that study, and placement and semantic content changed what readers took away. This supports purposeful annotations with a clear job and a defined audience. [Stokes et al., Striking a Balance](https://vis.csail.mit.edu/pubs/vis-text-balance/) · [Stokes et al., Text Functions](https://arxiv.org/abs/2507.12334) · [Hearst, Show It or Tell It?](https://people.ischool.berkeley.edu/~hearst/papers/hearst_CACM23_preprint.pdf)

## 3. Select visual forms by relationship and reading task

| Reader needs to see | Good candidates | Precondition or design check |
| --- | --- | --- |
| Exact values or repeated criteria | Table, comparison matrix | Align like values and expose unknowns |
| Rank, magnitude or differences | Sorted bars, dots on a common scale | Comparable unit, period and denominator. Bars use a meaningful zero baseline |
| A measured trend | Line or small multiples | Actual observations on a meaningful time axis. Mark gaps and preserve dates |
| Order, milestones or overlapping periods | Ordered sequence, timeline, interval chart | Distinguish event from duration. Encode elapsed time only on a time scale |
| Distribution or variation | Dot plot, histogram, box plot | Requires multiple observations. A single average does not establish distribution |
| Part of a whole | 100% stacked bar or small pictogram | Known denominator and a defensible relationship between parts and whole |
| Relationship between measured quantities | Scatterplot | Paired observations. Association alone does not establish a causal claim |
| Conditional steps | Branching flowchart, swimlanes | Directed transitions labeled with conditions. Use swimlanes when actor roles matter |
| A measured flow | Sankey, alluvial diagram, flow map | Edge widths correspond to a meaningful measured quantity. Qualitative flow can use equal-width arrows |
| A hierarchy | Tree, indented hierarchy, treemap for quantitative parts | Verify parent-child relationships. A treemap also needs a defensible area measure |
| Many-to-many links | Node-link graph, adjacency matrix | Type each edge. Choose based on path tracing, lookup, density and available space |
| Claim and qualification | Claim-evidence diagram, annotated excerpts | Preserve attribution, counterpoints and scope |
| Locations, paths or spatial variation | Map, route map, small multiples | Geography must matter. Label the quantity and how it is normalized |
| Language around a phrase | Concordance, Word Tree | Use exact passages and make the anchor term clear |
| How parts fit or move | Annotated view, exploded diagram, sequence of views | Use verified geometry when the visual carries technical claims |
| Key idea without structured relationships | Short explanation or a grouped set of sourced observations | Check that adding a chart would make a legitimate comparison easier |

Cleveland and McGill's graphical perception research and later experiments by Heer and Bostock motivate using common position or aligned length for precise quantitative judgments. The task still governs: a map may be indispensable for route tracing, an image for a physical feature, and a table for exact lookup. Vega-Lite formalizes the link between a typed data field and a visual channel. This distinction is useful even if the app uses its own renderer. [Cleveland and McGill](https://doi.org/10.1080/01621459.1984.10478080) · [Heer and Bostock](https://idl.uw.edu/papers/crowdsourcing-graphical-perception) · [ONS chart choice](https://service-manual.ons.gov.uk/data-visualisation/chart-types/choosing-a-chart-type) · [Financial Times Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/Visual-vocabulary.pdf) · [Vega-Lite encodings](https://vega.github.io/vega-lite/docs/encoding.html) · [UNHCR on flows](https://dataviz.unhcr.org/chart-types/flow/)

### Let the subject carry the data

When a subject has a recognizable form that can carry the intended comparison, use that form as a data mark. Decide what the reader should see first, then choose which property of the mark will communicate it. The shape can identify the subject, its area can represent magnitude, repeated marks can show a count or share with a stated unit, and position on a common scale can support precise comparisons.

**Worked example — fish population, 1970 and 2015.** Use the same fish silhouette at both dates. Put the year above each fish, the population value inside or beside it, and the percentage change between the two. If the 2015 population is half the 1970 population, the second silhouette should have half the area. Apply the square root of the value ratio to both width and height, so in this case each dimension is about 71% of the original. Keep the population definition and units consistent. If the source supplies only an index, label the index and its baseline. Show estimates and rounding where they change the reading.

Choose this treatment when a recognizable subject helps readers grasp the direction and rough magnitude of a change. Use direct labels for exact values. For small differences or many categories, use a shared scale that makes those differences easy to see. A recognizable symbol can still identify each category on that scale.

**Readability check.** Hide the explanatory paragraph. The reader should still recognize the subject, see which value is larger and locate the exact values and dates. If the silhouettes suggest a larger change than the labels support, correct the scale before publishing.

## 4. Construct graphs before arranging them

### Define what a node and edge mean

- Give nodes stable IDs. Merge aliases only when they refer to the same entity. People, places, events and claims can coexist when the graph explains their roles and differentiates them.
- Define edge types and direction, with an evidence locator per edge. “A contains B,” “A precedes B,” “A claims B,” and “A and B co-occur” encode different relations.
- Use a node or explicit qualifier for relationships that depend on time, conditions, or additional parties. For example, “A supplied B with material C during trial D” can be modeled as a delivery event with typed connections.
- Store numeric weights only if the source or an explicit counting rule supplies them. Node size, line width and distance otherwise create claims a reader may assume are measured.
- Preserve underlying records when filtering. A visible subgraph is a particular view. The legend and visible filter state should explain what is included.

### Choose the representation

| Question | Representation | What to inspect |
| --- | --- | --- |
| Can I follow a path through a small set of dependencies? | Directed node-link layout | Crossings, readable arrowheads, direction and legible link labels |
| Which actors connect to which across many pairs? | Adjacency matrix | Row and column order, symmetry, legend and missing-state encoding |
| Which group or bridge stands out in an exploratory network? | Clustered or filtered network plus detail on demand | Definition of a cluster, visible thresholds, provenance and the effect of alternative layouts |
| What happens after a decision? | Flowchart or layered directed graph | Loops, exit paths and visible branch conditions |
| How does each passage support or challenge a claim? | Compact argument graph linked to excerpts | Claim attribution, evidence direction and conditional language |

In the Ghoniem, Fekete and Castagliola experiment, matrices performed better for many tasks as the tested graphs grew, while path finding consistently favored node-link diagrams. This is evidence for testing by task and density, rather than imposing a fixed threshold in the app. Graphviz dot is one option for hierarchical directed layouts. Force-directed layouts are useful for exploring topology and need interpretation: distances can emerge from the layout algorithm rather than a data field. [Ghoniem et al.](https://journals.sagepub.com/doi/10.1057/palgrave.ivs.9500092) · [Graphviz dot](https://graphviz.org/docs/layouts/dot/) · [Kobourov](https://arxiv.org/abs/1201.3011)

## 5. Make composition express the story

- **Choose the first fixation.** Give the strongest visual emphasis to a supported finding or the question readers should explore. Use size, position, contrast and whitespace deliberately. A bright photograph in the center will compete with a finding relegated to a caption.
- **Design the next step.** Use visual continuity, grouping, alignment and direct labels to make the reading order visible. Place related words and images together. If the reader needs to compare two values, bring them into the same visual frame.
- **Use color with a consistent meaning.** A color can denote a category, rank or emphasis. Keep the same semantics in related views. Supply labels or another cue where color distinguishes content.
- **Keep meaningful density.** Remove clutter around the intended comparison. Retain the annotation, unit, caveat or excerpt that changes the reading. Studies of embellishment and visual memorability address specific stimuli and tasks. Recognition, correct interpretation, and trust warrant separate checks.
- **Decide how much exploration to permit.** An explanatory graphic can guide an audience through one evidence-backed story. A research tool can expose alternative filters and competing readings. Preserve what the author chose to emphasize and what the reader is free to change.
- **Provide an accessible reading route.** Use descriptive text, labels and keyboard interaction. A complex graphic may need a short summary plus a structured equivalent such as a table or a longer description. If key context only appears on hover, static export and many assistive workflows will lose it.

[Segel and Heer](https://idl.uw.edu/papers/narrative) · [Hullman and Diakopoulos](https://www.hullmanlab.northwestern.edu/paper/2011/02/01/vis-rhetoric.html) · [Ajani et al.](https://visualthinking.psych.northwestern.edu/publications/Ajani_Declutter_2021.pdf) · [Borkin et al.](https://vcg.seas.harvard.edu/publications/20130101-what-makes-a-visualization-memorable) · [Mayer](https://doi.org/10.1111/jcal.12197) · [W3C complex images](https://www.w3.org/WAI/tutorials/images/complex/)

### Lead with a visual answer

Use this sequence when composing an infographic from source text.

1. **Choose the main relationship.** Write the one question the piece should answer and the shortest accurate answer. Decide what the reader should see: magnitude, share, change, a gap, order, or a physical relationship.
2. **Put the strongest visual in the opening view.** Pair it with a short takeaway and direct labels. Make the data-bearing graphic the largest or most prominent element in that view. Keep the legend close to the marks it explains. Put introductory prose and method details after the answer when they can wait.
3. **Assign a job to each visual element.** An icon identifies the subject. Length can compare magnitudes, position on a shared scale can show a gap, and repeated marks with a fixed denominator can show a share. If an image only identifies the topic, check whether a chart or a direct annotation is also needed to answer the question.
4. **Give every following panel a new job.** Combine an absolute number and its share when they explain the same finding. Add a panel when it answers a distinct question, shows a meaningful exception, or supplies necessary context. Let the material determine how many panels and chart types are needed.
5. **Cut repeated text before cutting context.** Give the headline, labels and annotations distinct roles. Remove a sentence that restates a marked value unless it adds interpretation. Keep the unit, population, denominator, date range and qualifiers such as “reported,” “estimated,” “about,” or “at least” wherever removing them changes the claim. Move detailed tables and methodology to a clearly labeled secondary layer. A standalone HTML export can keep that layer collapsed with an accessible disclosure. In a static export, keep essential context next to the chart.
6. **Highlight the evidence for the claim.** Use emphasis to identify the relevant mark or gap. Give symbols a stable meaning, use recognizable silhouettes, and add a direct label when similar symbols are hard to distinguish. A separate closing takeaway earns its space when it adds a synthesis or implication supported by the piece.

| Benchmark | What the visual does | What to keep beside it |
| --- | --- | --- |
| Harvard period-products ranking | Aligned bar lengths show the ranking. Recurring product silhouettes identify the categories. | Exact percentages, a clear scale, and the multiple-response note. |
| Harvard age comparison | Two marks per age group on one scale show which product leads. The distance between them shows the gap. | Age groups, series labels, and exact percentages. Highlight the group only if it answers the headline's question. |
| Harvard overnight use | Six highlighted symbols out of ten communicate a share at a glance. | Who is counted and what they reported. Keep rounding and any separate response categories clear. |
| Bird-loss redesign | Put the ten-bird pictogram and the 2.9 billion estimate together at the top. Identify the three highlighted birds as the share lost. Follow with habitat comparisons on a common baseline and a before/after view for the named species. | Region, starting year, estimate wording, dates or period labels, and greater-than signs on lower bounds. Keep the species label specific. |

**Five-second check.** Show the opening view at the intended screen size, then hide it. Ask “What happened?” and “How much or to whom?” For the bird example, the expected takeaway is that roughly three out of ten birds were lost since 1970 in the study region. This is a quick design check. Use a longer evaluation when the reading task requires it.

### Carry the visual explanation through the entire infographic

Before laying out the page, give each major finding one line in the plan. Record the reader question, the relationship the source supports, the visual mark that will show it, and the values and qualifiers the reader will need. Combine findings that answer the same question. Keep meaningful exceptions visible in the section where they change the story.

Apply the **cover-the-paragraph check** to every section that presents a finding. Hide the explanatory prose while keeping the takeaway, graphic, direct labels, units and essential notes. At the intended screen size, a reader should still be able to identify what is being compared, see the direction or pattern of the result, and locate the values or labels that support it. If a key comparison disappears, put it into the graphic or a direct annotation, then check the section again before export. The opening also gets the five-second check.

Plan the visual treatment for the middle and end alongside the opening. In every findings section, give the primary graphic enough room to be read at the target size. Carry forward the meaning of colors, objects and line styles so readers can follow them across sections. Choose the graphic by what it needs to explain. In the Apollo 11 example, a route map introduces the mission, a closer orbital diagram follows the two spacecraft after they separate, and an illustrated sequence shows the transition from capsule separation to parachutes to splashdown.

After the cover-the-paragraph check, review the default reading view from top to bottom. Remove prose that repeats what the graphic already communicates. Put supplementary explanation, detailed logs and tables in a clearly labeled secondary layer, with essential qualifications visible by the marks they affect. Inspect the first, middle and final findings sections at the intended screen size. Give a later section a clearer graphic if its main relationship still depends on a caption or a decorative icon.

Use the subject itself as the data mark when its shape or surface makes the relationship easier to read. A recognizable icon can identify a group. The graphic still needs a visible encoding such as length, count, position or area. For precise comparisons, use a shared scale across comparable marks. Keep qualifications beside the affected values and use short prose for interpretation, methodology and claims that have no sound visual encoding. Keep detailed tables available for lookup.

**Worked example — car colors.** A fleet pictogram shows how much grayscale grew overall, and an annual chart shows when it leveled off. Later sections need evidence of their own. Automotive paint chips can carry paired bars on the same scale to show which colors gained or lost share. For vehicle types, fill matched silhouettes by length so the reader can compare the same body shape across both model years. Put the years and exact shares beside the vehicles. A small comparison chart can then show why sports cars are an exception by plotting non-grayscale shares on a common scale and labeling each population.

### Compose for the output format

Identify the complete answer from the sources before planning its composition. Choose the visual that shows all the evidence the answer needs. Allocate space and position direct labels for the target format. Preserve essential units and qualifiers next to their marks, and keep the citation in the footer.

Plan the illustration or chart at the target aspect ratio. Choose the subject's pose, viewpoint or crop and place the labels alongside the relevant features. Use the grid for alignment. If space is tight, move a label with its anchor, redirect the object into open space or choose a different view. Keep recognisable proportions by using the same scale factor on both axes when resizing.

**Lessons from the Monstera slides (owner review, 22 November 2026).** Three outputs failed in the same ways: the pot cutaway, which carried the answer, became small or was pushed into a corner while a big leaf took the space; the water was painted in the amber accent; and round leaf holes read as eyes. Rules since then: the part that carries the answer is the hero and gets about half the drawing or more; context objects stay smaller or cropped; real things keep real colours (water blue, soil brown, leaves green) and the accent marks labels or numbers; holes and dots that read as faces are avoided. A subject-specific composition is no longer written into the general prompt, because it was copied literally onto the output.

For a chart, select the encoding and reading direction for the available space at the outset. In a wide comparison, horizontal bars on a common scale can leave room for direct labels. Check that the layout preserves the units, baseline, quantities and spatial relationships that give the marks meaning.

| Format | First thing to see | Arrangement of the visual answer |
| --- | --- | --- |
| Presentation, 16:9 | A short takeaway in large type and the complete visual answer, legible across a room | A single short number and its unit can sit in an answer block beside a compact visual. Give a comparison or scene the whole width under the headline when that makes the evidence clearer. Label each essential part near its mark. Aim for a 3–6 word headline in at most two whole-word lines. Reserve the footer for the citation. |
| Instagram, 4:5 | A short takeaway followed by a close-framed, directly labelled visual | Compose for a vertical eye path. Stack aligned comparisons on a common scale or place sequence steps top to bottom. Place values and qualifications close to their marks. Test on an actual phone. |
| Print, A4 | A takeaway and complete visual evidence at page size | Use the available space to enlarge the drawing, clarify the labels or improve spacing. End with the citation and check print preview at actual size. |

**Worked example.** The same coffee question runs through all three examples in the app prompt. A serving of brewed coffee contains about 95 mg of caffeine per 8 fl oz, and a serving of espresso contains 63 mg per 1 fl oz. The slide uses a wide comparison under the headline. The phone post stacks the two servings. The A4 example places them side by side with a shared baseline. All three keep the serving sizes and quantities directly attached to the two marks.

**When only the format changes,** use the open version as a starting point and verify that the answer is complete against the same sources. Redraw or rearrange the evidence and keep all essential facts in the main illustration or directly attached to their marks. Move any essential fact stranded in older prose into the visual and omit the rest. If the question or sources change, establish the answer again from the current request and sources.

For a format check, use the same brief and sources. In the four-milestone example, find head and chest lift, babbling, smiling back and reaching and grasping in the illustration or its direct labels on both the slide and the A4 page. In the healthy-plate example, the plate proportions and their qualifications belong with the drawing. Unrelated daily intake advice is omitted in every format.

### Generation instruction for the app

The app sends a compact version of these instructions with generation and revision requests. Keep `POSTER_RULES`, `ANSWER_PRESERVATION_RULES`, `OUTPUT_FORMATS` and `VISUAL_ANSWER_CHECK` in `index.html` aligned with this section.

1. **Identify the complete answer.** One reader question gives the infographic one takeaway. List every source-supported fact needed for that answer, including each requested part, relevant units, baselines and qualifications. Indicate what the sources cannot establish.
2. **Choose how to show it.** Give every necessary fact a place in the main drawing or a direct label attached to its evidence. Choose a diagram, comparison, map, sequence or illustration that makes the relationship clear. Place any key for repeated marks inside the graphic.
3. **Compose at the target size.** Redraw the evidence, place the labels and give the takeaway a clear visual hierarchy. Keep object proportions and data scales faithful. Use extra space to improve the layout.
4. **Check the visual answer.** At the intended size, locate every necessary fact in the graphic or its direct labels. Omit standalone captions, explanatory paragraphs, method notes, source summaries and closing lines. If a qualification is necessary, place it directly with its evidence. The footer holds only the citation. Check the facts against the sources and review contrast, clipping and overlapping labels.

### Examples to study

| Example | What to inspect and adapt |
| --- | --- |
| [Marie Neurath and Isotype](https://www.isotyperevisited.org/isotype-collection/index.php) | The transformation process: edit, organize, then assign pictorial forms. Study consistent symbols across panels and how a graphic supports explanation. |
| [Anatomy of an AI System](https://anatomyof.ai/) | A diagram and essay make a large system available at different reading depths. Study what connects a visible device to the infrastructure behind it, and how detail is grouped. |
| [Les Misérables Co-occurrence](https://bost.ocks.org/mike/miserables/) | The matrix defines a relationship precisely: appearing in the same chapter. Reordering reveals patterns without changing the underlying edges. |
| [The Word Tree](https://research.ibm.com/publications/the-word-tree-an-interactive-visual-concordance) | Repeated phrases appear as shared branches while the underlying language remains visible. Useful when readers want wording and context. |
| [Semantically grouped word clouds](https://pubmed.ncbi.nlm.nih.gov/30872231/) | Grouping can improve topic recognition in a keyword-summary task. Word size still needs a defined measure. Frequency does not explain who claimed what, or why. |
| [Minard's campaign map](https://www.davidrumsey.com/luna/servlet/detail/RUMSEY~8~1~372298~90139136%3ACarte-Firgurative-des-pertes-succes) | Route, direction, changing magnitude and temperature occupy different parts of a single composition. Inspect the legend and the connection between geography and the supporting data. |
| [Information Is Beautiful's design framework](https://informationisbeautiful.net/visualizations/what-makes-a-good-data-visualization/) | Use its four dimensions—information, story, visual form and function—as prompts for critique. |
| [NYT dialect quiz case](https://peabodyawards.com/award-profile/how-yall-youse-and-you-guys-talk-ny-times-dialect-quiz-2013/) | Personal input makes a geographic pattern meaningful to the reader. Compare the experience of reading a map with entering answers and inspecting the result. |

For more examples, the [Text Visualization Browser](https://textvis.lnu.se/) and the [University of Washington text visualization reading list](https://idl.uw.edu/readings/data-types/text/) are useful catalogs. The [Annual Review of Vision Science survey](https://doi.org/10.1146/annurev-vision-110323-110009) and [APS review of visual data communication](https://www.psychologicalscience.org/publications/visual-data-communication.html) connect perception, annotation and interpretation.

## 6. Apply this to the Bauhaus benchmark

Use the same source passage and explicitly vary the question.

| Brief | Primary graphic | What the reader should be able to answer |
| --- | --- | --- |
| Where and when did the school move? | Timeline of periods and move events, optionally supported by a small route map | Identify the order of the three cities and distinguish moving to Dessau from opening the new building |
| What made the Dessau building visually distinctive? | A verified image or drawing with a direct callout on the workshop wing | Point to the steel-and-glass curtain wall and explain which feature the annotation refers to |
| How did conditions for the school differ across the three cities? | Three aligned columns with sourced criteria such as venue and institutional status | Compare the same criteria across cities and identify where the sources leave a gap |

The foundation distinguishes the move to Dessau from the opening on 4 December 1926. It also describes the steel-and-glass workshop façade and clarifies that Gropius's private office and collaborators carried out the building's planning. Keep those details in the evidence. A date does different work in a timeline than it does in an architectural annotation. [Bauhaus Dessau chronology](https://bauhaus-dessau.de/en/institution/chronology/) · [Bauhaus Building](https://bauhaus-dessau.de/en/venues/bauhaus-building/) · [Bauhaus-Archiv chronology](https://www.bauhaus.de/en/discover/article/14-years-of-bauhaus/)

## 7. Evaluate and build the next version

### Test a reader outcome

Create a small benchmark corpus of diverse, rights-cleared samples: the Bauhaus passage, assembly instructions with a branch, a report with incompatible units, interviews with conflicting accounts, a sparse dependency network, and a dense co-occurrence dataset. Pair each with a question, expected answer, source passages, acceptable visual forms and likely failure modes. Include ambiguous and insufficient cases.

For a first review, compare the original, a structured visual with precise annotations, and plain text. Ask target readers to answer a neutral question and point to the evidence. Counterbalance the order where practical. Track answer accuracy, time, confidence, and whether the reader incorrectly infers a causal link or numeric relationship. Separately ask what they noticed first and what they remember. A short pilot yields useful design observations. A formal claim about one design outperforming another needs an appropriately designed study. [Lam et al., Seven Scenarios](https://pubmed.ncbi.nlm.nih.gov/22144529/)

### Research benchmarks for expanded workflows

1. Add a generation step that produces a **reader question, supported takeaways, typed relationships and source locators**, plus explicit ambiguities. Make that interpretation reviewable before committing to a composition.
2. Render a focused **timeline with an annotation anchored to an event**. An annotation can contain editable text, a verified image or clearly marked concept illustration, and a passage link. Preserve separate event and interval representations. Keep the focus stable when the layout changes.
3. Run all three Bauhaus briefs on the same source and record where the renderer supports the answer. For a controlled second test, use the branching procedure to check that the system understands conditional relations and loops.
4. Add graph or matrix support when the benchmark calls for it. A node-link diagram should expose the meaning and source of an edge. A matrix should preserve the same relations in a form suited to lookup.

### Acceptance checks

- Every factual claim, number, arrow and event can be traced to a passage, table row, or explicitly documented derivation.
- The main visual answers the selected question without an unsupported assumption. Changes to the brief lead to meaningful changes in selection or structure.
- The opening view passes the five-second and cover-the-paragraph checks at the intended screen size, with essential context still present.
- Each later findings section passes the cover-the-paragraph check at the intended screen size. The main comparison and meaningful exceptions remain legible from the graphic and its labels.
- A conditional step remains conditional, and adjacent dates remain separate events.
- Prominent color, size and position carry explainable meaning. The asset reinforces the reading order.
- Text is editable, key context survives export, and the result has an accessible text equivalent.
- A reader can answer the intended question accurately in a comparison against the current view.

This brief is a curated synthesis and product proposal. No application code or UI was changed during this research.


<a id="typography-by-subject"></a>
## 8. Typography by subject

**Owner decision · 19 November 2026 · Anchor: `TYPOGRAPHY_BY_SUBJECT_V1`.** This is the current typography policy for new infographic generations. It supersedes older unrestricted font menus, subject examples and example-poster fonts. It does not prescribe a shared grid, fixed type sizes, palette or illustration treatment.

Choose ONE pair from the topic catalogue below for a new infographic. First identify the subject AND the story's tone (a car's history differs from its speed record); the topic groups are starting points, not rigid categories. For food or craft, start with the nature/everyday-life pairs; for business or general data, start with Archivo + Inter or Work Sans + JetBrains Mono. For any other subject, choose the closest tonal fit from these same 12 pairs. An explicit user font request takes precedence.

Use the display family for the headline and large takeaway numbers; use the text family for captions, direct SVG labels, units, dates, legends and source notes. Maximum two families per infographic. Use two or three weight levels across the piece, choosing weights the families support. Keep numbers, units and qualifiers readable together; use tabular numerals for aligned numerical comparisons, never compress or distort letters to fit. Size SVG labels at their intended display width using [Text readability and contextual palettes](#text-readability-and-contextual-palettes).

No identical grid, fixed title position, fixed line breaks or fixed type sizes across topics: compose typography around the information and the drawing. The shared identity comes from clear hierarchy, consistent role assignments, restrained weights and readable annotations, not identical fonts or layouts on every topic. Topic selection does not impose colours or an illustration style.

Set data-font and data-body to the exact selected family names in .ig-symdefs. SVG text inherits the text family; do not hard-code an unrelated font. All catalogue families load from Google Fonts (the only font source a claude.ai artifact allows). Offline exports retain local fallbacks.

Language coverage takes precedence over this Latin-script catalogue. For Hebrew use Rubik + Heebo (neutral/technical), Secular One + Assistant (strong editorial) or Heebo + Assistant (quiet explanatory), with data-dir="rtl". For another unsupported script choose two script-capable sans-serif families rather than mixing unsupported Latin fonts with accidental fallback glyphs.

For a revision, preserve the current pair unless the user asks to change typography or the subject/tone changes; when selecting a new pair apply this anchor. Treat example fonts and the older general mood suggestions as non-binding; this anchor takes precedence for typography. Check hierarchy, glyph coverage and label collisions before returning HTML.

### Approved topic catalogue

| Story / tone | Headline and large numbers | Captions and labels |
| --- | --- | --- |
| Transport, mechanisms, industry | Barlow Condensed | Barlow |
| Transport, mechanisms, industry | Archivo | IBM Plex Mono |
| Space, technology, engineering | Space Grotesk | Plus Jakarta Sans |
| Space, technology, engineering | Instrument Sans | Chivo Mono |
| Nature, ecology, animals | Manrope | Work Sans |
| Nature, ecology, animals | Urbanist | Open Sans |
| Health, people, everyday life | Manrope | Inter |
| Health, people, everyday life | Archivo | Inter |
| History, culture, society | Jost | Libre Franklin |
| History, culture, society | Work Sans | JetBrains Mono |
| Sport, records, dynamic comparisons | Special Gothic Condensed One | Special Gothic |
| Sport, records, dynamic comparisons | Alumni Sans | DM Sans |

Plus Jakarta Sans replaces the owner's original General Sans (19 November 2026): General Sans is only on Fontshare, which a claude.ai artifact cannot load, and Plus Jakarta Sans was the closest Google Fonts match in a side-by-side comparison (similar width, crisp geometric shapes, single-storey g, straight-tailed y). The catalogue comes from the owner's Fontpair selection, not a claim that a topic objectively requires a particular font. [Fontpair sans-serif pairings](https://fontpair.co/category/sans-serif?tab=pairings).

### Runtime and handoff anchor

The browser generator cannot read this Markdown from GitHub. Its compact runtime equivalent is `TYPOGRAPHY_PAIRS` plus `TYPOGRAPHY_RULES` in `index.html`, interpolated into `POSTER_FORMAT`. Both `posterPrompt()` (Generate and Try a different picture) and `refinePrompt()` (Change it) receive it. Keep the catalogue and policy synchronized here and in the code. SVG annotations inherit the text family through `--txt`; exports use the same Google Fonts links, with local fallbacks offline.

Before the next live generation, Claude Code must read this section, fetch the latest `feature/four-elements`, publish its current `index.html` to the existing Info to Graphics Artifact while preserving capabilities, and record the version in `HANDOFF.md`. A GitHub commit alone does not update a published Artifact. Verify real font loading, a new generation, a revision and a different-picture run there. This update's real model behavior remains unverified until those checks run.

<a id="text-readability-and-contextual-palettes"></a>
## 9. Text readability and contextual palettes

**Owner decision, 19 November 2026 (V2):** the poster uses the moodboard's ONE bold, saturated colour field, not a calm or subdued one. The contrast and label-size rules below still apply, and matter more on strong colours. Text and essential graphics must remain legible at their final size.

### Pick colours from the story

1. Start from a material, setting, period or mood that fits the specific takeaway, and turn it into one bold field: a lunar route can sit on deep navy, a car story on teal or plum, a camping scene on burnt orange or pine.
2. Assign roles: the field, the object colour, a dark shadow tone, cream or white, and a small accent that fits the subject and mood. Use 3 to 5 colours; treat other shades as tones of these. Preserve meaningful source colours, such as the actual hues in a car colour comparison, and identify categories with labels, line styles, shapes or patterns as well as colour.
3. Choose ink against the actual local background. Check cream, white and accent text against the same thresholds as dark ink. Use a separate ink for labels if an accent is too close in tone to the background.

| Example | Field | Text | Ratio |
| --- | --- | --- | ---: |
| Apollo 11 | Deep navy `#16205A` | Cream `#F6EFDF` | 13.20:1 |
| Car colours | Teal `#5EC4B8` | Deep navy `#16205A` | 7.25:1 |
| Camping | Burnt orange `#D9662E` | Near-black `#1A1A2E` | 4.78:1 |
| (large text only) | Coral `#E8524F` | Cream `#FBF1E6` | 3.27:1 |

Ratios were computed with the WCAG 2.2 relative-luminance formula for these solid pairs. The last row passes only for large text, which is why bright fields need dark ink for small labels.

### Material Design colour theme (V3)

**Owner request, 19 November 2026:** expand the palette with the [Material Design colour system](https://m2.material.io/design/color/the-color-system.html#tools-for-picking-colors) so colours vary with the context. The poster keeps one bold field, built as a Material colour theme from the 2014 Material palette (19 hues, tones 50 to 900 plus A100 to A700 accents):

- **Tokens.** Claude may write any palette colour as `HUE-TONE` (for example `teal-700`, `deep-orange-A200`, `blue-grey-900`, also spelled `gray`); the app turns it into the exact hex in the theme, SVG paint, gradient stops, map land, sea, borders, country fills and symbol colours. Hex still works.
- **Primary.** The bold field takes its hue from the subject's own world (the real colour of the object, material, place, season or period), not a habitual blue.
- **Tone from the mood.** Bright and joyful 300 to 500; confident 500 to 700; serious, dramatic, historic or night 800 to 900; light and airy 100 to 200.
- **Variants.** The shadow tone is the same hue two to four tones darker; highlights are two to four tones lighter, or the hue's 50.
- **Secondary.** The accent's harmony follows the subject and mood: analogous (neighbouring hue) for calm and natural stories, complementary (about eight hues away on the wheel) for contrast and comparison, triadic (about five away) for playful ones. Use it sparingly and choose a tone that gives the intended emphasis without requiring a vivid accent.
- **"On" colours.** The prompt lists, for each hue, the lightest tone that carries white text at 4.5:1 (computed by the app from the palette with the WCAG formula; for example teal 700, blue 700, indigo 400; yellow, amber and orange never). On lighter tones, small text uses near-black or the hue's 900.
- Real things keep real colours (water blue, soil brown, leaves green); the accent marks labels and numbers, never repaints an object. Real data colours stay real, and 3 to 5 colours in total remain the limit.

### Measure contrast where the element appears

| Element | WCAG 2.2 AA minimum |
| --- | ---: |
| Ordinary text and images of ordinary text, including most labels, dates, units, legends, qualifiers and sources | 4.5:1 against the local background |
| Large text, at least 18 pt regular or 14 pt bold, approximately 24 or 18.67 CSS px respectively | 3:1 against the local background |
| Lines, arrows, markers and other parts of the graphic needed to understand it | 3:1 against adjacent colours |

Aim for 4.5:1 even for large titles where the palette allows. The enhanced AAA thresholds are 7:1 for ordinary text and 4.5:1 for large text. Compare using the unrounded WCAG ratio. Keep secondary text quiet through position, spacing and weight while maintaining sufficient contrast. An off-white surface can support a softer look while retaining strong contrast. [MDN Color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast) · [Harvard Use sufficient color contrast](https://accessibility.huit.harvard.edu/use-sufficient-color-contrast) · [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/#distinguishable)

Check the weakest part of the background under the lettering. Account for composited opacity, gradients, shadows and overlapping map fills. If a label is weak, try a quiet area with a clear leader, change the ink or add a small solid backing. Check the repaired pair and leader. Cream `#F6F4EA` on coral `#EF4D52` gives 3.25:1 for large text. Indigo `#17183F` on the same coral gives 4.72:1 and also passes for ordinary text. [W3C Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) · [WCAG contrast ratio](https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio)

### Check the rendered text

- Start at 14–16 CSS px for important short labels and around 16 CSS px for explanatory text at phone size. These are project defaults to adjust for the chosen font and script. Use a readable weight and keep numbers, units and qualifiers together.
- Measure inside the rendered SVG. At 340 CSS px wide, a 400-wide viewBox scales a 12-unit label to about 10.2 CSS px. Around 17 units gives about 14.5 CSS px before additional transforms. Shorten, wrap or move labels into adjacent HTML if the drawing is too crowded.
- Inspect the finished page at 360–390 CSS px viewport widths and on desktop. Check overlap, clipping, glyphs, numeric punctuation and right-to-left text after fonts load. Check the HTML export with fallback fonts if it will be read offline. Keep labels as text and check HTML text enlargement up to 200% and user spacing overrides. [W3C Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) · [W3C Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)
- Inspect the design in greyscale to see whether categories, routes and the takeaway remain clear. Measure the essential text and graphic pairs separately. Use a contrast checker for solid pairs and inspect the weakest local pair for layered areas.

### Generator rule

`READABILITY_AND_PALETTE_V3` in `index.html` supplies the condensed rule to Generate, Change it and Try a different picture. During revisions, apply the checks to affected elements and preserve unrelated design decisions. Verify colour and label size in the composed result, including the website's theme styles and the HTML export.
