import pyttsx3
import random
import json
import os

BOT_NAME = "Lily"

try:
    with open("database/intents.json") as f:
        intents = json.load(f)
except FileNotFoundError:
    current_path = os.getcwd()
    rel_path = current_path.replace("lib", "database/intents.json")
    with open(rel_path) as f:
        intents = json.load(f)

def speak(*text: str): # function used to convert text to speech
    
    engine = pyttsx3.init() # use sapi5 here, if on windows
    # engine.setProperty()
    for item in text:
        engine.say(item)
    engine.runAndWait()


def respond(tag=None, args=0):
    for intent in intents["intents"]:
        if args == 0:
            if tag == intent["tag"]:
                if len(intent["responses"]) != 0:
                    response = random.choice(intent['responses'])
                    print(f"\033[1;33m{BOT_NAME}: {response}")
                    speak(response)
        
    if args == 1:
        response = random.choice(intents["dontunderstand"])
        print(f"\033[1;31m{BOT_NAME}: {response}")
        speak(response)
