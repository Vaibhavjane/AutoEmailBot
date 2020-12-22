import smtplib
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('listening.......')
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)
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