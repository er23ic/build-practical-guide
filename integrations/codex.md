# Codex integration

## Install

Copy the Skill folder into the user-level Codex skills directory:

```bash
cp -R skills/build-practical-guide ~/.codex/skills/
```

Open a new Codex session after installation. The installed folder must contain
`SKILL.md` directly at:

```text
~/.codex/skills/build-practical-guide/SKILL.md
```

## Invoke

Explicit invocation:

```text
Use $build-practical-guide to turn these project notes into a verified
beginner-friendly Markdown guide.
```

Codex may also select the Skill automatically when the request matches the
description in `SKILL.md`.

## Optional math SVG adapter

The Skill works without the adapter. Install its pinned dependency only when
formal SVG math is required and dependency installation is authorized:

```bash
cd ~/.codex/skills/build-practical-guide/adapters/math-svg
npm ci
npm run capability
```

The capability command exits with status `0` when available and `3` when the
optional renderer is unavailable.
