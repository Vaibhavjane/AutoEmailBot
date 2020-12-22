import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('vjane18@gmail.com','vaibhav2838')
server.sendmail('vjane18@gmail.com',
                'vaibhavjane@gmail.com',
                'Hi vaibhav i hope you getting my message'
                )