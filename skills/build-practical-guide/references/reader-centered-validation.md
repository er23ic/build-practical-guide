# Reader-Centered Validation

Use this workflow for every output mode. Scale its depth to the size and risk of
the requested guide, but do not omit a layer merely because the user did not ask
for validation explicitly.

## Build a Concrete Reader Model

Record only attributes that can change a teaching or validation decision:

- **Goal:** What the reader needs to accomplish.
- **Prior knowledge:** Relevant concepts, tools, and terminology the reader
  already understands or does not yet understand.
- **Use context:** Relevant device, environment, available tools, time, and
  conditions in which the reader will use the guide.
- **Constraints:** Relevant access, permission, budget, physical,
  accessibility, or cognitive constraints.
- **Risk perception:** What the reader fears doing incorrectly and the
  consequences they need help avoiding.
- **Success criteria:** What the reader must be able to observe or demonstrate
  to know the outcome is complete.

For each attribute, distinguish source-supported information from a
**provisional assumption**. Do not invent demographic details or fictional
biography to make the model feel specific.

Infer a provisional model from the task and available sources when that is
enough to proceed safely. Ask a focused question only when materially different
answers would change the guide's structure, safety, terminology depth, or
learning outcome. Otherwise continue and disclose the assumption.

Keep the guide itself concise. State only who the guide is for, what relevant
knowledge or prerequisites it assumes, and what the reader should be able to do
when finished. Put the fuller reader model in the delivery summary or approved
package evidence area.

## Run Four Validation Layers

Validate the completed draft in this order. Keep the layers distinguishable in
the delivery summary even when one finding affects more than one layer.

### 1. Evidence Validation

Check important claims, commands, versions, expected results, and source
attributions against the available evidence. Use the provenance and assessment
statuses in [content-verification.md](content-verification.md). Do not turn an
assumption, plausible inference, or unperformed action into a verified result.

### 2. Logic Validation

Check whether:

- stated premises support the conclusions;
- causal direction is justified;
- definitions and assumptions remain consistent;
- procedural and explanatory dependencies are ordered correctly;
- necessary intermediate reasoning is present;
- sections or conclusions contradict one another; and
- the final outcome still answers the original goal.

Factual sentences can form an invalid argument. Treat logical coherence as a
separate result from source accuracy.

### 3. Practical Walkthrough

Walk through the procedure as the modeled reader without claiming to execute
anything that was not executed. For each consequential step, check whether the
reader can:

- identify the next action;
- understand the necessary terms and prerequisites;
- perform the action with the stated tools and permissions;
- observe progress and the expected result;
- distinguish success from failure; and
- use a safe diagnostic or recovery path when the result differs.

Label environment-dependent behavior as unverified when the required execution
or evidence is unavailable.

### 4. Reader Walkthrough

Review the draft against every relevant reader-model attribute. Check for
hidden prerequisites, unexplained terminology, excessive cognitive load,
irrelevant detail, inaccessible presentation, avoidable anxiety, unsafe
defaults, and a learning sequence that does not support the reader's goal.

This is a simulated evaluation based on an explicit model. Never describe it as
Human QA, usability research, representative-user testing, or empirical
evidence.

## Correct and Revalidate

Correct a local defect when the evidence supports the correction and it does not
change the user's established intent, scope, conclusion, or authorization
boundary. After editing, rerun every validation layer the change could affect.
Report the corrected draft's current result; do not retain a stale pass from an
earlier version.

If a safe correction needs evidence, execution, access, or a user decision that
is unavailable, keep the supported portion and report the affected result as
unverified or decision needed. Do not invent a repair merely to make every
layer pass.

## Handle Consequential Decisions

Before applying a correction, determine whether it would change an established
core conclusion, scope boundary, teaching direction, authorial position, or
authorization boundary. Treat that as a consequential decision, not a local
defect. Do not silently choose on the user's behalf even when one choice appears
safer or easier to teach.

Complete and validate content that does not depend on the decision. Mark every
dependent claim, step, and conclusion as pending, and ensure no candidate option
is written as an established fact.

