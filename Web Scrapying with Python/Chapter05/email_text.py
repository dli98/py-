import smtplib

from email.mime.text import MIMEText

msg = MIMEText("This is a mail test")

msg['Subject'] = "An Email ALERT"
msg['From'] = "ds@ds-virtual-machine"
msg['To'] = "942203701@qq.com"

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
