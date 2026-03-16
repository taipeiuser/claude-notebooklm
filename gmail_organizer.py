#!/usr/bin/env python3
"""
Gmail 重要郵件整理工具
使用 Gmail API 獲取今日郵件，並透過 Claude 分析整理重要內容
"""

import os
import base64
import json
from datetime import datetime, timezone
from email import message_from_bytes
from email.utils import parsedate_to_datetime

from dotenv import load_dotenv
import anthropic
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"


def get_gmail_service():
    """建立並回傳 Gmail API 服務"""
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(
                    f"找不到 {CREDENTIALS_FILE}。\n"
                    "請先從 Google Cloud Console 下載 OAuth 憑證，\n"
                    "並儲存為 credentials.json。\n"
                    "詳細說明請參考 README.md。"
                )
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def get_today_emails(service, max_results=50):
    """獲取今日收到的郵件"""
    today = datetime.now(timezone.utc).strftime("%Y/%m/%d")
    query = f"after:{today}"

    try:
        results = service.users().messages().list(
            userId="me",
            q=query,
            maxResults=max_results
        ).execute()

        messages = results.get("messages", [])
        if not messages:
            return []

        emails = []
        for msg_ref in messages:
            msg = service.users().messages().get(
                userId="me",
                id=msg_ref["id"],
                format="full"
            ).execute()
            emails.append(parse_email(msg))

        return emails

    except HttpError as error:
        raise RuntimeError(f"Gmail API 錯誤: {error}")


def parse_email(msg):
    """解析郵件內容"""
    headers = {h["name"].lower(): h["value"] for h in msg["payload"].get("headers", [])}

    subject = headers.get("subject", "(無主旨)")
    sender = headers.get("from", "(未知寄件者)")
    date_str = headers.get("date", "")
    snippet = msg.get("snippet", "")
    labels = msg.get("labelIds", [])

    try:
        date = parsedate_to_datetime(date_str).strftime("%H:%M") if date_str else ""
    except Exception:
        date = ""

    body = extract_body(msg["payload"])

    return {
        "id": msg["id"],
        "subject": subject,
        "sender": sender,
        "date": date,
        "snippet": snippet,
        "body": body[:2000] if body else snippet,
        "labels": labels,
        "is_unread": "UNREAD" in labels,
        "is_starred": "STARRED" in labels,
        "is_important": "IMPORTANT" in labels,
    }


def extract_body(payload):
    """從郵件 payload 中提取純文字內容"""
    body = ""

    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                data = part.get("body", {}).get("data", "")
                if data:
                    body = base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
                    break
            elif part["mimeType"] == "multipart/alternative":
                body = extract_body(part)
                if body:
                    break
    else:
        mime_type = payload.get("mimeType", "")
        if "text" in mime_type:
            data = payload.get("body", {}).get("data", "")
            if data:
                body = base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")

    return body.strip()


def analyze_emails_with_claude(emails):
    """使用 Claude 分析並整理郵件"""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "找不到 ANTHROPIC_API_KEY 環境變數。\n"
            "請在 .env 檔案中設定：ANTHROPIC_API_KEY=your_key"
        )

    client = anthropic.Anthropic(api_key=api_key)

    today = datetime.now().strftime("%Y年%m月%d日")

    emails_text = ""
    for i, email in enumerate(emails, 1):
        status_tags = []
        if email["is_unread"]:
            status_tags.append("未讀")
        if email["is_starred"]:
            status_tags.append("已加星號")
        if email["is_important"]:
            status_tags.append("重要")

        status = f"[{', '.join(status_tags)}]" if status_tags else ""

        emails_text += f"""
---郵件 {i}---
時間: {email['date']}
寄件者: {email['sender']}
主旨: {email['subject']} {status}
內容摘要: {email['body'][:500]}
"""

    prompt = f"""今天是 {today}，以下是今天收到的所有 Gmail 郵件：

{emails_text}

請幫我：
1. **篩選出重要郵件**：識別需要回覆、採取行動、或包含重要資訊的郵件
2. **分類整理**：將郵件按類型分組（例如：工作/業務、帳單/交易、通知、訂閱資訊等）
3. **摘要說明**：每封重要郵件提供一句話重點說明
4. **行動建議**：指出哪些郵件需要今天回覆或處理

請用繁體中文回答，格式清晰易讀。若有不需要特別關注的廣告或自動通知，可以歸納為一行說明即可。"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text


def main():
    print("=== Gmail 今日重要郵件整理 ===\n")

    print("正在連接 Gmail...")
    try:
        service = get_gmail_service()
    except FileNotFoundError as e:
        print(f"錯誤: {e}")
        return

    print("正在獲取今日郵件...")
    try:
        emails = get_today_emails(service)
    except RuntimeError as e:
        print(f"錯誤: {e}")
        return

    if not emails:
        print("今天沒有收到任何郵件。")
        return

    print(f"共找到 {len(emails)} 封今日郵件，正在使用 Claude 分析...\n")

    try:
        analysis = analyze_emails_with_claude(emails)
    except ValueError as e:
        print(f"錯誤: {e}")
        return

    print(analysis)
    print("\n" + "=" * 50)

    summary_file = f"email_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(f"Gmail 郵件整理報告\n")
        f.write(f"日期: {datetime.now().strftime('%Y年%m月%d日 %H:%M')}\n")
        f.write("=" * 50 + "\n\n")
        f.write(analysis)

    print(f"\n報告已儲存至: {summary_file}")


if __name__ == "__main__":
    main()
