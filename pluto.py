import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition
import wikipedia   #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import os
import pyautogui #pip install pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha #pip install wolframalpha
import time
import winshell #pip install winshell
import operator


engine = pyttsx3.init()
wolframalpha_app_id = 'GTX5Y5-P4K8GPQUQ3'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  #for 12 hours 
    speak("The Current time is")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Rohan")
    time_()
    date_()

    #greetings

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("good afternoon Sir")
    elif hour>18 and hour<24:
        speak("good evening Sir")
    else:
        speak("good night Sir")

    speak("Pluto here Please tell me what can i do for you! ")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    
    except Exception as e:
        print(e)
        print("Please Say that again....")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #for this function you must enable low security in your gmail which you are going to use as sender


    server.login('rohansharma5829@gmail.com','rohan2001#')
    server.sendmail('rohansharma5829@gmail.com',to,content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/ACER/Desktop/python/ss/screenshot.png')



def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)


def joke():
    speak(pyjokes.get_joke())


def Introduction():
    speak("I am PLUTO 1.0 , Personal AI assistant , "
    "I am created by ROHAN , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life easier , "
    "Where you just have to command me , and I will do it for you , ")

def Creator():
    speak("ROHAN is an extra-ordinary person ,"
    "He has a passion for Web development, Artificial Intelligence and Machine Learning , Python"
    "He is very co-operative ,"
    "If you are facing any problem regarding the 'Pluto', He will be glad to help you ")


if __name__ == "__main__":
    wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:   
            time_()
        
        
        elif 'date' in query:
            date_()

        
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")

        
        
        elif 'wikipedia' in query:
            speak("Searching....")
            query=query.replace('wikipedia','')
            result= wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)

        
        
        elif 'send email' in query:
            try:
                speak("What should I say ?")
                content=TakeCommand()
                # provide recievers email address

                speak("Who is the reciver....")
                reciver=input("Enter Reciver's Email:")
                to = reciver
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')
            
            except Exception as e:
                print(e)
                speak("Unable to send Email...")
                
        
        
        
        elif 'search in chrome' in query:
            speak('What should I search')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            

        
        
        elif 'search youtube' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak("Here we go to youtube!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        
        
        elif 'search google' in query:  
            speak('What should I search')
            search_Term = TakeCommand().lower()
            speak("Searching...")
            wb.open('https://www.google.com/search?q='+search_Term)


        
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")



        elif "why you came to this world" in query:
            speak("Thanks to MAK. further it is a secret")

        
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled") 
 
        
        
        elif 'cpu' in query:
            cpu()

        
        
        elif 'joke' in query:
            joke()

        
        
        elif 'go offline' in query:
            speak('Going Offline Sir!')
            quit()


        
        
        elif 'word' in query:
            speak('Opening MS Word...')
            ms_word = r'C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(ms_word)

        
        
        elif 'write a note' in query:
            speak("What should I note,Sir")
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("Sir Should I include Date and Time?")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking notes,SIR!')
            else:
                file.write(notes)

        
        
        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        
        
        elif 'screenshot' in query:
            screenshot()

        
        
        elif 'play music' in query:
            songs_dir = 'C:/Users/ACER/Music'       
            music = os.listdir(songs_dir)
            speak('What should i play?')
            speak('Select a Number...')
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak('I could not understand you. Please Try Again,')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number','')) 
            elif 'random' or 'you choose' in ans: 
                no = random.randint(1,100)
                os.startfile(os.path.join(songs_dir,music[no]))
            
        
        
        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        
        
        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())

        
        
        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d408f554a47549dd8bfd129c899aa7dd")
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top tech headlines')
                print('=============Tech News=============')
                for item in data['articles']:
                    print(str(i)+'.'+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+= 1

            except Exception as e:
                print(str(e)) 

        
        #To locate some place 
        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)


        
        #To calculate 
        elif 'calculate' in query:
            
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        
        
        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No Results")

        

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            speak("The time is over now and i am listening")
            print(a)


        
        elif 'log out' in query:
            os.system("shutdown -1")
        
        
        elif 'restart' in query:
             os.system("shutdown /r /t 1")
             
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")




     





        

        

        

        


