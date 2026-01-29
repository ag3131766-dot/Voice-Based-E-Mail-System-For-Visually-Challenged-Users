import smtplib
from voice import speak, listen

def send_email(sender, password):
    speak("Say receiver email address")
    receiver = listen().replace(" ", "")

    speak("Say the subject")
    subject = listen()

    speak("Say the message")
    message = listen()

    email_text = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, email_text)
        server.quit()
        speak("Email sent successfully")
    except:
        speak("Failed to send email")
