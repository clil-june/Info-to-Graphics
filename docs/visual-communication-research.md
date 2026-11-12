# Visual communication research for Info to Graphics

12 November 2026 · Research brief and reference guide

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

### Implement the smallest meaningful slice

1. Add a generation step that produces a **reader question, supported takeaways, typed relationships and source locators**, plus explicit ambiguities. Make that interpretation reviewable before committing to a composition.
2. Render a focused **timeline with an annotation anchored to an event**. An annotation can contain editable text, a verified image or clearly marked concept illustration, and a passage link. Preserve separate event and interval representations. Keep the focus stable when the layout changes.
3. Run all three Bauhaus briefs on the same source and record where the renderer supports the answer. For a controlled second test, use the branching procedure to check that the system understands conditional relations and loops.
4. Add graph or matrix support when the benchmark calls for it. A node-link diagram should expose the meaning and source of an edge. A matrix should preserve the same relations in a form suited to lookup.

### Acceptance checks

- Every factual claim, number, arrow and event can be traced to a passage, table row, or explicitly documented derivation.
- The main visual answers the selected question without an unsupported assumption. Changes to the brief lead to meaningful changes in selection or structure.
- A conditional step remains conditional, and adjacent dates remain separate events.
- Prominent color, size and position carry explainable meaning. The asset reinforces the reading order.
- Text is editable, key context survives export, and the result has an accessible text equivalent.
- A reader can answer the intended question accurately in a comparison against the current view.

This brief is a curated synthesis and product proposal. No application code or UI was changed during this research.
