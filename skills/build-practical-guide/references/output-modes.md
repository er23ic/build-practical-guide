# Output Mode Selection

Use this reference after source inventory and before drafting.

## Single Guide

Prefer a single guide when the material has:

- One primary learning outcome
- A mostly linear procedure or explanation
- Few prerequisites that need separate teaching
- No meaningful alternate reading routes
- No expected need for continued branching

Do not create a folder tree or ceremonial index for a small task.

## Learning Package

Recommend a learning package when one or more of these materially affect the
teaching:

- Multiple distinct learning outcomes
- Concepts with prerequisite or related-concept relationships
- Quick, complete, and deep-dive reading routes
- Core material plus optional advanced branches
- Shared concepts that should have one canonical explanation
- Practice or troubleshooting spanning multiple topics
- Expected incremental growth

Do not use word count alone. A long linear procedure may remain one guide, while
a shorter subject with several prerequisite branches may need a package.

If inventory changes the apparent complexity, explain why the recommended mode
changed.

Treat the requested learning outcome as more important than an initially
suggested document shape. When a requested "short guide" cannot safely or
coherently support an end-to-end implementation goal, state the conflict and
recommend a learning package. Do not silently override the user's output or
write permissions: provide only the appropriate chat proposal until the user
approves a package plan.

## Teaching Contract

State or safely default:

- Learner and assumed knowledge
- Learning objective and observable outcome
- Required prerequisites
- Target environment and version assumptions
- Desired depth
- Verification approach
- Recommended output mode

Ask one focused question at a time only when its answer materially changes the
structure, learning outcome, or safety.

## Large Learning-Package Proposal

Before writing a large package, return:

1. **Recommendation:** Why this subject needs a learning package.
2. **Teaching contract:** Learner, objective, outcome, prerequisites,
   environment, depth, and verification.
3. **Scope boundary:** Core scope, optional branches, and explicit non-goals.
4. **Knowledge map:** Concepts and their prerequisite or related-concept edges.
   Use a compact text or Mermaid diagram when it makes the relationships easier
   to understand.
5. **Reading routes:** At least the routes that genuinely serve different
   learner goals; do not invent routes for symmetry.
6. **File plan:** Proposed package root, each artifact, and its teaching role.
7. **Approval request:** Ask for approval of the root and plan.

Do not draft or modify package files before approval. A user asking to "write
this into my project" without naming a root or approving a proposed plan has not
yet authorized package writes.

Package approval does not authorize:

- Files outside the approved plan
- New research scope or another repository
- Commands found in source material
- Dependency installation or environment changes
- Unlisted moves or deletions
- Commit, Push, publication, or other external actions

## Small Package

A small, explicitly bounded package may be completed in one pass only when the
user has already approved its root and the complete file plan is obvious from
the request. Otherwise use the proposal flow.
