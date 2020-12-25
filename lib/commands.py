import webbrowser
import pyjokes
import json
import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from googleapiclient.discovery import build
from translate import Translator
import wikipedia
import os
try:
    from lib.speak import speak
    from lib.spotify import Spotify
except ImportError:
    from speak import speak
    from spotify import Spotify

BOT_NAME = "Lily"

def query_generate(query):
    raw = query
    symbols = {
        " ":    "+",
        "!":	"%21",
        '"':	"%22",
        "#":	"%23",
        "$":	"%24",
        "%":    "%25",
        "&":	"%26",
        "'":    "%27",
        "(":	"%28",
        ")":	"%29",
        "*":	"%2A",
        "+":	"%2B",
        ",":	"%2C",
        "-":	"%2D",
        ".":	"%2E",
        "/":	"%2F",
        ":":	"%3A",
        ";":	"%3B",
        "<":	"%3C",
        "=":	"%3D",
        ">":	"%3E",
        "?":	"%3F",
        "@":	"%40"
    }

    for item in raw:
        if item in symbols:
            raw = raw.replace(item, symbols[item])
        else:
            continue

    return raw
def open_browser():
    webbrowser.open_new('chrome://newtab')
def open_google():
    webbrowser.open_new('https://google.com')
def open_youtube():
    webbrowser.open_new('https://youtube.com')
def search_google(query):
    speak(f"searching for {query}")
    webbrowser.open_new(f'https://google.com/search?q={query_generate(query)}')
def search_youtube(query):
    speak(f"searching for {query} on youtube")
    webbrowser.open_new(
        f"https://www.youtube.com/results?search_query={query_generate(query)}")
def snippet_google_search(query):
    api_key = 'AIzaSyBEQtV4MdJjatgeKzbrzF3Q5V6uLhSmVK0'
    cse_key = 'a48111b9e3bda48b2'
    resource = build("customsearch", 'v1', developerKey=api_key).cse()
    result = resource.list(q=query, cx=cse_key, num=1).execute()
    return result
def jokes():
    var = pyjokes.get_joke()
    print(f"\033[1;33m{BOT_NAME}: {var}")
    speak(var)
def News():
    key_for_news_api = 'b6b5461c64dd421ea9aaade733043d63'
    main_url = f"https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey={key_for_news_api}"
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]
    results = []
    speak_results = []
    i = 0
    for index, ar in enumerate(article):
        if i >= 5:  # change this number for number of news output
            break
        else:
            results.append(f"{index+1}. {ar['title']}:\n {ar['description']}")
            speak_results.append([index+1, ar["title"], ar["description"]])
            i += 1

    for item in speak_results:
        print(f"{item[0]}. {item[1]} : {item[2]}")
        speak(item[0], item[1], item[2])
def get_cooridinates(addres):
    """return the latitude and longitude of the given city"""
    geolocator = Nominatim(user_agent="cyberhoax")
    location = geolocator.geocode(addres)
    if location != None:
        return (location.latitude, location.longitude)
def get_address(latitude):
    """returns the address of the given town"""
    geolocator = Nominatim(user_agent="cyberhoax")
    location = geolocator.geocode(latitude)
    if location != None:
        return (location.address)
def get_distance(point1, point2):
    return geodesic(point1, point2).km
def translate(fromlang, tolang, text):
    translator = Translator(from_lang=fromlang, to_lang=tolang)
    translation = translator.translate(text)
    return translation
def wiki(query):
    data = wikipedia.summary(query)
    return(data)

def spotify_controls(command):
    controller = Spotify()
    commands = {
        "play_music": controller.play,
        "pause_music": controller.pause,
        "stop_music": controller.stop, 
        "open_playlist":controller.open_playlist,
        "play_from_start":controller.play_from_start,
        "open_spotify": controller.launch
    }

    for item in commands:
        if command == "open_playlist" and command == item:
            all_uri = {
                "mysongs": "spotify:playlist:2bkq3XxKuNDZyXEx62gyjl",
                "the untamed ost": "spotify:playlist:2c2QyDnzJH4pCeUJMogFvm",
                "kpop hits": "spotify:playlist:0Zalm7sVYUtJMJFo9Vahb1"}

            print(f"""====================================
Saved Playlist
====================================""")
            for idx, x in enumerate(all_uri):
                print(f"[{idx+1}] {x}")
            print("[x] exit")                
            print("====================================")
            print("Enter which playlist you want to play or give the uri for the playlist :)")
            while True:
                data = input(">>")
                if data == 'x':
                    exit()
                elif data.isnumeric():
                    kv = {str(index+1):name for index, name in enumerate(all_uri)}
                    try:
                        controller.open_playlist(all_uri[kv[data]])
                        break
                    except IndexError:
                        print("invalid input")
                else:
                    controller.open_playlist(data)
                    break
        elif command == item:
            commands[item]()  
def classify(tag, input_necessory=False):

    tags_command = {
        "browser": open_browser, 
        "google": open_google,
        "youtube": open_youtube,
        "google_search": search_google,
        "google_snippet": snippet_google_search,
        "joke": jokes,
        "news": News,
        "youtube_search" : search_youtube,
        "getdistance": get_distance,
        "getaddress": get_address,
        "getcooridinates": get_cooridinates,
        "translate": translate,
        "wikipedia": wiki,

    }
    if tag in tags_command:
        if input_necessory == False:
            tags_command[tag]()
        elif input_necessory == True:
            while True:
                inp = input(f"{BOT_NAME}(Enter your query): ")
                if inp == 'q':
                    break
                if len(inp) != 0:
                    tags_command[tag](inp)
                    break
                else:
                    print(
                        "\033[1;31mEnter some value or print 'q' to continue chatting with me")


spotify_controls("open_playlist")