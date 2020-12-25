import json
import torch
from lib.model import NeuralNet
from lib.nltk_utilis import bag_of_words, tokenize
from lib.speak import respond, speak
from os import system
from lib.commands import BOT_NAME, classify

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
system('clear')


with open('database/intents.json') as f:
    intents = json.load(f)

FILE = 'database/data.pth'    
data = torch.load(FILE)
input_size = data["input_size"]
output_size = data["output_size"]
hidden_size = data["hidden_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]



model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

print("lets start chatting enter \"quit\" to exit")
speak(f"hi, i am {BOT_NAME}, how can i help you?")
while True:
    sentence = input("\n\033[1;32mYou: ")
    exit_words = ["quit", "exit", "sleep", f"sleep {BOT_NAME}", f"{BOT_NAME} sleep"]
    if sentence in exit_words:
        speak('Thank you, see you again')
        break

    if sentence == "clear":
        speak('clearing our chat!')
        system('clear')

    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    output = model(x)

    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.80:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                if intent["command"] == True and intent["input"] == False:
                    respond(tag, 0)
                    classify(tag)
                elif intent["command"] == True and intent["input"] == True:
                    respond(tag, 0)
                    classify(tag, input_necessory=True)

                else:
                    respond(tag, 0)

    else:
        respond(tag=None ,args=1)

