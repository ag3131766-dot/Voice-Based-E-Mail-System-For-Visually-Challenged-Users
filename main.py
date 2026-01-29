from voice import speak, listen
from email_sender import send_email
from email_reader import read_email

EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"

speak("Welcome to Voice Based Email System")

while True:
    speak("Say send email or read email or exit")
    command = listen()

    if "send" in command:
        send_email(EMAIL, PASSWORD)

    elif "read" in command:
        read_email(EMAIL, PASSWORD)

    elif "exit" in command:
        speak("Goodbye")
        break
