# Claude NotebookLM - Gmail 重要郵件整理

使用 Gmail API + Claude AI 自動整理今日重要郵件。

## 功能

- 自動獲取今日收到的所有 Gmail 郵件
- 透過 Claude AI 分析並篩選重要郵件
- 按類型分類（工作、帳單、通知等）
- 提供每封重要郵件的重點摘要
- 建議需要優先處理的行動事項
- 將報告儲存為文字檔

## 環境需求

- Python 3.9+
- Google Cloud 專案（需啟用 Gmail API）
- Anthropic API Key

## 安裝步驟

### 1. 安裝相依套件

```bash
pip install -r requirements.txt
```

### 2. 設定 Anthropic API Key

複製 `.env.example` 為 `.env` 並填入你的 API Key：

```bash
cp .env.example .env
```

編輯 `.env`：
```
ANTHROPIC_API_KEY=your_actual_api_key
```

### 3. 設定 Gmail API 憑證

1. 前往 [Google Cloud Console](https://console.cloud.google.com/)
2. 建立新專案或選擇現有專案
3. 啟用 **Gmail API**
4. 建立 **OAuth 2.0 用戶端 ID**（類型選「桌面應用程式」）
5. 下載憑證 JSON 檔，命名為 `credentials.json` 並放置於專案根目錄

### 4. 執行

```bash
python gmail_organizer.py
```

首次執行時會開啟瀏覽器要求授權，授權後會自動儲存 `token.json` 供後續使用。

## 輸出範例

```
=== Gmail 今日重要郵件整理 ===

共找到 12 封今日郵件，正在使用 Claude 分析...

## 重要郵件

### 需要立即處理
1. [09:30] 主管 - 下午會議議程確認
   需在 12:00 前回覆確認出席

### 工作/業務
2. [10:15] 客戶 ABC - 合約修改意見
   客戶提出 3 點修改建議，需本週回覆

### 帳單/交易
3. [08:00] 銀行 - 信用卡帳單
   本月帳單 NT$3,250，截止日 3/25

### 訂閱通知（共 7 封）
   GitHub、Notion 等服務的自動通知，無需特別處理
```

## 注意事項

- `token.json` 和 `credentials.json` 包含敏感資訊，已加入 `.gitignore`
- 每日有免費 API 額度，一般個人使用不會超過
