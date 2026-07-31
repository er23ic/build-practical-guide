# Instructional Visuals

Use this reference when a mathematical, scientific, architectural, algorithmic,
or engineering relationship would be materially easier to learn from a visual
than from prose, a short table, or a compact example alone.

The objective is not to decorate a guide. A teaching visual must externalize a
relationship, operation, comparison, state change, or chain of reasoning that
the reader would otherwise have to construct mentally.

## 1. Decide Whether a Visual Is Justified

Create a visual only when it makes at least one of these easier to observe:

- spatial location, orientation, projection, or correspondence;
- change from one state to another;
- decomposition or composition of quantities;
- a sequence, branch, loop, invariant, or causal path;
- a controlled comparison;
- the mapping between a formal expression and a physical or logical relation.

Prefer prose or a table when the content is only a list, a single fact, or a
small mapping that does not gain explanatory structure from drawing. Do not
turn headings and paragraphs into boxes merely to make a page look visual.

## 2. Write the Visual-Reasoning Brief First

Complete this brief before drawing or writing an image-generation prompt:

```text
Reader and prerequisite:
One teaching question:
Intended insight:
Visual claim:
Visual action:
Start state:
Intermediate state or comparison:
End state:
What remains invariant:
What changes:
Known quantities:
Unknown quantities:
Formula-to-mark mapping:
Required context:
Elements to omit or suppress:
Intended viewing order:
Short alternative text:
Long-description location:
Human QA prompt:
```

Use one visual claim, not necessarily one panel. Multiple panels are justified
only when they form necessary stages or a controlled comparison supporting the
same claim. Split the visual when its panels require unrelated insights.

The intended insight is one sentence the target reader should be able to say
after viewing. The visual claim states what the marks themselves will prove or
make observable. If the claim can be removed without losing information from
the prose, reconsider whether the image is needed.

## 3. Translate the Concept into a Visual Action

Choose the operation before choosing objects or styling. Useful visual actions
include:

- move, rotate, follow, or return;
- decompose, compose, accumulate, or cancel;
- project, align, map, or change reference;
- compare while holding controls constant;
- branch, merge, circulate, or close a loop;
- reveal an invariant across changing states;
- trace data or control through an architecture;
- refine an approximation across algorithm steps.

Show the operation through a path, aligned states, shared reference, trace, or
other observable relationship. Objects such as robots, cameras, tables,
servers, classes, and icons provide context; they are not the visual argument.
Reduce their contrast, detail, or size when they compete with the operation.

## 4. Derive Abstraction from Visible Action

Introduce a symbol only after the reader can see the relation or operation it
names. Use this sequence when the concept is unfamiliar:

1. show the objects, states, or data involved;
2. make the action or invariant visible through motion, attachment, alignment,
   enclosure, a path, or a state transition;
3. name that visible relation;
4. compress the named relation into notation or a formal expression.

Do not use a text label, relationship name, or icon as the only evidence that a
relation exists. For example, prove rigid attachment through a visible joint
and shared motion before adding a transform label; prove ownership through
containment or a stable connection before naming it; show changing values
before adding an iteration index.

When several cognitive stages are independently necessary, use progressive
panels. Each panel should add one new burden while preserving the geometry,
marks, and correspondence established earlier. Useful stages may include:

- identify the objects or states;
- observe one local operation;
- trace the composed operation;
- compress the trace into notation;
- compare an alternate path or verify an invariant.

Do not force a fixed panel count. Use as few panels as the reader needs, and do
not split a relationship that is already observable in one coherent view.

Place sample, time, pose, or iteration indices beside the state or operation
that varies. A remote note does not establish what the index modifies.

If the visual reading direction differs from the formal execution order, show
both explicitly. Trace one concrete input through the visible direction, then
show where formal evaluation begins. A warning sentence alone is insufficient.

### Freeze Accepted Teaching Structure Before Publication Refinement

After the visual claim, action, panel sequence, and controlled comparison pass
Human QA, record them as frozen for the refinement pass. Publication refinement
may improve notation, alignment, spacing, line craft, accessibility metadata,
and standalone export quality. It must not silently:

- add a new teaching question, concept, panel, legend, or explanatory paragraph;
- merge progressive stages into one denser figure;
- move established marks independently between progressive stages;
- revive information that Human QA deliberately moved into nearby Markdown.

If refinement exposes a teaching failure, reopen the visual-reasoning brief
explicitly instead of disguising a conceptual redesign as polish.

For progressive figures, reuse the exact canvas or `viewBox`, coordinates,
scale, and established marks. Each later stage should add only the marks named
in its difference list. Accept unused whitespace when cropping would make the
established geometry jump between stages.

## 5. Establish a Local Visual Grammar

Define each visual encoding once for a coherent visual set. Record a small
grammar table in the brief or package design notes:

| Meaning | Possible encoding |
|---|---|
| Current operation or primary relation | strongest solid line |
| Fixed supporting relation | thinner solid line |
| Projection, derived relation, or alternate path | dashed line with a direct label |
| Previous or alternate state | low-contrast ghost with the same geometry |
| Unknown quantity | one restrained accent plus an explicit `unknown` label |
| Context object | low-contrast outline or plane |

