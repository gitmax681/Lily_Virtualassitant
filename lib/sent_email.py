import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('manjunatharjun80@gmail.com', 'arjun80&2005')
# an error will be thrown if the email's security app permission is off, turn it on
# accounts.google.com > security> less apps security
server.sendmail('manjunatharjun80@gmail.com',
                "arjunmnath356@gmail.com", 
                "hi arjun this is a email from you itself i am senting this to myself thankyou"
                )