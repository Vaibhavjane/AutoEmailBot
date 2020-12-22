import smtplib
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening.......')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('vjane18@gmail.com','vaibhav2838')
    server.sendmail('vjane18@gmail.com',
                'vaibhavjane@gmail.com',
                'Hi vaibhav i hope you getting my message'
                )
def get_email_info():
    talk('To whom want to send email')
    name = get_info()
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()

get_email_info()
