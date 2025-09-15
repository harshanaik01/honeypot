import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# ---------- CONFIG ----------
SMTP_SERVER = "smtp.gmail.com"   # For Gmail
SMTP_PORT = 587
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"   # Use App Password
EMAIL_RECEIVER = "alert_receiver@gmail.com"
# ----------------------------

def send_email_alert(ip, port, command):
    subject = "🚨 Honeypot Alert: New Attack Detected"
    body = f"""
    A new attack attempt has been detected:

    📌 IP Address: {ip}
    📌 Port: {port}
    📌 Command: {command}
    📌 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
            print(f"[+] Email alert sent for attack from {ip}")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")
