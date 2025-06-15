import smtplib
import os
import zipfile
import requests
from email.message import EmailMessage

# Настройки — заполни своими данными
SMTP_SERVER = "smtp.your-email.com"
SMTP_PORT = 587
SMTP_USER = "your-email@example.com"
SMTP_PASSWORD = "your-password"
EMAIL_TO = ["recipient@example.com"]

TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"

def zip_allure_report(report_dir="allure-results", archive_name="allure-report.zip"):
    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(report_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, report_dir)
                zipf.write(filepath, arcname)
    return archive_name

def send_email(subject, body, attachments=None):
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = ", ".join(EMAIL_TO)
    msg["Subject"] = subject
    msg.set_content(body)

    if attachments:
        for filepath in attachments:
            with open(filepath, "rb") as f:
                data = f.read()
                msg.add_attachment(data, maintype="application", subtype="zip", filename=os.path.basename(filepath))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
    print("Email sent.")

def send_telegram_document(file_path):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as f:
        files = {"document": f}
        data = {"chat_id": TELEGRAM_CHAT_ID}
        r = requests.post(url, files=files, data=data)
    if r.status_code == 200:
        print("Telegram report sent.")
    else:
        print("Telegram sending failed:", r.text)

if __name__ == "__main__":
    archive = zip_allure_report()
    send_email("Allure Test Report", "Attached is the latest Allure report.", [archive])
    send_telegram_document(archive)