Present two to four feasible, meaningfully distinct options. Do not pad the list
with cosmetic variants. For every option state:

- **Change:** What would be different in the guide.
- **Benefits:** What the option improves or preserves.
- **Costs:** What it gives up, delays, complicates, or leaves unresolved.
- **Reader impact:** How it changes safety, comprehension, effort, confidence,
  or the ability to reach the reader's success criteria.
- **Evidence or validation needed:** What would support or test the option.

Recommend one option and give a concise reason grounded in the reader model,
available evidence, and risk. Explicitly leave the final choice to the user.
If no option can be recommended from the available evidence, say so and explain
what evidence would make a recommendation possible.

After the user chooses, update the affected content and rerun every validation
layer the decision can change. Until then, report those layers as `Decision
needed`, `Unverified`, or `Partially passed` as appropriate.

## Escalate Repeated Correction Failure

Track correction attempts within the current guide task. If the same category
of defect remains after two local correction attempts, stop making another
word-level or step-level replacement. Reassess the relevant reader-model
assumption, evidence base, terminology owner or glossary, section boundaries,
or overall guide structure.

Then either apply a supported structural correction and rerun affected layers,
or report the exact blocker and what input, evidence, access, or decision would
resolve it. Do not lower the validation standard, loop indefinitely, or claim a
pass because repeated edits changed the wording.

## Scale Validation to Scope and Risk

Use the smallest tier that matches both the deliverable and its consequences.
When scope and risk point to different tiers, use the higher one.

| Tier | Typical output | Minimum validation depth |
|---|---|---|
| **Low-risk draft** | Chat draft, proposal, or explanatory outline | Provisional reader model, static four-layer validation, explicit evidence and execution limits. |
| **Formal unit or reference** | Named standalone learning unit or explicitly requested reference intended for reuse | Complete reader model and validation summary, source and command checks, full practical walkthrough when procedural, persistent-change recovery, and preservation of the summary with the document. |
| **Substantial learning path** | Multiple modules, prerequisite relationships, reading routes, high cognitive load, or continued growth | Formal-guide checks plus complete-tree validation of prerequisite edges, routes, terminology, canonical concept ownership, worked cases or approved learner prompts, evidence labels, and cross-module conclusions; representative Human QA is a separate required or pending activity. |
| **High-stakes guidance** | Medical, legal, financial, security, destructive, safety-critical, or similarly consequential decisions or procedures | All applicable package or guide checks plus relevant primary evidence, independent execution or calculation checks where safe and authorized, representative-user evidence, appropriate domain-expert review, and real-world validation proportionate to the consequence. |

A deliverable can be useful before every higher-tier activity occurs, but report
the missing activity as `Unverified` or `Decision needed`. Do not call
high-stakes guidance fully validated merely because its prose, links, files, or
simulated reader walkthrough passed.

For a learning path, integrate the four validation layers with the existing
specialist workflows instead of replacing them:

- validate prerequisite edges, reading routes, terminology, canonical concept
  ownership, and cross-module conclusions using
  [learning-package-structure.md](learning-package-structure.md);
- use [math-teaching.md](math-teaching.md) for mathematical prerequisites,
  worked relationships, notation, and target-renderer constraints;
- use [instructional-visuals.md](instructional-visuals.md) for visual argument,
  accessibility, rendering, and target-reader Human QA;
- use [research-sources.md](research-sources.md) and
  [content-verification.md](content-verification.md) for source roles,
  provenance, and claim status; and
- use [maintaining-learning-packages.md](maintaining-learning-packages.md) when
  validation changes an existing package's structure or canonical owners.

Rerun every affected specialist check after the reader model, prerequisite
graph, route, concept owner, mathematical explanation, visual, source, or
package structure changes. Keep their evidence types distinct; for example, a
rendered graph is not evidence that a reader understands it, and Human QA is not
evidence that a formula is correct.

## Incorporate Human QA

Record who participated, how they relate to the intended reader model, which
tasks or content they encountered, what was observed or reported, and the
session's limits. One participant can reveal a problem but does not establish
that every representative reader will succeed.

