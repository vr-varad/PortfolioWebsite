import smtplib,ssl

host = 'smtp.gmail.com'
port = 465


def sendEmail(message):
    username = 'varadgupta21@gmail.com'
    password = 'dqsmcknylnpvzpsy'
    reciever_email = 'varadgupta21@gmail.com'

    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=my_context ) as server:
        server.login(username,password)
        server.sendmail(username,reciever_email,message)

