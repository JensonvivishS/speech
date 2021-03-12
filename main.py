import logger as logger
import pyttsx3
import datetime
import time

# default configuration
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', 100)
dateService = datetime.datetime.now()

logger.info("Engine Started")

# def speak(message):


lunchTime = "12:30:00"
dinnerTime = "19:00:00"

engine.say(
    'Engine started at ' + dateService.strftime('%B').lower() + ' ' + str(
        dateService.strftime('%Y') + ' ' + dateService.strftime('%X') + ' ' + dateService.strftime('%p'))
)
engine.runAndWait()
while True:
    if datetime.datetime.now().strftime("%X") == "12:00:00":
        engine.say("Hi master")
        engine.say("Good afternoon")
        engine.runAndWait()
        time.sleep(1799)

    if datetime.datetime.now().strftime("%X") == lunchTime:
        engine.say("Hi master")
        engine.say("Sorry to disturb you")
        engine.say("but it is time for lunch")
        engine.runAndWait()
        time.sleep(25199)

    if datetime.datetime.now().strftime("%X") == "17:00:00":
        engine.say("Hi master")
        engine.say("Good evening")
        engine.runAndWait()
        time.sleep(7200)

    if datetime.datetime.now().strftime("%X") == dinnerTime:
        engine.say("Hi master")
        engine.say("Sorry to disturb you")
        engine.say("but it is time for dinner")
        engine.runAndWait()
        time.sleep(25199)

    if str(datetime.datetime.now().strftime("%X")) == "23:10:00":
        print("time reached")
        engine.say("Hi master")
        engine.say("Good night")
        engine.runAndWait()
        time.sleep(7200)
    time.sleep(1)