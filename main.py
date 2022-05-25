import pyttsx3
import datetime
import pyaudio
import webbrowser as wb
import wikipedia
import speech_recognition as sr
import os
import pyautogui
import psutil
import pyjokes
import keyboard


engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)#voice[0].id for male vocie
newVoiceRate = 200
engine.setProperty('rate',newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time = datetime.datetime.now().strftime('%H:%M:%S')
    speak("the current time is")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
    
def screenshot():
    img = pyautogui.screenshot()
    img.show()
    img.save("E:\pics")
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
    
def jokes():
    speak(pyjokes.get_joke())
    
    
def  wishme():
    speak("welcome back")
    #time()
    #date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <=12:
        speak("Good morning")
    elif hour>=12 and hour <=15:
        speak("good afternoon")
    elif hour >=15 and hour <=24:
        speak("good evening")
    else :
        speak("good night")
        
   
    speak("Any help")
    
def takecommand():
    r =sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google (audio)
        print(query)
        
    except Exception as e:
        print(e)
        speak("Say that again please...")
        
        return "None"
    return query
        
if __name__ == "__main__":
    
    wishme()
    
    while True:
        query =takecommand().lower()
        print(query)
        
        if "time" in query:
            time()
            
        elif "date" in query:
            date()
            
        elif "exit" in query:
            quit()
        
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 1)
            speak(result)
               
        elif "browser" in query:
            speak("what should i search?")
            search = takecommand().lower()
            wb.open_new_tab(search + ".com")
            
        elif "logout" in query:
            os.system("shutdown - l")
            
        elif "shutdown" in query:
            os.system("shutdown /s /t l")
            
        elif "restart" in query:
            os.system("shutdown /r /t l")
            
        elif "remember" in query:
            speak("what should i rember?")
            data = takecommand()
            speak("you said me to remember that" + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
            
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("you said me to remember that" + remember.read())
            
        elif "screenshot" in query:
            screenshot()
            speak("took screenshot!")
            
        elif "cpu" in query:
            cpu()
            
        elif "joke" in query:
            jokes()
            
        
            
