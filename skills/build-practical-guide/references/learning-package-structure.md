# Learning Package Structure

Use this reference only after the package root and file plan are approved.
Create exactly the approved artifacts and keep every artifact within its stated
teaching role.

## Assign Content Ownership

Before drafting, assign one canonical owner to each shared concept, definition,
mental model, warning, exercise, and source record.

Other artifacts may give the minimum context needed to follow a sentence, then
link to the owner. Do not copy the same explanatory paragraph, table, or
checklist into the entry page, map, modules, glossary, and practice.

Prefer these ownership roles:

| Artifact | Owns |
|---|---|
| Entry page | Audience, outcome, prerequisites, scope, reading routes, and navigation |
| Learning map | Concept nodes, prerequisite and related-concept edges, and the package-level mental model |
| Core module | One primary learning outcome and the explanation unique to that outcome |
| Deep dive | Optional depth that would interrupt the core route |
| Practice | Integrated application and milestone-level understanding checks |
| Troubleshooting | Observable symptoms, safe checks, and evidence-supported resolutions |
| Glossary | Short lookup definitions, not a second tutorial |
| Sources | Source roles, claim status, verification evidence, unknowns, and limitations |

If an approved artifact adds no teaching value after inventory, do not silently
omit or replace it. Explain the conflict and ask whether to revise the approved
plan.

## Entry Page

Help the learner choose a route without teaching every concept again. Include:

- Who the package is for
- Observable learning outcome
- Prerequisites and environment assumptions
- Core scope and material exclusions
- Only the reading routes that serve distinct goals
- Links to the learning map, modules, practice, glossary, and sources as useful

Avoid placing a second concept map, full glossary, repeated safety checklist, or
chapter-by-chapter summary on the entry page.

## Learning Map

Represent relationships a folder tree cannot show:

- Prerequisite edges
- Related concepts
- Shared dependencies
- Core route and optional branches

Use compact text, a table, or Mermaid according to the relationships. Link each
node to its canonical module when practical. The map may define the minimum
package-level mental model, but detailed teaching remains in the owning module.

## Modules

Give each core module one primary learning outcome. At its start or end, link
only the prerequisites, related concepts, and next step that are genuinely
useful.

Within a module:

- Introduce its unfamiliar terms in plain language.
- Move from intuition to example and formal detail only as the subject needs.
- Link to a shared concept's owner instead of re-teaching it.
- Keep optional theory in a deep dive when it would block the core route.
- End naturally when the outcome is complete.

Do not mechanically add `Learning objectives`, `Key takeaways`, `What you
learned`, or question lists to every module. Use a concise transition when the
next relationship matters.

## Practice and Understanding Checks

Concentrate practice at meaningful milestones. An integrated exercise should
connect multiple modules and state:

- What the learner will attempt
- Required safe starting conditions
- Observable evidence
- What remains an expected rather than verified result
- Where to return when an observation differs

Use questions only when answering them is itself useful practice. Do not repeat
shallow chapter checks and then repeat them again in an integrated exercise.

## Optional Artifacts

Create deep dives, practice, troubleshooting, glossary, or source files only
when the approved plan includes them and source inventory shows they add value.
Do not create empty headings or ceremonial files to complete a template.

When an approved optional artifact is unnecessary, propose a plan adjustment
instead of filling it with repeated content.

## Package Validation

Validate the package as one navigable artifact:

1. Confirm the file tree matches the approved plan exactly.
2. Resolve every relative Markdown link and heading anchor.
3. Walk each advertised reading route from the entry page.
4. Confirm prerequisite edges point in a learnable order.
5. Confirm every module has one primary outcome.
6. Search for repeated definitions, explanations, warnings, exercises, and
   source claims; keep one canonical owner unless repetition is necessary for
   safety or local comprehension.
7. Check terminology and symbols across modules.
8. Confirm evidence labels and limitations match the source inventory.
9. Confirm optional artifacts contain distinct teaching value.
10. Confirm module endings are natural and not copied from a template.

Report what was actually checked. Do not claim link, command, or content
validation that was not performed.
