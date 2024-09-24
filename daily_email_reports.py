import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email details
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient@example.com'

# Create the email content
def create_email_report():
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = RECIPIENT_EMAIL
    message['Subject'] = 'Daily Report'
    
    # Email body
    body = """
    Hi there,

    This is your daily report.

    Regards,
    Your Automation Script
    """
    
    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))
    
    return message

# Send the email
def send_email():
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Create the email content
        email_content = create_email_report()
        
        # Send the email
        server.send_message(email_content)
        print('Email sent successfully!')
        
        # Close the connection
        server.quit()
    except Exception as e:
        print(f'Failed to send email: {e}')

# Schedule the email to be sent daily at a specific time
def schedule_daily_email(time_of_day='09:00'):
    schedule.every().day.at(time_of_day).do(send_email)
    print(f'Scheduled daily email at {time_of_day}')
    while True:
        schedule.run_pending()
        time.sleep(1)

# Run the scheduling function
if __name__ == "__main__":
    schedule_daily_email('09:00')  # Set the time to send the email daily
