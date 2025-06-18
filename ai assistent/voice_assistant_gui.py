# pip install SpeechRecognition
# pip install pyttsx3
# pip install pywhatkit
# pip install wikipedia

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyaudio
import datetime
import requests


def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()
phone_numbers = {"Manas":"1234567890","Rohit":"999999999","Mohit":"1111111111","Ram":"0000000000"}

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening... Speak something.")
            audioin = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            my_text = r.recognize_google(audioin)
            print("You said:", my_text)
            

        #ask to play song
            if 'play' in my_text:
                my_text = my_text.replace('play','')
                speak('playing' + my_text)
                pywhatkit.playonyt(my_text)

                #ask date
            if 'date' in my_text:
                today = datetime.date.today()
                speak('today is' + str(today))

            #ask time
            if 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak(timenow)

            #ask details of a person
            if "who is" in my_text:
                person = my_text.replace('Who is', '')
                info = wikipedia.summary(person,1)
                speak(info)

            #ask phone numbers
            if "phone number" in my_text:
                names = list(phone_numbers)
                print(names)
                for name in names:
                    if name.lower() in my_text.lower():
                        print(name + "phone number is" + phone_numbers[name])
                        speak(name + "phone number is" + phone_numbers[name])
             #riddle
            if "riddle" in my_text:
                speak("What has keys but can't open locks? It's a keyboard!")
           

    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase.")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print("General error:", e)

commands()
