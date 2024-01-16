import streamlit as st
from send_email import sendEmail

st.header('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input('Your Email Address')
    raw_message = st.text_area('Your Message')
    message = f"""\
    Subject: New mail from {user_email}
    
    From: {user_email}
    {raw_message}
    """
    button = st.form_submit_button('Submit')
    if button:
        sendEmail(message)
        st.info('Your Email has been sent successfully!!!')