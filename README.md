# Build Practical Guide

[繁體中文](#繁體中文) · [English](#english)

## 繁體中文

`build-practical-guide` 是一個 AI Agent Skill，用來把對話、工作筆記、
錯誤紀錄、既有文件與專案證據，整理成經過驗證、適合初學者閱讀的
Markdown 教學指南或模組化學習教材。

它特別重視：

- 區分已驗證事實、合理推論與未知資訊；
- 先建立具體讀者模型，再從證據、邏輯、實作與讀者四個層次自我驗證；
- 依風險調整驗證深度，並在重要決策中提供 2–4 個具成本、效益與
  讀者影響說明的選項；
- 從具體例子建立數學與技術概念；
- 以教學推理結構設計技術插圖；
- 維護既有教材時保留授權、證據與可恢復性邊界。

### Codex 安裝

將 [`skills/build-practical-guide`](skills/build-practical-guide) 複製到
Codex 的 skills 目錄，然後重新啟動或開啟新的工作階段：

```bash
cp -R skills/build-practical-guide ~/.codex/skills/
```

使用範例：

```text
Use $build-practical-guide to turn these notes into a verified,
beginner-friendly Markdown guide.
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

`build-practical-guide` is an AI agent skill for turning conversations, work
notes, error records, existing documentation, and project evidence into
verified, beginner-friendly Markdown guides or modular learning packages.

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

Copy [`skills/build-practical-guide`](skills/build-practical-guide) into your
Codex skills directory, then restart Codex or begin a new session:

```bash
cp -R skills/build-practical-guide ~/.codex/skills/
```

Example:

```text
Use $build-practical-guide to turn these notes into a verified,
beginner-friendly Markdown guide.
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
