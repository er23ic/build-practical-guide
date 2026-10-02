# Learning Path Structure

Use this reference only after the package root and file plan are approved.
Create exactly the approved artifacts and keep every artifact within its stated
teaching role. The primary route is a continuous self-study narrative. A
hierarchical directory tree supports navigation; a separate knowledge map and
cross-links represent prerequisite relationships that cross directory
branches.

## Assign Content Ownership

Before drafting, assign one canonical owner to each shared concept, definition,
mental model, warning, worked example or case, and source record.

Other artifacts may give the minimum context needed to follow a sentence, then
link to the owner. Do not copy the same explanatory paragraph, table, or
checklist into the entry page, map, modules, glossary, and other artifacts.

Prefer these ownership roles:

| Artifact | Owns |
|---|---|
| Entry page | Audience, outcome, prerequisites, scope, main route, directory map, and navigation |
| Learning map | Concept nodes, prerequisite and related-concept edges, and the package-level mental model |
| Core module | One connected outcome, its narrative sequence, complete explanation, evidence, and worked cases |
| Deep dive | Optional depth that would interrupt the main route while remaining in the approved scope |
| Troubleshooting | Observable symptoms, safe checks, and evidence-supported resolutions when relevant |
| Glossary or index | Lookup aid linking terms to their canonical teaching location |
| Sources | Source roles, claim status, verification evidence, unknowns, and limitations |

Worked examples, derivations, and cases usually belong with the concept they
teach. Do not create a mandatory exercise or practice artifact by default. If
an approved artifact adds no teaching value after inventory, do not silently
omit or replace it. Explain the conflict and ask whether to revise the approved
plan.

## Entry Page

Help the learner follow the main route or locate a specific topic without
teaching every concept again. Include:

- Who the package is for
- Observable learning outcome
- Prerequisites and environment assumptions
- Core scope and material exclusions
- One recommended linear route through the core modules
- Optional branches and lookup entry points when they serve a distinct need
- A readable directory tree showing every approved artifact and its role
- Links to the learning map, modules, glossary or index, and sources as useful

Avoid placing a second concept map, full glossary, repeated safety checklist, or
chapter-by-chapter summary on the entry page.

Show the approved directory hierarchy as a readable tree when there are
multiple files. For example:

```text
<learning-path>/
├── README.md                 # entry point and recommended route
├── knowledge-map.md          # prerequisite and related-concept links
├── modules/
│   ├── 01-foundations.md
│   └── 02-central-method.md
└── references/
    ├── glossary.md
    └── sources.md
```

This is an illustration, not a required template. Include only approved files
that serve a distinct teaching or navigation purpose. Every file must be
reachable from the entry point and have a clear role.

## Learning Map

Represent relationships the directory tree cannot show:

- Prerequisite edges
- Related concepts
- Shared dependencies
- The main linear route and optional branches

Use compact text, a table, or Mermaid according to the relationships. Link each
node to its canonical module. The map may define the package-level mental
model, but detailed teaching remains in the owning module. Make every artifact
reachable from the entry page and avoid orphan files.

## Modules

Give each core module one connected learning outcome. At its start or end,
link the relevant prerequisites, previous or next point in the main route,
related concepts, and optional depth.

Within a module:

- Introduce its unfamiliar terms in plain language.
- Follow the agreed narrative and reasoning sequence; include all depth needed
  by the approved scope.
- Use worked examples, derivations, or cases to show how claims and methods
  operate, including intermediate reasoning.
- Link to a shared concept's owner instead of re-teaching it.
- Keep optional depth in a linked branch when it would interrupt the core route;
  do not omit it if it belongs to the approved scope.
- End naturally when the outcome is complete.

Do not mechanically add boilerplate questions or repetitive summaries to every
module. Use a concise synthesis and transition when the next relationship
matters.

## Optional Learner Prompts

Do not add mandatory problem sets by default. When a brief reflection prompt or
learner check materially helps understanding, keep it optional and give the
reader enough explanation or a worked case to continue independently. Do not
make completion of exercises a prerequisite for following the main route.

If the user explicitly approves exercises, connect them to the learning
outcome, provide solutions or evaluation criteria where possible, and do not
duplicate questions across modules without a teaching reason.

## Optional Artifacts

Create deep dives, optional prompts, troubleshooting, glossary, or source files only
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
5. Confirm every module has one connected outcome and follows the approved
   linear route.
6. Confirm the directory hierarchy is readable, every file is reachable, and
   cross-links represent dependencies that the tree cannot show.
7. Search for repeated definitions, explanations, warnings, exercises, and
  source claims; keep one canonical owner unless repetition is necessary for
  safety or local comprehension.
8. Check terminology and symbols across modules.
9. Confirm evidence labels and limitations match the source inventory.
10. Confirm optional artifacts contain distinct teaching value.
11. Confirm module endings are natural and not copied from a template.

Report what was actually checked. Do not claim link, command, or content
validation that was not performed.