These are defaults, not universal meanings. Adapt the grammar to the subject,
but never reuse one color, line style, shape, or icon for incompatible meanings
within the same set.

Do not rely on color alone. Preserve distinctions through labels, line styles,
shapes, position, or enclosure when viewed in grayscale. Prefer direct labels
beside their referents. Add a compact legend only when the encodings cannot be
understood directly or when more than a few encodings recur.

Avoid decorative lock, anchor, cloud, database, or motion icons when spatial
attachment, enclosure, shared motion, or an explicit label can show the same
fact. An icon may reinforce evidence but must not replace it.

## 6. Build the Viewing Hierarchy

Plan four levels of attention:

1. the core relation or action;
2. its decisive values, states, or transformations;
3. the formal expression;
4. physical context and qualification.

Use contrast, size, line weight, whitespace, and placement to enforce that
order. Titles orient the reader but must not be more prominent than the visual
claim. Background objects must not dominate mathematical paths, state changes,
or comparison marks.

Give all marks a job. Remove empty cards, ornamental backgrounds, duplicated
summaries, realistic texture, and any object included only to fill space.

Export the figure itself on a white or transparent background when it should be
portable across Markdown, PDF, slides, or print. Review pages and Human QA
controls may surround it during development, but they are not part of the
delivered figure.

## 7. Map Formal Expressions to Visible Marks

Before rendering a formula, create a mapping table:

| Formula item | Meaning | Visible mark | State |
|---|---|---|---|
| item | plain-language role | exact path, region, state, or label | known, unknown, measured, fixed, or changing |

Every important symbol, factor, component, or algorithm state must have one
unambiguous referent in the visual. Match order as well as identity: a reader
should be able to trace a composed expression along the same sequence shown in
the diagram.

Use the same restrained encoding for a quantity in the path, formal expression,
and nearby explanation. Do not color every symbol. When color cannot be applied
consistently in the target Markdown renderer, use numbered or named
correspondence instead.

Use the renderer's supported math syntax in Markdown. In native SVG, `<tspan>`
may position ordinary non-mathematical labels, but it must not manually assemble
formal subscripts, superscripts, vectors, matrices, or equations. Do not
approximate technical notation with Unicode superscript glyphs, literal
underscores, or hand-positioned scripts. Do not introduce a formula-rendering
dependency solely for visual polish without separate approval and evidence that
the existing medium is insufficient.

When formal notation is part of the visual argument and hand-positioned SVG
text cannot preserve the required typography, use a real math renderer behind
this narrow internal interface:

```text
formal math source → standalone scalable SVG fragment
```

The caller supplies formal source and placement intent. The renderer owns glyph
selection, baselines, script sizing, operator spacing, and one usable SVG
fragment or an explicit failure. Keep renderer configuration, font paths,
serialization quirks, and dependency details behind this seam.

Apply domain typography semantically rather than cosmetically. When the
subject's convention supports it, distinguish named frames, mathematical
indices, vectors, matrices, and operators through proper math alphabets. Do not
copy one fixture's bold or upright choices into a domain with different
conventions.

When several rendered fragments are embedded in one SVG, give each render call
a unique semantic ID prefix and let the adapter namespace definitions and
internal references. Generated glyph IDs are not guaranteed to be unique across
fragments. The outer figure remains responsible for prefix uniqueness,
placement, `<title>`, `<desc>`, concise alternative text, and a nearby
accessible equivalent.

Treat a math renderer as an optional capability until its dependency lifecycle
is approved and complete-Skill regression proves it reliable. If unavailable:

- keep the formal expression in supported Markdown math when that preserves the
  teaching contract;
- choose another approved medium; or
- stop with an explicit missing-capability result.

Do not install a dependency implicitly, silently fall back to simulated
superscripts, or describe an unrendered fragment as completed.

`build-practical-guide` provides an optional internal adapter at
`../adapters/math-svg/` relative to this reference. Read its `README.md` before
use and run its capability probe before planning SVG math output. A missing
capability is an expected state, not permission to run `npm ci`; installation
still requires separate user authorization.

If an index represents samples, time, iterations, or states, show at least two
instances or explicitly define what the index identifies. Do not introduce an
indexed quantity into a single unexplained scene.

When an expression composes functions, matrices, transforms, or other
operations, distinguish:

- the order in which the reader traces the visual path;
- the order in which the formal operations act on the input.

Use an actual input symbol or value to connect the two orders. Preserve the
same operation labels in the path and expression so that the reversal or
composition is observable rather than merely asserted.

## 8. Distinguish State and Epistemic Role

When relevant, identify separately:

- fixed and known;
- fixed and unknown;
- changing by state, time, pose, or iteration;
- measured or observed per sample;
- derived or inferred.

Prefer evidence in the drawing: shared attachment, common motion, repeated
states, aligned panels, or a traced derivation. Add a compact table when these
roles cannot remain legible in the drawing. Never make a single accent mean
both `unknown` and `changing`.

