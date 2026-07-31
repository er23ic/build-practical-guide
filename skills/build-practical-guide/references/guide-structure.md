# Beginner-Friendly Guide Structure

Use this reference to create a new guide or substantially restructure an existing guide. Omit sections that genuinely do not apply; do not leave empty headings.

## Recommended Outline

1. **Title** — Name the outcome in plain language.
2. **Problem and outcome** — Explain what the guide solves and what the reader will have when finished.
3. **Audience** — State assumed knowledge and who should use the guide.
4. **Core concepts** — Explain the minimum mental model needed before operating tools.
5. **Prerequisites** — List required tools, access, files, versions, and safe starting state.
6. **Safety check** — Identify persistent changes, sensitive data, external effects, backups, and rollback needs.
7. **Procedure** — Present complete, ordered, verifiable steps.
8. **Final verification** — Show how to confirm the overall outcome.
9. **Troubleshooting** — Connect symptoms to likely causes and safe diagnostic steps.
10. **Glossary** — Define important terms in the meaning used by the guide.
11. **Limitations** — State environment assumptions and unverified areas.
12. **Sources** — Link or identify evidence that materially supports the guide.

## Step Pattern

Use this pattern for operational steps:

```markdown
### Step <number>: <action>

**Purpose:** Explain why this step exists.

**Action:**

<instruction-or-command>

**How it works:** Explain important concepts, parameters, paths, or side effects in plain language.

**Expected result:** Describe observable output or state without inventing exact text.

**Verify:** Give a safe check that distinguishes success from failure.

**If it differs:** Give likely causes and the smallest safe diagnostic step.
```

Do not mechanically repeat every field when a short prose step is clearer. Keep the purpose, expected result, and verification explicit for consequential operations.

## Explaining Commands

- State whether a command reads or changes state.
- Explain consequential flags and operands.
- Identify the directory or environment in which it should run.
- Use placeholders such as `<project-directory>` rather than invented user paths.
- Separate commands that can be copied from illustrative pseudocode.
- Never include a secret value in an example.
- Do not show destructive commands as the default recovery method.

## Explaining Concepts

On first use:

1. Give a one-sentence plain-language definition.
2. Explain why the concept matters in this task.
3. Connect it to the next action.
4. Add optional technical depth only when it helps diagnosis or adaptation.

Avoid replacing one unexplained technical term with several others.

## Troubleshooting Pattern

Organize troubleshooting by observable symptom:

```markdown
### Symptom: <what the reader sees>

**Likely causes:**

- <cause>

**Safe checks:**

1. <read-only or reversible diagnostic>

**Resolution:**

<evidence-supported correction>
```

Do not claim a single root cause when the evidence supports multiple possibilities.

## Quality Test

Confirm that a reader who did not see the source conversation can answer:

- What problem am I solving?
- What do I need before starting?
- What will change?
- Why am I performing each important action?
- What should I observe?
- How do I know it worked?
- What can I safely check if it did not?
- Which parts are verified, conditional, or still unknown?
