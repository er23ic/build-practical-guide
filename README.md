# Build Practical Guide

[繁體中文](#繁體中文) · [English](#english)

## 繁體中文

`build-practical-guide` 是一個 AI Agent Skill，用來把對話、研究、工作筆記、
專案證據與其他適用來源，整理成完整、以證據為基礎的自學教材。它會依
讀者需求設計連貫的學習敘事、知識地圖、完整解說與可導覽的單元或模組路徑；
只有在使用者明確要求時，才改用速查指南。

它特別重視：

- 區分已驗證事實、合理推論與未知資訊；
- 先建立具體讀者模型，再從證據、邏輯、實作與讀者四個層次自我驗證；
- 依風險調整驗證深度，並在重要決策中提供 2–4 個具成本、效益與
  讀者影響說明的選項；
- 從具體例子建立數學與技術概念；
- 以教學推理結構設計技術插圖；
- 維護既有教材時保留授權、證據與可恢復性邊界。

### Codex 安裝

將此 repository 的連結貼給 AI Agent，請它協助把 Skill 安裝到 Codex skills
目錄，然後重新啟動或開啟新的工作階段。也可以參考下方整合說明自行安裝。

使用範例：

```text
Use $build-practical-guide to turn these sources into complete self-study
material. Start by discussing the learner, knowledge boundary, evidence needs,
and teaching route; wait for confirmation before drafting.
```

詳細說明請見 [`integrations/codex.md`](integrations/codex.md)。

### 其他 AI 工具

不支援原生 Skill 載入的 AI 工具，仍可把 `SKILL.md` 當作主要指令，
並依任務載入其中指向的 `references/`。這是通用的手動整合方式，
實際能力仍取決於該工具是否能讀取檔案、執行腳本及遵守分段載入流程。

請見 [`integrations/generic-ai.md`](integrations/generic-ai.md)。

### 選用的數學 SVG 功能

正式數學 SVG 轉換器是選用功能。核心 Skill 不需要 Node.js 或 MathJax
也能運作。若需要此功能，請在
`skills/build-practical-guide/adapters/math-svg/` 中明確執行：

```bash
npm ci
npm run capability
```

請勿提交產生的 `node_modules/`。

## English

`build-practical-guide` is an AI agent skill for turning conversations,
research, work notes, project evidence, and other in-scope sources into complete,
evidence-grounded self-study material. It designs a coherent learning narrative,
a connected knowledge map, worked explanations, and a navigable unit or modular
learning path for the intended learner. A quick reference guide is used only
when explicitly requested.

It emphasizes:

- separating verified facts, reasonable inferences, and unknowns;
- building a concrete reader model, then self-validating evidence, logic,
  practical usability, and reader fit;
- scaling validation to risk and presenting 2–4 consequential-decision options
  with benefits, costs, reader impact, and evidence;
- building mathematical and technical ideas from concrete examples;
- designing instructional visuals around the reader's reasoning process;
- preserving authorization, evidence, and recoverability boundaries.

### Install for Codex

Share this repository link with an AI agent and ask it to install the Skill
for Codex. Start a new session after installation. You can also follow the
platform-specific instructions below to install it yourself.

Example:

```text
Use $build-practical-guide to turn these sources into complete self-study
material. Start by discussing the learner, knowledge boundary, evidence needs,
and teaching route; wait for confirmation before drafting.
```

See [`integrations/codex.md`](integrations/codex.md) for details.

### Other AI tools

For tools without native Skill loading, provide `SKILL.md` as the primary
instruction and load only the referenced files needed for the task. This is an
experimental manual integration; results depend on the tool's file access,
script execution, and instruction-loading behavior.

See [`integrations/generic-ai.md`](integrations/generic-ai.md).

### Optional math SVG support

The formal math SVG adapter is optional. The core Skill works without Node.js
or MathJax. To enable it, explicitly run the following inside
`skills/build-practical-guide/adapters/math-svg/`:

```bash
npm ci
npm run capability
```

Do not commit the generated `node_modules/`.

## License

MIT © 2026 er23ic
