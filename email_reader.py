import imaplib
import email
from voice import speak

def read_email(user, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user, password)
    mail.select("inbox")

    result, data = mail.search(None, "ALL")
    ids = data[0].split()
    latest_id = ids[-1]

    result, msg_data = mail.fetch(latest_id, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    speak("You have a new email")
    speak("Subject is " + msg["subject"])
    speak("From " + msg["from"])
