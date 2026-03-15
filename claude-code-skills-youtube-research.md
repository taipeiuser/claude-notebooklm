# Claude Code Skills — YouTube 影片研究報告

> **研究日期：** 2026-03-15
> **來源：** 網路搜尋、Medium 排名評測、官方課程資料

---

## 概述

Claude Code Skills（代理技能）是 Anthropic 於 **2025 年 10 月 16 日** 正式發布的功能，並在 **2025 年 12 月 18 日** 開放為跨平台開放標準。Skills 讓 Claude 透過 `SKILL.md` 檔案載入客製化指令、腳本與資源，可自動觸發或以 `/skill-name` 斜線指令調用。

本報告挑選 YouTube 上關於 Claude Code Skills 最熱門、最具代表性的 **5 支影片**，進行專業分析與總結。

---

## 熱門影片 Top 5

---

### 🥇 Video 1 — Peter Yang：Claude Code 初學者教學（15 分鐘建置 Movie App）

| 欄位 | 內容 |
|------|------|
| **標題** | Claude Code Beginner's Tutorial: Build a Movie App in 15 Minutes |
| **創作者** | Peter Yang（@petergyang / Creator Economy） |
| **頻道** | [@peteryangyt](https://youtube.com/@peteryangyt) |
| **影片連結** | [https://youtu.be/GepHGs_CZdk](https://youtu.be/GepHGs_CZdk) |
| **發布日期** | 2025 年 9 月 |
| **影片時長** | ~17 分鐘 |
| **熱門程度** | 受 Class Central 收錄，跨平台廣泛分享 |

**核心內容：**
- 在終端機與 Cursor 中安裝 Claude Code
- 利用 AI 解析現有程式碼庫
- **Plan Mode（規劃模式）**：在撰寫程式碼前先產生詳細規格
- 初始化 `CLAUDE.md` 建立持久專案記憶
- 一次到位打造「電影觀看清單」功能

**重點時間戳：**
- `00:00` — 安裝 Claude Code
- `03:29` — Clone 電影 App，讓 Claude 解析程式碼庫
- `07:37` — 用 Plan Mode 寫詳細規格
- `10:44` — 初始化 `claude.md`
- `13:43` — 一次性建置 Watchlist 功能

**分析：** 這是最適合完全初學者的入門影片。Peter 強調「先規劃、再執行」的工作流程，示範了 CLAUDE.md 持久記憶與 Plan Mode 的核心優勢，是理解 Claude Code Skills 概念的最佳起點。

---

### 🥈 Video 2 — Peter Yang：建置 YouTube AI 研究代理（15 分鐘）

| 欄位 | 內容 |
|------|------|
| **標題** | Claude Code Tutorial: Build a YouTube Research Agent using Slash Commands |
| **創作者** | Peter Yang（@petergyang） |
| **影片連結** | [https://youtu.be/iW0lMW-Ff5I](https://youtu.be/iW0lMW-Ff5I) |
| **發布日期** | 2025 年 |
| **影片時長** | ~15 分鐘 |
| **熱門程度** | 被 Creator Economy Newsletter 大量推廣 |

**核心內容：**
- 建立 `/youtube` 斜線指令（Slash Command）
- 實作「分析任意頻道最熱門影片」功能
- 批次處理多個 YouTube 頻道的分析
- Spec（規格）→ TODO → Code 的標準工作流程

**分析：** 這支影片直接示範了 Skills 的核心概念——將任務打包成可重複調用的斜線指令。觀眾能清晰看到 `SKILL.md` 格式與斜線指令如何結合，理解「Skill 不只是 Prompt，而是 Claude 的行動劇本」。

---

### 🥉 Video 3 — Sabrina Ramonov：Claude Code 完整課程（建置 AI 社群媒體助理）

| 欄位 | 內容 |
|------|------|
| **標題** | CLAUDE CODE FULL COURSE!! (for beginners) |
| **創作者** | Sabrina Ramonov（Forbes 30 Under 30） |
| **頻道** | [@sabrinaramonov](https://www.sabrina.dev) |
| **課程連結** | [sabrina.dev — Claude Code Full Course](https://www.sabrina.dev/p/claude-code-full-course-for-beginners) |
| **影片時長** | ~75 分鐘 |
| **熱門程度** | 被 The Neuron、多個 AI 學習平台評選為最推薦初學者課程 |

**核心內容：**

| 章節 | 主題 |
|------|------|
| Setup | 安裝 Claude Code、VS Code、處理權限設定 |
| **Skills** | **建立客製化 Skills 撰寫社群貼文** |
| Brand Voice | 教 AI 模仿你的寫作風格（或 Hormozi 風格） |
| Quality Gates | 使用 Hooks 檢查格式與品質問題 |
| Subagents | 建立自主代理協作系統 |
| MCP | 連接 MCP Server 發布到社群媒體 |

**分析：** Sabrina 的課程是最完整涵蓋 Skills 實戰應用的教學。她特別強調**安全模式（Safe Mode）與權限管理**，讓 Claude Code 不會未經許可執行危險操作。課程中直接示範「建立 Skills 撰寫貼文」，是目前最貼近 Skills 功能核心的實用教學。

---

### 4️⃣ Video 4 — Nick Saraev：Claude Code 4 小時完整大師課

| 欄位 | 內容 |
|------|------|
| **標題** | Claude Code Full Course: Build & Sell (4 Hours) |
| **創作者** | Nick Saraev（Maker School 創辦人） |
| **頻道** | Nick Saraev YouTube（150,000+ 訂閱） |
| **參考連結** | [LinkedIn 宣布貼文](https://www.linkedin.com/posts/nick-saraev_i-just-published-what-i-think-is-the-most-activity-7429910067052969984-iBhE) |
| **影片時長** | 4 小時 |
| **熱門程度** | 數百萬次觀看紀錄，業界最推薦的進階課程 |

**核心內容：**
- 子代理（Sub-agents）的正確使用方式
- **Git Worktrees 並行開發**
- 雲端部署端到端流程
- IDE 比較（VS Code vs Antigravity）
- Context Window 管理與優化策略
- Hooks 與斜線指令進階應用
- 完整自動化業務建置流程

**分析：** Nick 是目前最深入、最全面的 Claude Code 技術課程。特別是他對**並行開發（Parallelization）**與**上下文視窗管理（Context Management）**的講解，被評為「區分初級與高級 Claude Code 使用者的關鍵知識」。對於已有基礎的開發者，這是必看的進階教材。

---

### 5️⃣ Video 5 — Anthropic 官方：Introduction to Agent Skills（官方課程）

| 欄位 | 內容 |
|------|------|
| **標題** | Introduction to Agent Skills |
| **創作者** | Anthropic（官方出品） |
| **平台** | Anthropic Academy / Skilljar |
| **課程連結** | [anthropic.skilljar.com/introduction-to-agent-skills](https://anthropic.skilljar.com/introduction-to-agent-skills) |
| **影片時長** | 6 堂課 / 共 30 分鐘 |
| **發布日期** | 2026 年 3 月 2 日（Anthropic Academy 正式上線） |
| **費用** | 完全免費 |

**核心內容：**
- Agent Skills 的設計理念與架構
- `SKILL.md` 格式詳解：YAML frontmatter + Markdown 指令
- Progressive Disclosure（漸進式揭露）機制
- 建立、測試、分享 Skills 的完整流程
- 組織層級部署（Enterprise Managed Skills）

**分析：** 這是由 Skills 功能**發明者親自授課**的官方教學，涵蓋所有技術細節和最佳實踐，無任何錯誤或過時資訊。雖然不在 YouTube，但作為「第一手權威資料」，是深入理解 Claude Code Skills 不可或缺的核心資源。

---

## 專業分析總結

### 1. Claude Code Skills 的核心價值

```
Skills = SKILL.md 指令 + 可選腳本/資源 + 自動觸發邏輯
```

Skills 解決了三個根本問題：
- **可重複性**：不需每次重新描述工作流程
- **模組化**：一個技能一個職責，易於維護
- **可分享性**：透過 Git 版本控制，團隊共享一致的 AI 工作方式

### 2. 影片內容趨勢分析

| 趨勢 | 說明 |
|------|------|
| **初學者友善化** | 最熱門影片均強調「15-20 分鐘完成第一個作品」 |
| **實戰導向** | 抽象概念說明減少，直接 demo 真實 use case |
| **Skills 整合** | 幾乎所有 2025 年後的教學均加入 Skills/Hooks 內容 |
| **品質管控意識** | Quality Gates、Safe Mode 被多位創作者強調 |

### 3. 學習路徑建議

```
初學者路徑：
Peter Yang (15 min) → Sabrina Ramonov (75 min) → Anthropic 官方課程 (30 min)

進階開發者路徑：
Anthropic 官方課程 → Nick Saraev 4 小時大師課 → 自建 Skills 實驗
```

### 4. Skills 生態系現況（2026 年 3 月）

| 指標 | 數據 |
|------|------|
| 最多安裝數的 Skill | `find-skills`（Vercel Labs）— 418,600+ 安裝 |
| 官方最熱門 Skill | `frontend-design`（Anthropic）— 277,000+ 安裝 |
| 生態系規模 | 85,000+ Skills 跨平台索引 |
| 跨平台支援 | Claude Code、Cursor、Gemini CLI、Codex CLI、GitHub Copilot |

---

## 相關資源清單

| 資源 | 連結 |
|------|------|
| 官方 Claude Code Skills 文件 | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| Agent Skills 開放標準 | [agentskills.io](https://agentskills.io) |
| Anthropic 官方 Skills 倉庫 | [github.com/anthropics/skills](https://github.com/anthropics/skills) |
| Anthropic Academy 免費課程 | [anthropic.skilljar.com](https://anthropic.skilljar.com) |
| Awesome Claude Skills | [github.com/travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) |
| Awesome Claude Code | [github.com/hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) |
| Claude Skills 市場 | [claude.com/skills](https://claude.com/skills) |
| Peter Yang 系列教學 | [creatoreconomy.so](https://creatoreconomy.so) |
| Sabrina Ramonov 課程 | [sabrina.dev](https://www.sabrina.dev) |
