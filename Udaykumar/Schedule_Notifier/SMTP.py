import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

def email_service(Receiver_Email, Person_name):
    # Sender's email details
    sender_email = 'sender@gmail.com'
    sender_password = 'app_password'

    # Recipient's email details
    recipient_email = Receiver_Email

    # Email content
    subject = 'Builder Tracker Reminder'
    body_1 = f'Dear {Person_name},' \
           '\n' \
            '\n' \
           'Good Morning, This is a reminder to start your "Builder Tracker" timer and run it for 8 hours without losing any work hours.' \
           '\n' \
            '\n' \
            'Please ignore this email if you have already started the tracker.' \
           '\n' \
            '\n' \
           'Thank you,\n' \
           'BeSquare Technologies' \
            '\n' \
            '\n' \
            'NOTE: This is a system-generated email. Please do not reply to this message.' \

    body_2 = f'Dear {Person_name},' \
           '\n' \
            '\n' \
           'Good Evening, This is a reminder to stop your "Builder Tracker" timer after completing 8 working hours.' \
           '\n' \
            '\n' \
            'Please ignore this email if you have already stopped the tracker.' \
           '\n' \
            '\n' \
           'Thank you,\n' \
           'BeSquare Technologies' \
            '\n' \
            '\n' \
            'NOTE: This is a system-generated email. Please do not reply to this message.' \

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    message_attached = False  # Flag to keep track if a message has been attached
    while not message_attached:
        time_now = datetime.datetime.now().strftime("%I:%M%p")

        if "09:55AM" <= time_now <= "10:00AM":
            message.attach(MIMEText(body_1, 'plain'))
            message_attached = True
        elif "07:30PM" <= time_now <= "07:35PM":
            message.attach(MIMEText(body_2, 'plain'))
            message_attached = True

    try:
        # Connect to Gmail's SMTP server using SSL
        # SMTP - Simple Mail Transfer Protocol
        # SMTP_SSL - Simple Mail Transfer Protocol_Secure Socket Layer will use local host & port as 465, if not given
        with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
            # Login to the Gmail account
            smtp.login(sender_email, sender_password)

            # Send the email
            smtp.send_message(message)

        # print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Error: unable to send email.")
        print(str(e))

