import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(reciever,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('keerthanavk38@gmail.com','kevimach@01')
    email = EmailMessage()
    email['From'] = 'keerthanavk38@gmail.com'
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    
email_list = {
    'self': 'kevimach011997@gmail.com',
    'keerthana': 'keerthanavk38@gmail.com',
    'gali': 'galibhaskar57@gmail.com'
}

def get_email_info():
    talk('To whom do you want to send an email')
    name = get_info()
    print(name)
    reciever = email_list[name]
    print(reciever)
    talk('What is the subject of the email')
    subject = get_info()
    talk('Tell me the text of your email')
    message = get_info()

    send_email(reciever,subject,message)


get_email_info()