## 9. Control Comparisons

Write an explicit difference list before drawing a comparison. Reuse the same
base geometry for everything not on that list:

- canvas and panel dimensions;
- viewpoint, scale, origin, and coordinate convention;
- object geometry and neutral state;
- label positions and typographic hierarchy;
- whitespace and alignment.

Change only the variables required by the teaching question. When a moving
state is necessary, use the same set of state ghosts or trajectories on both
sides. If unrelated changes remain, the comparison is confounded and must be
revised.

## 10. Select the Medium After the Argument

Choose the simplest medium that preserves the visual claim:

- **Mermaid:** topology, ownership, sequence, or a small flow where exact
  geometry and formula typography are not essential.
- **Native SVG:** exact spatial relationships, controlled states, formula-mark
  correspondence, responsive static diagrams, and accessible titles or
  descriptions.
- **HTML/CSS/canvas:** interaction or layout behavior that static Markdown
  cannot represent, when the target environment supports it.
- **Generated raster image:** physical appearance, texture, atmosphere, or
  visual analogy where geometric precision and editable notation are secondary.
- **Code-generated plot:** quantitative data, functions, distributions, or
  repeatable scientific plots when the environment and dependencies are known.

Do not force Mermaid to express measured geometry, or use a generated
illustration where exact coordinates and symbol correspondence are essential.
Prefer existing project tooling. Treat new dependencies, browser automation, or
installation as separately authorized actions.

## 11. Integrate the Visual with Markdown

Place the visual immediately after the first passage that requires it. Use:

- concise alternative text that states the visual's teaching function;
- an internal SVG `<title>` and `<desc>` when SVG is used;
- a nearby long description that preserves the steps, values, invariants, and
  conclusion needed to complete the same reasoning without the image.

Do not use the filename as alternative text. Do not make the long description
depend on color alone. Avoid duplicating every visible label; describe the
argument and conclusion.

## 12. Validate in Layers

### Structural and Technical Checks

Confirm:

- the selected medium renders in the target Markdown environment;
- SVG or HTML is structurally valid;
- links and asset paths resolve;
- text, arrows, and labels are not clipped or overlapping;
- notation matches the guide;
- the visual remains readable at its actual embedded size;
- grayscale retains every essential distinction;
- short and long descriptions are available.

For progressive figures, also compare their canvases and established geometry
programmatically when possible. A visual resemblance is not enough evidence
that points, paths, scales, and anchors remain fixed.

For rendered math fragments, also confirm:

- formal source regenerates deterministically in the pinned environment;
- every output contains exactly one scalable SVG root;
- scripts, baselines, factor grouping, and symbol roles remain legible at the
  actual embedded size;
- combined figures do not contain colliding definition IDs;
- failure does not produce a plausible-looking substitute.

For native SVG visuals, run
`scripts/check_instructional_visuals.py <guide-or-package-root>`. This checks
parseability, structural accessibility metadata, referenced SVG paths, and
simulated Unicode superscript notation. It does not judge visual reasoning,
layout, or teaching success.

These checks prove artifact integrity, not teaching effectiveness.

### Visual-Argument Audit

Answer concretely for every visual:

1. What mark will receive the first fixation, and why?
2. What mark was intended to receive it?
3. Are those the same?
4. What is the single visual protagonist?
5. Which specific objects, lines, labels, or regions compete with it?
6. Does the image expose a process or only label an answer?
7. Can the formal expression be read along visible marks in the same order?
8. Which elements can be removed or reduced in contrast?
9. Which relation needs stronger visual exaggeration?
10. If only five visual elements survived, which five preserve the claim?

Record failures as exact changes, such as `move the path label beside the
segment`, not judgments such as `make it clearer` or `make it professional`.

### Target-Reader Human QA

Do not tell the reader the intended insight first. Show the rendered visual at
its real Markdown size, initially without nearby prose, and ask:

- What do you think this diagram is explaining?
- What changed, and what stayed fixed?
- Where would you begin, and in what order would you follow it?
- Point to the visual counterpart of each important formula item.
- What does any index, ghost, dashed line, or accent mean?
- Which relation could you identify before reading its symbol?
- If the path direction and operation order differ, demonstrate both.

Record the reader's route and words. A short viewing window can test initial
orientation, but do not claim a universal five- or ten-second threshold. Revise
the brief, visual structure, or description according to the observed failure.

## 13. Completion Gate

A teaching visual is ready only when:

- its one-sentence insight matches the visual claim;
- every panel supports that claim;
- the primary action dominates its context;
- invariants and changes are visible;
- important symbols name relations already made visible;
- important formal items map to marks in the correct order;
- comparison variables are controlled;
- the artifact passes structural and embedded-size checks;
- accessibility descriptions preserve the reasoning;
- Human QA is either passed or explicitly recorded as pending.

Do not call an image verified merely because it is attractive, stylistically
consistent, generated successfully, or free from rendering errors.