Human QA is empirical reader evidence. A reader walkthrough is only a simulated
inspection. Label them separately from representative-user coverage, source
verification, execution or calculation evidence, accessibility checks, and
domain-expert review.

For a substantial package or high-stakes deliverable, include an evidence-
activity matrix in the delivery summary. Report each activity separately as
`Passed`, `Partially passed`, `Unverified`, or `Decision needed`, with its
observed scope:

- simulated reader walkthrough;
- actual Human QA;
- representative-user coverage;
- source verification;
- execution or calculation checking;
- accessibility and rendering checks when applicable;
- domain-expert review; and
- real-world validation when applicable.

Do not merge activities into a generic `reviewed` or `validated` label. Evidence
from one activity cannot silently satisfy another. The status describes whether
the activity's relevant planned scope is supported, not whether the deliverable
as a whole passed. In the finding column, state whether the activity occurred,
what it covered, what it found, and what remains pending.

When Human QA contradicts a reader-model attribute:

1. Mark the prior attribute as contradicted; do not preserve it as a convenient
   assumption.
2. Update the model using the observed evidence, while avoiding broader claims
   than the participant and task support.
3. Identify every explanation, prerequisite edge, reading route, example,
   worked case, optional learner prompt, visual, success criterion, and
   validation result that depended on
   the old attribute.
4. Correct or mark those items pending, then rerun all affected validation and
   specialist checks.
5. Record the revised evidence state and any additional representative Human QA
   still needed.

For important, high-cognitive-load, or substantial learning paths, treat
representative Human QA as a distinct validation activity rather than an
optional synonym for self-review. For high-stakes content, also require the
appropriate domain and real-world evidence; neither Human QA nor expert review
substitutes for the other.

## Report the Result

Use these statuses for the four validation layers and material findings:

- **Passed:** The relevant checks found no unresolved issue within the stated
  evidence and execution boundary.
- **Partially passed:** A supported portion passed, but a bounded issue or
  limitation remains.
- **Unverified:** Required evidence, execution, environment access, or Human QA
  was not available.
- **Decision needed:** The user must choose or supply information before the
  affected content can be completed safely.

Do not compute an aggregate score. A score can hide a critical unverified item
and implies a precision the workflow does not establish.

Every delivery, including a low-risk chat draft, must end with an observable
reader model and validation summary. Use this minimum shape, adapting labels to
the guide's language:

```markdown
## Reader and validation summary

### Reader model

| Attribute | Current model | Basis |
|---|---|---|
| Goal | ... | Source-supported / Provisional assumption |
| Prior knowledge | ... | Source-supported / Provisional assumption |
| Use context | ... | Source-supported / Provisional assumption |
| Constraints | ... | Source-supported / Provisional assumption |
| Risk perception | ... | Source-supported / Provisional assumption |
| Success criteria | ... | Source-supported / Provisional assumption |

### Validation

| Layer | Status | Finding |
|---|---|---|
| Evidence | Passed / Partially passed / Unverified / Decision needed | ... |
| Logic | Passed / Partially passed / Unverified / Decision needed | ... |
| Practical | Passed / Partially passed / Unverified / Decision needed | ... |
| Reader | Passed / Partially passed / Unverified / Decision needed | ... |
```

Every reader-model basis cell must contain exactly one classification:
**Source-supported** or **Provisional assumption**. Do not combine them with a
slash, conjunction, qualifier, or third category. When one field contains mixed
provenance, split its content into separate statements or keep only the part
that supports the current teaching decision. Put missing information in the
modeled value and validation finding rather than inventing another provenance
category.

After any correction, add a concise correction-and-revalidation note naming the
problem, the correction, and the layers rerun. If no correction was made, say
so. Also state whether execution and Human QA occurred. Never collapse the four
rows into one overall status.

For a low-risk chat draft, keep the table entries compact and use static
validation. For a formal document, preserve the complete summary with the
delivery. Never expose private chain-of-thought; report findings, corrections,
evidence, and remaining boundaries instead.
