import time
import os
try:
    os.system('pip install pyttsx3 && pip install speechRecognition && pip install pyaudio && pip install wikipedia && pip install datetime && pip install pyjokes')
except Exception as e:
    os.system('sudo pip install pyttsx3 && sudo pip install speechRecognition && sudo pip install pyaudio && sudo pip install wikipedia && sudo pip install datetime && sudo pip install pyjokes')

try:
    os.system('cls')
except Exception as e:
  os.system('clear')
print("To start run file first.py")
time.sleep(2)
print('Setting up...')
time.sleep(1)
print('All modules installed')
time.sleep(1)
print('Removing setup.py...')
time.sleep(3)
print("thank you for using our assistant")
time.sleep(2)
os.remove('setup.py')
