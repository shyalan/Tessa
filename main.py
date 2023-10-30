import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
from datetime import datetime
import arrow
import os # to remove created audio files
import wolframalpha
import urllib.request
import urllib.parse
import re
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

class person:
    name = 'Shyalan'
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Tessa: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):

    # start
    if there_exists(["tessa","tesa","tissa","kaisa","chacha"]):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # greeting
    if there_exists(['hey','hi','hello','hay']):
        speak("Yes sir, what can i do for you")

    # greeting morning
    if there_exists(["morning","good morning","bad morning","monin","mornin"]):
        greetingsmorning = [f"Good morning {person_obj.name}", f"good morning sir"]
        greetmorning = greetingsmorning[random.randint(0,len(greetingsmorning)-1)]
        speak(greetmorning)
        speak("Welcome back sir")
        speak("Servers are now online")
    
    # greeting afternoon
    if there_exists(["afternoon","good afternoon","bad afternoon","afternoun","noon"]):
        greetingsafternoon = [f"Good afternoon {person_obj.name}", f"good afternoon sir"]
        greetafternoon = greetingsafternoon[random.randint(0,len(greetingsafternoon)-1)]
        speak(greetmafternoon)
    
    # greeting evening
    if there_exists(["evening","good evening","bad evening","ening","evenin","eve"]):
        greetingsevening = [f"Good evening {person_obj.name}", f"good evening sir"]
        greetevening = greetingsevening[random.randint(0,len(greetingsevening)-1)]
        speak(greetevening)

    # greeting goodnight
    if there_exists(["good night","bad night"]):
        greetingsnight = [f"Good night {person_obj.name}", f"good night sir"]
        greetnight = greetingsnight[random.randint(0,len(greetingsnight)-1)]
        speak(greetnight)
        speak("preparing to shutdown server")
        speak("Server's are offline now")
        speak("See you later")
        exit()

    # end
    if there_exists(["end program","quit","shutdown","server offline","power off","n program","good bye","goodbye","break program"]):
        endbyes = [f"good bye {person_obj.name}", f"good bye sir"]
        endbye = endbyes[random.randint(0,len(endbyes)-1)]
        speak(endbye)
        speak("See you later")
        exit()

    # name
    if there_exists(["what is your name","what's your name","tell me your name","your name","you name","who are you","whoryou","whoareyou","who r you","what are you","who are you","what in the world are you"]):
        if person_obj.name:
            speak("my name's Tessa")
            speak("I am Shalan's personal assistance")
            speak("Say, 'about me' if you Would like to see what i can do?")      
        else:
            speak("my name is Tessa. what's your name?")

    if there_exists(["about me","about"]):
        speak("I'm an Interactive AI based Virtual Assistant")
        speak("I can search on google for you, play music, tell you the time and the date, greet you whenever you greet me, and many more")
    if there_exists(["no"]):
        speak("thats mean well okay sir")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object
        speak("I am Shalan's personal assistance")
        speak("Would you like to see what i can do")
        if there_exists(["yes"]):
            speak("I'm an Interactive AI based Virtual Assistant")
            speak("I can search on google for you, play music, tell you the time and the date, greet you whenever you greet me and many more")
        else:
            speak("thats mean well okay sir")

    # greeting
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # time
    if there_exists(["what's the time","tell me the time","what time is it","time","what is the time","show me the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # date
    if there_exists(["what's the day","tell me the day","what day is it","what's today's date","whats todays date","huts tudays dait","what is the day","what day is it today","today's date","todays date","what is todays date","whats todays date","whats the date today","date","todays date","tell me todays date"]):
        date = arrow.now().format('YYYY-MM-DD')
        speak(f"Today's date is")
        speak(date)

    # worldwideweb
    if there_exists(["search the world wide web for"]):
        search_term = voice_data.split("for")[-1]
        url = f"www.{search_term}.com"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on the world wide web')

    # search google
    if there_exists(["search google for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    # Stupid
    if there_exists(["stupid","fool","useless","idiot"]):
        speak("Excuse me, stop calling me that")

    #creator
    if there_exists(["who created you","who's your creator","who made you","creator","who owns you"]):
        speak("I was made by Shalan")
    
    #launch date
    if there_exists(["when were you made","date of birth","date of launch","What is your launch date","launch date","creation date","date made"]):
        speak("I was first launched on the 24th of January")

    # calculate
    if there_exists(["calculate","cal"]):
        app_id = "WOLFRAMALPHA_APP_ID"
        client = wolframalpha.Client(app_id) 

        indx = there_exists.lower().split().index('calculate') 
        query = there_exists.split()[indx + 1:] 
        res = client.query(' '.join(query)) 
        answer = there_exists(res.results).text 
        speaks("The answer is " + answer) 

    #joke
    if there_exists(["tell me a joke","make me laugh","joke","jokes","make me laugh","tell me another joke"]):
        speak(pyjokes.get_joke())
    
    #relationship
    if there_exists(["would you like to go on a date with me","are you single","married","nari","are you married","are you nari","relationship"]):
        dates = [f"I am in a relationship with wifi sir", f"sorry, I have a headache"]
        date = dates[random.randint(0,len(dates)-1)]
        speak(date)

    #run diagnosis
    if there_exists(["run diagnosis","diagnosis"]):
        speak("running diagnosis now")
        speak("shutting down server 1 and 2, server 1 is now offline, shutting down server 3, server 2 and 3 is now offline")
        speak("diagnosis complete")
        speak("server 1 2 and 3 are now online")
        speak("system are now initialising")
        speak("I found no errors in my system sir")

    #system reboot
    if there_exists(["reboot","system reboot"]):
        speak("reboot initiated")
        speak("reboot unsuccessful, server 2 is offline now, would you like me to run diagnosis and fix system failure")
    
    #fix system
    if there_exists(["fix system error","system error","fix","system failure","fix system"]):
        speak("running diagnosis now")
        speak("shutting down server 1 and 2, server 1 is now offline, shutting down server 3, server 2 and 3 is now offline")
        speak("diagnosis complete")
        speak("server 1 2 and 3 are now online")
        speak("all systems are functioning")
        speak("welcome back sir")
    
    #Calling u sir
    if there_exists(["shyalan","shalan","shaalan","shylan"]):
        speak("Sir there's someone calling you!")

time.sleep(1)
print("Tessa")
person_obj = person()
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond
