# Maintaining Learning Packages

Use this reference when adding material to an existing learning package or
reorganizing overlapping learning documents. An update and a restructure are
different operations: an update changes teaching content within the current
shape, while a restructure changes file ownership, paths, or navigation.

## Inventory Before Proposing Changes

Read only the package and task-related sources within the approved boundary.
Record:

- The entry page, learning map, advertised reading routes, and package root
- Each artifact's current purpose and primary learning outcome
- Canonical owners for shared concepts, definitions, warnings, exercises, and
  source records
- Prerequisite and related-concept edges
- Terminology and glossary entries
- Source-ledger records and known evidence limitations
- Internal links and any paths known or reasonably likely to be referenced
  outside the package
- New material's provenance, assessment, and intended learning outcome

Compare the new material with both the knowledge map and source inventory before
choosing a destination. Do not infer that a new source requires a new module.

## Choose the Smallest Coherent Update

Extend an existing artifact when it already owns the concept and the new
material supports the same primary learning outcome. Update only the affected
explanation, example, evidence label, source record, relationship, or route.

Propose a new module or deep-dive branch only when the material has a distinct
learning outcome or adds a relationship that cannot be taught coherently by the
current owner. State:

- The proposed artifact and its one primary outcome
- Its prerequisites and related concepts
- Why the current owner is insufficient
- Which reading routes, map edges, terminology, and source records would change

If the material merely clarifies, corrects, or verifies existing teaching, keep
it with the current owner. Repeated execution must recognize headings,
definitions, glossary terms, warnings, citations, routes, and source records
that are already correct rather than appending another copy.

## Keep Navigation and Evidence Aligned

After an incremental change, inspect every navigation or evidence surface that
the change can make stale:

- Entry-page scope and reading routes
- Knowledge-map nodes and edges
- Module prerequisite, related-concept, and next-step links
- Glossary terminology and avoided synonyms
- Practice or troubleshooting that depends on the changed behavior
- Source-ledger claims, provenance, assessment, version, and limitations

Change a surface only when its statement or route is no longer accurate. Do not
rewrite unaffected files merely for stylistic consistency.

## Classify Documents Before Restructuring

Give every affected document exactly one proposed disposition:

| Disposition | Use when |
|---|---|
| Retain | Its purpose and canonical ownership remain distinct and correct |
| Merge | Useful content belongs in another canonical owner |
| Replace with index | The old path remains useful as concise navigation or migration help |
| Outdated | Its claims or route are superseded and preserving the body would mislead |
| Unresolved | Ownership, evidence, external references, or preservation is not yet clear |

Before any move, rewrite, or deletion, present a migration table with:

| Current path | Current purpose | Disposition | Target path | Content or links to preserve | Reason |
|---|---|---|---|---|---|

Also list the exact files to create, edit, move, replace with an index, and
delete. Identify unresolved documents separately. A broad request to clean up,
deduplicate, reorganize, or approve a package root does not authorize unlisted
moves or deletions.

## Approval and Recovery Gate

Do not move or delete files until the user explicitly approves the exact
migration plan and deletion list. Approval to draft an inventory or proposal is
not migration approval.

Before an approved deletion:

1. Confirm the useful content has a named destination or is intentionally
   obsolete.
2. Update inbound internal references and advertised reading routes.
3. Confirm Git or another user-approved mechanism contains a recoverable
   earlier state. An uncommitted file or ignored file is not recoverable merely
   because the package is inside a Git repository.
4. Keep a concise page at the old path when external references are plausible
   and redirect-like navigation has meaningful value.
5. Stop rather than delete when preservation, reference impact, or recovery
   remains unresolved.

Do not Commit, Push, publish, or create a recovery commit unless the user
separately authorizes that action.

## Apply an Approved Migration

Implement only the approved table:

1. Create or extend canonical targets and preserve attributed useful content.
2. Update the map, routes, prerequisites, terminology, source records, and
   internal references affected by the new ownership.
3. Add approved compatibility indexes.
4. Re-inventory the affected content before deleting an approved source.
5. Delete only the explicitly approved files whose recovery gate passed.

If evidence discovered during migration changes a disposition or target, pause
that part and propose a revised table. Do not silently improvise a new path.

## Validate the Result

In addition to whole-package validation in
[learning-package-structure.md](learning-package-structure.md), check:

1. Every migration-table row matches the resulting path and disposition.
2. Each retained useful claim, example, warning, exercise, and source
   attribution is present at its named target.
3. All internal links and advertised reading routes resolve from their actual
   files.
4. Knowledge-map and prerequisite edges describe the resulting ownership.
5. Compatibility indexes point to live canonical destinations without
   duplicating the migrated lesson.
6. Source provenance, assessment, version, and limitations remain attached to
   the claims they support.
7. No unjustified duplicate headings, definitions, warnings, glossary entries,
   citations, modules, or routes were introduced.
8. Repeating the same approved update would produce no additional content or
   structural change.
9. Deleted paths were explicitly approved and had a confirmed recovery route.

Report the checks actually performed, deletion and recovery evidence, unresolved
external references, and anything that remains unverified.
