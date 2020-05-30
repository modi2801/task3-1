import smtplib as sm
msg="The model is not working properly!!!"
server=sm.SMTP_SSL("smtp.gmail.com", 465)
server.login("robertjr.2801@gmail.com","wczwuwovnebmzrsu")
server.sendmail("robertjr.2801@gmail.com","modifearless@gmail.com", msg)
server.close()