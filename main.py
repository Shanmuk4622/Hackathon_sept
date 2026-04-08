
import speech_recognition as sr
import pyaudio
import os
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

query = "No input"
def say(text):
    print(f"say : {text}")
    speaker.Speak(text)

def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language="en-in")
            print(said)
        except Exception as e :
            print("Exception"+ str(e))
    return said


if __name__ == '__main__' :
    print("PyCharm")
    say("Hello I am jarvis A I")
    while True :
        print("Listining...")
        query = takeCommand()
        say(query)
        if "open youtube" in query.lower():
            webbrowser.open("https://youtube.com")
            say("opeaning You tube")