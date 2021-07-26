import smtplib
import tkinter as tk
from tkinter import simpledialog

# To store the email and the password
with open("Email.txt", "r") as file:
    credentials = file.read().replace('\n', ',')
credentials = credentials.split(',')

from_ = credentials[0]

window = tk.Tk()
to_ = simpledialog.askstring("Email", "To: ")
msg = simpledialog.askstring("Email", "Your message: ")

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(credentials[0], credentials[1])  # Make sure to have enabled the permission to access insecure apps
# (https://www.google.com/settings/security/lesssecureapps)
server.sendmail(from_addr=from_, to_addrs=to_, msg=msg)

