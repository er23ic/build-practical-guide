# Generic AI integration

This repository's canonical behavior lives in
`skills/build-practical-guide/`. Do not maintain a second rewritten prompt for
another AI tool.

## Manual loading

For an AI tool that can read local files:

1. Provide `skills/build-practical-guide/SKILL.md` as the task instruction.
2. Let the model read only the reference files that `SKILL.md` identifies for
   the current task.
3. Make `scripts/` available when the tool can execute local commands.
4. Keep the optional `adapters/math-svg/` capability disabled unless its
   dependency is explicitly installed.
5. Give the model the source material, exact output destination, and applicable
   project instructions.

Suggested request:

```text
Follow the workflow in skills/build-practical-guide/SKILL.md. Read only the
referenced files needed for this task. Turn the supplied material into a
verified beginner-friendly Markdown guide, and report unsupported claims or
missing evidence instead of inventing them.
```

## Compatibility boundary

This manual integration is experimental. A tool must be able to preserve the
Skill's staged workflow, read referenced files, and respect authorization
boundaries. Tools without file access can receive pasted excerpts, but
progressive disclosure and script-based validation will be weaker.

Platform-specific compatibility should be claimed only after testing that
platform. The Codex metadata file `agents/openai.yaml` may be ignored by tools
that do not understand it; `SKILL.md` remains the canonical instruction.
