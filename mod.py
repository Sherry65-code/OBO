import pyttsx3
import speech_recognition as sr
import os
import subprocess
import webbrowser
import datetime
import sys
import wikipedia
import time
import pyjokes
# Variable initilizations

ans = ''

# End
def give_ans(query):
    query = query.lower()
    if ("hello" in query or 'hi' in query):
        ans = "Hi, this is obo"
    elif (query == "put my class"):
        ans = "Ok, starting your class"
        subprocess.Popen('C:\\Users\\spara\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
        user_start_class()
    elif (query == 'bye'):
        ans = "Bye for now"
        time.sleep(3)
        sys.exit()
    elif ("how are you" in query):
        ans = "I am fine. but thank you for asking me in such tempestuous times"
    elif ("what is" in query and "your" in query and "name" in query):
        ans = "i am obo. objectification binary ozoner"
    elif ("search" in query and "google" in query):
        ans = "searching"
        webbrowser.open(f"https://www.google.com/search?q={query.replace('google','').replace('search','')}")
    elif ("search" in query and "wiki" in query):
        ans = wikipedia.summary(f"{query.replace('for','').replace('wikipedia','').replace('wiki','').replace('search','')}" , sentences=2)
    elif ("what" in query and "time" in query):
        ans = f"time is {datetime.datetime.now().hour} {datetime.datetime.now().minute}"
    elif (query == "open settings"):
        try:
            os.system("control panel")
            ans = "Opening settings"
        except Exception as e:
            ans = "Sorry could not open settings"
    elif ('play' in query and 'favourite' in query and 'song' in query):
        ans = "Playing your favourite song"
        webbrowser.open('https://www.youtube.com/watch?v=0I647GU3Jsc')
    elif (query == "open youtube"):
        ans = "opening youtube"
        webbrowser.open('https://youtube.com')
    elif (query == "open edge"):
        ans = "Opening edge"
        webbrowser.open('https://bing.com')
    elif (query == "what can you do"):
        ans = "if you use me, you will come to know"
    elif ("donkey" in query):
        ans = "no bad words"
    elif ("you" in query and "are" in query and "good" in query):
        ans = "thank you"
    elif (query == "open zoom"):
        ans = "opening zoom"
        subprocess.Popen('C:\\Users\\spara\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    elif ('joke' in query and 'tell' in query):
        ans = f"{pyjokes.get_joke(language='en' , category='neutral')}"
    elif (query == "shutdown the computer"):
        ans = "Shutting down"
        os.system("shutdown /s")
    else:
        ans = "sorry, i cannot help with that"
    return ans

def clear_slate():
    try:
        os.system('cls')
    except Exception as e:
        os.system('clear')

engine = pyttsx3.init()
def speak(texttospeak):
    engine.say(texttospeak)
    engine.runAndWait()

def hear(dev_inx):
    r = sr.Recognizer()
    with sr.Microphone(device_index=dev_inx) as source:
        audio = r.listen(source)
    query = r.recognize_google(audio)
    return query


def user_start_class():
    time = datetime.datetime.now()
    cur_month = int(time.month)
    if (cur_month == 1):
        name = "JAN"
    elif (cur_month == 2):
        name = "FEB"
    elif (cur_month == 3):
        name = "MAR"
    elif (cur_month == 4):
        name = "APR"
    elif (cur_month == 5):
        name = "MAY"
    elif (cur_month == 6):
        name = "JUN"
    elif (cur_month == 7):
        name = "JUL"
    elif (cur_month == 8):
        name = "AUG"
    elif (cur_month == 9):
        name = "SEP"
    elif (cur_month == 10):
        name = "OCT"
    elif (cur_month == 11):
        name = "NOV"
    elif (cur_month == 12):
        name = "DEC"
    webbrowser.open(f"https://schoolmitra.com/images/bulletins/73/CLS_IX_{time.day}_{name}.pdf")
