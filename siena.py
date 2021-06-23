import speech_recognition as sr # pip install speechRecognition
import pyttsx3                  # pip install pyttsx3
import datetime
import wikipedia                # pip install wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha             # pip install wolframalpha
import json
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Hello,Good Morning!")
        speak("Hello,Good Morning!")
    elif hour>=12 and hour<18:
        print("Hello,Good Afternoon!")
        speak("Hello,Good Afternoon!")
    else:
        print("Hello,Good Evening!")
        speak("Hello,Good Evening!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        statement=""
    try:
        statement=r.recognize_google(audio,language='en-in')
        print(f"User: {statement}\n")
    except Exception as e:
        speak("Try again...")
        return "None"
    return statement

if __name__=='__main__':
    wishMe()
    print("Loading your AI personal assistant - Siena")
    speak("Loading your AI personal assistant - Siena")

    while True:
        speak("How can I help you ?")
        statement = takeCommand().lower()

        # Turn Siena off
        if "bye" in statement or "ok bye" in statement or "stop" in statement or "end" in statement:
            speak('Your personal desktop assistant Siena is shutting down')
            print('Your personal desktop assistant Siena is shutting down')
            break

        # Wikipedia
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            print(results)
            speak("According to Wikipedia")
            speak(results)

        # Youtube
        elif 'open youtube' in statement:
            speak("Opening Youtube...")
            webbrowser.open_new_tab("https://www.youtube.com")
            time.sleep(5)

        # Google
        elif 'open google' in statement:
            speak("Opening Google...")
            webbrowser.open_new_tab("https://www.google.com")
            
            time.sleep(5)

        # Gmail
        elif 'open gmail' in statement:
            speak("Opening G mail")
            webbrowser.open_new_tab("gmail.com")
            time.sleep(5)

        # What's app
        elif 'open whats app' or "open what's app" in statement:
            speak("Opening What's app")
            webbrowser.open_new_tab("https://web.whatsapp.com/")
            time.sleep(5)

        # Weather
        elif "weather" in statement:
            api_key="b55f2b6013defa702ae636c1ef9b5c82"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"q="+city_name+"&appid="+api_key
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" City Not Found ")

        # Time
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        # About Siena
        elif 'who are you' in statement:
            speak('I am Siena  your persoanl desktop assistant. I am programmed to do minor tasks')

        # What can Siena do        
        elif 'what can you do' in statement:
            speak('I am Siena programmed to do minor tasks like'
                  'opening youtube, google chrome, gmail,predict time, search wikipedia, predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        # Siena Creator
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            print("I was built by Yathin")
            speak("I was built by Yathin")

        # News
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India')
            time.sleep(5)

        # Search 
        elif 'search'  in statement:
            statement = statement.replace("search","")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        # Ask
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="KV4URY-T8JT2WAQ8J"
            client = wolframalpha.Client('KV4URY-T8JT2WAQ8J')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

         # If you use VS code you can add your path of VS code and remove comments   
         #         
#        elif 'code' in query:
#            codePath="Enter Your VS Code path here"
#            os.startfile(r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        # Shutdown desktop
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)