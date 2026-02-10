import smtplib
from secrets import sender, receiver, password
from email.mime.text import MIMEText

sender = "4mh23cs107@gmail.com"
receiver = "sanikamj5@gmail.com"
password = "lyku gmiz ehhn geed"

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
