# NotebookLM「Demo - Claude」匯入操作指南

> **說明：** NotebookLM 是 Google 的 Web 應用程式，需要 Google 帳號登入並透過瀏覽器操作，無法透過程式自動存取。本指南提供所有匯入所需的完整素材與步驟。

---

## 匯入內容清單

本次研究共準備 **6 個來源（Sources）** 供匯入：

| # | 類型 | 來源 | 說明 |
|---|------|------|------|
| 1 | YouTube 影片 | https://youtu.be/GepHGs_CZdk | Peter Yang：15 分鐘 Movie App |
| 2 | YouTube 影片 | https://youtu.be/iW0lMW-Ff5I | Peter Yang：YouTube Research Agent |
| 3 | 網站連結 | https://www.sabrina.dev/p/claude-code-full-course-for-beginners | Sabrina Ramonov 完整課程 |
| 4 | 網站連結 | https://anthropic.skilljar.com/introduction-to-agent-skills | Anthropic 官方課程 |
| 5 | 文字檔案 | `notebooklm-source-claude-skills.txt` | 完整研究分析報告 |
| 6 | 網站連結 | https://code.claude.com/docs/en/skills | 官方技術文件 |

---

## 操作步驟

### Step 1：開啟 NotebookLM

1. 開啟瀏覽器，前往 [https://notebooklm.google.com](https://notebooklm.google.com)
2. 以 Google 帳號登入（taipeiuser@gmail.com）
3. 在左側筆記本列表中點選「**Demo - Claude**」

---

### Step 2：新增 YouTube 影片來源

點選右側「**Sources**」面板的「**+ Add source**」按鈕：

**影片 1：**
1. 選擇「YouTube」
2. 貼上：`https://youtu.be/GepHGs_CZdk`
3. 確認標題顯示：「Claude Code Beginner's Tutorial: Build a Movie App in 15 Minutes」
4. 點「Insert」

**影片 2：**
1. 再次點「+ Add source」→「YouTube」
2. 貼上：`https://youtu.be/iW0lMW-Ff5I`
3. 確認標題顯示 YouTube Research Agent 相關
4. 點「Insert」

---

### Step 3：新增網站連結來源

依序新增以下 3 個 URL（每次點「+ Add source」→「Website」）：

```
https://www.sabrina.dev/p/claude-code-full-course-for-beginners
https://anthropic.skilljar.com/introduction-to-agent-skills
https://code.claude.com/docs/en/skills
```

---

### Step 4：上傳文字分析報告

1. 點「+ Add source」→「Upload file」
2. 選擇專案目錄中的：`notebooklm-source-claude-skills.txt`
3. 等待上傳完成（約 5-10 秒）

---

### Step 5：驗證來源清單

確認 Sources 面板顯示 6 個來源：

- [ ] YouTube：GepHGs_CZdk（Peter Yang Movie App）
- [ ] YouTube：iW0lMW-Ff5I（YouTube Research Agent）
- [ ] Website：sabrina.dev（Ramonov 完整課程）
- [ ] Website：anthropic.skilljar.com（官方課程）
- [ ] Website：code.claude.com/docs/en/skills（官方文件）
- [ ] File：notebooklm-source-claude-skills.txt（研究報告）

---

### Step 6：建議的後續操作（可選）

來源匯入後，可在 NotebookLM 中嘗試以下問題：

```
Q1: Claude Code Skills 的核心概念是什麼？與 Slash Command 有何不同？

Q2: 初學者應該從哪支影片開始學習 Claude Code Skills？

Q3: SKILL.md 的 YAML frontmatter 有哪些重要欄位？

Q4: 目前最熱門的 5 個 Claude Code Skills 是什麼？各有多少安裝數？

Q5: 比較 Peter Yang、Sabrina Ramonov、Nick Saraev 三位創作者的教學風格差異。
```

---

## 匯入的核心分析結論

供快速複製貼入 NotebookLM 備忘筆記（Note）：

```
Claude Code Skills 研究摘要（2026-03-15）

精選 Top 5 YouTube 影片：
1. Peter Yang — Build a Movie App (youtu.be/GepHGs_CZdk) ★ 最佳入門
2. Peter Yang — YouTube Research Agent (youtu.be/iW0lMW-Ff5I) ★ Skills 實作
3. Sabrina Ramonov — Full Course (sabrina.dev) ★ 最完整實戰課程
4. Nick Saraev — 4hr Masterclass ★ 進階開發者首選
5. Anthropic 官方 — Introduction to Agent Skills ★ 官方權威

核心要點：
• Skills = SKILL.md + 自動觸發 + 漸進式揭露機制
• 每個 Skill 初始只消耗 ~100 tokens，觸發後不超過 5K tokens
• 跨平台開放標準：Claude Code、Cursor、Gemini CLI、Codex CLI 均支援
• 最熱門 Skill：find-skills（418,600+ 安裝）
• 生態系規模：85,000+ Skills（2026 年 3 月）

學習路徑（初學者）：
Peter Yang (15min) → Sabrina Ramonov (75min) → Anthropic 官方 (30min)
```

---

## 本專案相關檔案

| 檔案 | 用途 |
|------|------|
| `claude-code-skills-youtube-research.md` | 完整 Markdown 研究報告 |
| `claude-code-skills-infographic.html` | 互動式資訊圖表（瀏覽器開啟） |
| `notebooklm-source-claude-skills.txt` | NotebookLM 文字來源（直接上傳） |
| `notebooklm-import-guide.md` | 本操作指南 |
