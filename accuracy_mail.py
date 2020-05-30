with open("/root/task3/accuracy.txt", "r") as f:
 acc=f.read()
import smtplib as sm
from email.mime.multipart import MIMEmultipart
msg="The model has been successfully created with the desired accuracy!! \nAccuracy of the model is: "+str(acc)+" percentage"
server=sm.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login("robertjr.2801@gmail.com","Modi@1999")
server.sendmail("robertjr.2801@gmail.com", "modifearless@gmail.com", msg)
server.close()
