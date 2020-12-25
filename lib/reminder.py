import datetime
import json
from lib.speak import speak
import time


def set_Reminder(topic, text, time=str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"))):

    with open('reminder.json') as file:
        content = json.load(file)

    
    data = {
        "topic" : topic,
        "text" : text,
        "target_time" : time,
        "current_time": str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M")),
        "task_done": False,
    }
    content['reminders'].append(data)

    with open("reminder.json", 'w') as f:
        json.dump(content, f, indent=4)

def reminder():
    with open('reminder.json') as f:
        data = json.load(f)
    while True:
        for reminder in data["reminders"]:
            current_datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
            time.sleep(1)
            if reminder["target_time"] == current_datetime and reminder["task_done"] == False:
                speak(reminder["topic"], reminder["text"])
                print(reminder["topic"], reminder["text"])
                reminder["task_done"] = True
                with open('reminder.json', 'w') as file:
                    json.dump(data, file, indent=4)

                break
            else:
                continue
# set_Reminder('try', 'this is your reminder', '2020/12/18 14:38')
# reminder()

