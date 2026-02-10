import smtplib
from email.mime.text import MIMEText
from secrets import sender_email, receiver_email, password

def send_email(body: str, subject: str = "Hello from Python", to_email: str = receiver_email):
    """Sends an email with the provided body and subject."""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()

    return "Email sent successfully!"

if __name__ == "__main__":
    send_email("This is a test email sent using Python.")
    print("Email sent successfully!")
