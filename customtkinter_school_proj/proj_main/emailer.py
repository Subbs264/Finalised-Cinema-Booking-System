import smtplib
from email.message import EmailMessage

def email(name, qr_filepath):

    content = f'Hello {name}!\n This is your ticket to the event you booked:'

    message = EmailMessage()
    message['Subject'] = 'Performance Ticket'
    message['From'] = 'abc123@gmail.com'
    message['To'] = 'Attendee@gmail.com'
    message.set_content(content)

    with open(qr_filepath, 'rb') as file:
        message.add_attachment(file.read(), maintype='image', subtype='png', filename='ticket_qr.png')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('abc123@gmail.com', 'password123')
        smtp.send_message(message)
