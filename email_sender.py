import smtplib
from email.mime.text import MIMEText
from secrets import sender_email, receiver_email, password

sender = sender_email
receiver = receiver_email
password = password

subject = "Hello from Python"
body = "This is a test email sent using Python."

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.send_message(msg)
server.quit()

print("Email sent successfully!")
