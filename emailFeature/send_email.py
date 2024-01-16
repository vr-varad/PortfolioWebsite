import smtplib, ssl
import streamlit as st
host = 'smtp.gmail.com'
port = 465


def sendEmail(message):
    username = st.secrets['email']
    password = st.secrets['password']
    reciever_email = st.secrets['email']

    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, reciever_email, message)
