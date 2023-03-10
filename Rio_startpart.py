#important library
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import sys
import winsound
import wikipedia
import webbrowser
import pyjokes
import requests
from bs4 import BeautifulSoup
import operator
from tkinter import *
from PIL import ImageTk, Image

#main window code
root = Tk()
root.geometry("750x800+10+20")

root.maxsize(750,800)
root.minsize(750,800)

root['background']="#00FFFF"

root.title("Rio-Desktop Assistance")

logo =Image.open("Rio1.png")
resized=logo.resize((400,260),Image.ANTIALIAS)
logo_1 = ImageTk.PhotoImage(resized)
label = Label(root,image=logo_1)
label.pack(pady=150)

#this function is for chatbot replys
def reply():
    while True:
        query = takecommand()
        wish()
        speak("its Rio , smart voice based fitness chatbot")
        if "hello" in query or "hey" in query:
            speak("hello sir,may i help you with something")

        elif "how are you" in query or "how are you doin" in query:
            speak("i am good sir , what about you")

        elif "i am also fine" in query or "fine" in query:
            speak("that's great to hear from you")

        elif "thanks rio" in query or "nice work" in query:
            speak("it's my pleasure sir.")
            return False

#used to call main fucntion
def work():
    taskexecution()

#chatbot required material
def chatbot_material():
    #wish()
    reply()


#introduction window code
def help():
    help_window = Toplevel(root)
    help_window.title("Intro window")
    #help_window.geometry("750x800")

    #help_window.maxsize(750, 800)
    #help_window.minsize(750, 800)
    help_window['background'] = "#b0c4de"
    label1=Label(help_window,text="!!!!!Here is complete Intro of our project!!!!!",bg = "#b6d4e7", fg = "black", font=('calibre',10, 'bold'),bd=5)
    label1.pack(fill=BOTH,expand=True,padx=25 , pady=20)
    label2 = Label(help_window, text="Rio is the Application which is made to make some of the \n simple. this Application contains one 'smart me' button \n which is used to start start the application.\n you can find list of command in left side of i button\n the after you will one 'go to google' button \n which takes you to google and shows you results\n and then you will have chatbot button which is made\nfor voice based chatting purpose and its fitness \nrelated chatbot so you can get fitness related answer.\n and the final and most importent button is \n 'end me'. by this you can switch off your application.", bg="#b6d4e7", fg="black",font=('calibre',10, 'normal'),bd=95)
    label2.pack(fill=BOTH, expand=True, padx=25, pady=20)

#all code introduse in this fucntion
def info():
    info_window = Toplevel(root)
    info_window.title("Information About Commands")
    #help_window.geometry("750x800")

    #help_window.maxsize(750, 800)
    #help_window.minsize(750, 800)
    info_window['background'] = "#b0c4de"
    label1=Label(info_window,text="!!!!!Here is complete command list present!!!!!",bg = "#b6d4e7", fg = "black", font=('calibre',10, 'bold'),bd=5)
    label1.pack(fill=BOTH,expand=True,padx=25 , pady=20)
    label2 = Label(info_window, text="open notepade or start notepad: use to open notepad\nclose notepad or turnoff notepad: used to close notepad\nopen chrome or start chrome: used to close chrome\nopen movies for me  or show me some movies : to show movies\nopen youtube or go to youtube: to go google\ntell me about weather or what is weather today: it will fatch you current weather\nopne command prompt or open cmd : used to open cmd\nwhere are we or search location : it will fatch you current location\ntake screenshot or screenshot : used to take screenshot\ntell me a joke : it  will tell you joke\nset alarm : used to set alarm\nopen calculator or do some calculation for me : used to do \nsome calculation eg.456+654,55-876 etc.\nopen bmi or bmi : it will open bmi calculator\ndivide bill or bill split : its used to do bill split\nwikipedia : to use this you have to say your topic\n followed by wikipedia to get voice result.\nshutdown the syetem : it will lead to shotdown\nrestart the system : it will leads to restart the system\ngoodbye : it will end the application", bg="#b6d4e7", fg="black",font=('calibre',10, 'normal'),bd=95,justify="left")
    label2.pack(fill=BOTH, expand=True, padx=25, pady=20)

#all buttons
btn1 = Button(root, text = "Start Me", command = lambda:work(),width=25,height=2,activebackground="red",activeforeground="black",bd="2px",font=("Times_New_Roman",8))
btn1.place(x=250,y=395)

start_info = PhotoImage(file="download.png",height=21,width=21)
img = Button(root,image=start_info,borderwidth=0 ,command=lambda :info(),activebackground="red",activeforeground="black",bd="2px",font=("Times_New_Roman",8))
img.place(x=495,y=405)

btn2 = Button(root, text = "End ME.", command = lambda :sys.exit(),width=15,height=1,activebackground="Blue",activeforeground="black",bd="2px",font=("Times_New_Roman",8))
btn2.place(x=25,y=65)

btn3 = Button(root, text = "Help!!!", command = lambda :help(),width=15,height=1,activebackground="red",activeforeground="black",bd="2px",font=("Times_New_Roman",8))
btn3.place(x=570,y=65)

btn4 = Button(root, text = "Search on Google", command = lambda :Search(),width=15,height=1,activebackground="red",activeforeground="black",bd="2px",font=("Times_New_Roman",8))
btn4.place(x=300,y=480)

btn10 = Button(root, text = "Voice based\nChatbot", command = lambda:chatbot(),width=25,height=2,activebackground="red",activeforeground="black",bd="2px",font=("Times_New_Roman",8))
btn10.place(x=250,y=580)

output = Text(root, height=1,width=16,bg="light cyan")
output.place(x=276,y=520)

#chatbot window code
def chatbot():
    bot = Toplevel()
    bot.title("Voice-Based ChatBot")
    bot.geometry("450x400")

    bot.maxsize(450, 400)
    bot.minsize(450, 400)

    bot['background'] = "#8ad4eb"

    label1 = Label(bot, text="this is Fitness chatbot which takes \nvoice input and gives voice output\n And to End conversation say 'bye'", bg="#b6d4e7",
                   fg="black", font=('calibre', 10, 'bold'), bd=5)
    label1.pack(fill=BOTH, expand=True, padx=22, pady=25)

    btn12 = Button(bot, text="Start ", command=lambda:chatbot_material() , width=25, height=2, activebackground="red",
                  activeforeground="black", bd="2px", font=("Times_New_Roman", 8))
    btn12.place(x=115, y=250)

#setting up voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#use to speak out sentance
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#use to take command
def  takecommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout=5,phrase_time_limit=8)
    except KeyboardInterrupt:
        taskexecution()
    except sr.WaitTimeoutError as k:
        print("time out")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("sorry for the glitch,please try again")
        return "none"
    except sr.WaitTimeoutError as k:
        print("time out")
    query=query.lower()
    return query

def prin():
    output.insert(END, "Showing Result...")

#used to search command on google
def Search():
    output.delete("1.0", "end")
    prin()
    speak("Tell me what should i search on google")
    search = takecommand()
    webbrowser.open(f"{search}")


#this fuction is used to calculate bmi
def calculate_bmi():
    try:
        speak("can you please tell me your weight.")
        weight = takecommand()
        kg = int(weight)
        speak("can you please tell me you height")
        meter = takecommand()
        m = int(meter) / 100
        bmi = kg / (m * m)
        bmi = round(bmi, 1)
        bmi_index(bmi)
    except TimeoutError:
        calculate_bmi()

#this fucntion is for to show output of bmi
def bmi_index(bmi):
    if bmi < 18.5:
        speak(f"{bmi} is Underweight")
    elif (bmi > 18.5) and (bmi < 24.9):
        speak(f"{bmi} is Normal")
    elif (bmi > 24.9) and (bmi < 29.9):
        speak(f"{bmi} is Overweight")
    elif (bmi > 29.9):
        speak(f"{bmi} is Obesity")

#this fucntion is for do bills splits
def bill_split():
    try:
        speak("ohk then tell me how many no of people you are ")
        people = takecommand()
        p1 = int(people)
        speak("tell me the amount of bill")
    except Exception as e:
        print(e)
        speak("sorry sir, i didn't get it , can you repeat again")
        bill_split()
    try:
        amount = takecommand()
        amt = int(amount)
    except Exception as e:
        print(e)
        speak("sorry sir, i didn't get it , can you repeat again")
        bill_split()
    value = amt / p1
    value_1 = round(value,2)
    speak(f"so for each person you have to pay {value_1}")

#this is for to convert calsius to fahrenheit
def caltofah():
    speak("tell me your celsius value")
    cel1 = takecommand()
    fah1 = (cel1 * 1.8) + 32
    result1 = round(fah1,2)
    speak(f"your answer in fahrenheit is {result1}")

#this is for to convert fahrenheit to calsius
def fahtocal():
    speak("tell me your Fahrenheit value")
    fah1 = takecommand()
    cal1 = (fah1 - 32) / 1.8
    result1 = round(cal1,2)
    speak(f"your answer in calsius is {result1}")

#this is for with fucntion
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour < 16:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")

#this is for setting up alarm
def alarm(Timing):
    try:
        altime = str(datetime.datetime.now().strptime(Timing,"%H:%M %p"))

        altime = altime[11:-3]
        print(altime)
        horeal = altime[:2]
        horeal = int(horeal)
        mireal = altime[3:5]
        mireal = int(mireal)
        print(f"done, alarm is set for {Timing}")

        while True:
            if horeal==datetime.datetime.now().hour:
                if mireal==datetime.datetime.now().minute:
                    print("alarm is running")
                    winsound.PlaySound("abc",winsound.SND_LOOP)
                    #Winsound.Beep(1, 10)

                elif mireal<datetime.datetime.now().minute:
                    break

    except Exception as e:
        speak("Try again")


#this will fatch weather
def weather():
    search = "temparature in mumbai"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"current {search} is {temp}")


def terminate(ProcessName):
    os.system('taskkill /IM "' + ProcessName + '" /F')

#def ip_address():
#    ip = get("https://api.ipify.org").text
#    speak(f"your IP address is {ip}")

#this is main fucntion which contain most of the features
def taskexecution():
    #wish()

    query = takecommand()
    if "open notepad" in query or "start notepad" in query:
        npath = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(npath)

    elif "close notepad" in query or "trun off notepad" in query:
        speak("okay sir, closing notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "open word" in query or "start word" in query:
        npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word"
        os.startfile(npath)

    elif "open chrome" in query or "start chrome" in query:
        npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\google chrome"
        os.startfile(npath)


    elif "open movies for me" in query or "show me some movies" in query:
        npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Popcorn Time\\popcorn time"
        os.startfile(npath)

    elif "open command prompt" in query or "open cmd" in query or "go to cmd" in query or "go to command prompt" in query:
        os.system("start cmd")

    elif "open youtube" in query or "youtube" in query or "start youtube" in query:
        webbrowser.open("www.youtube.com")

    elif "tell me about weather" in query or "what's  weather" in query or "what is weather today" in query:
        weather()


    elif "open google" in query or "go to google" in query or "start google" in query:
        speak("sir, what do you want me to search on google")
        search = takecommand().lower()
        webbrowser.open(f"{search}")

    elif "wikipedia" in query:
        speak("searching on wikipedia....")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        speak(results)
        print(results)

    elif "where are we" in query or "where we are" in query or "search location" in query:
        speak("wait sir , let me check")
        try:
            r = requests.get('https://get.geojs.io/')

            ip_requests = requests.get('https://get.geojs.io/v1/ip.json')
            ipAdd = ip_requests.json()['ip']
            print(ipAdd)

            url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
            geo_request = requests.get(url)
            geo_data = geo_request.json()

            # print(geo_data['city'])
            # print(geo_data['region'])
            # print(geo_data['country'])

            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            speak(f"sir we are in mumbai city of maharashtra which is in {country} country")

        except Exception as e:
            speak("sorry sir ,not able to find the location")
            pass
        except KeyboardInterrupt as e:
            pass


    elif "take screenshot" in query or "screenshot" in query:
        speak("sir,please tell me the name for screenshot file")
        name = takecommand().lower()
        speak('please hold the screen for few seconds, i am taking screenshot')
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f'{name}.png')
        speak('i am done with the screenshot,you ready for the next commands')


    elif "open calculator" in query or "do calculation for me" in query:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("tell me what i have to calculate")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            pass

        try:
            def get_operator_fn(op):
                return {
                    "+": operator.add,
                    "-": operator.sub,
                    "x": operator.mul,
                    "/": operator.truediv,
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)

            # speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
        except Exception as e:
            print(e)
            speak("sorry sir, i didn't get it , can you repeat again")
        except KeyboardInterrupt:
            pass


    elif "bmi" in query or "open bmi calculator" in query or "open bmi" in query:
        calculate_bmi()

    elif "convert Celsius to Fahrenheit" in query:
        temp1 = takecommand().lower()
        if temp1 == "Celsius":
            caltofah()


    elif "divide bill " in query or "bill split" in query:
        bill_split()

    # elif "ip address" in query or "tell me ip adress":
    #   ip_address()

    elif "tell me a joke" in query :
        joke = pyjokes.get_joke(language="en", category="neutral")
        speak(joke)

    elif "set alarm" in query:
        try:
            speak("sir, please tell me time to set alarm")
            tt = takecommand()
            # tt = tt.replace("set alarm to","")
            tt = tt.replace(".", "")
            tt = tt.upper()
            alarm(tt)
        except KeyboardInterrupt:
            pass


    elif "shutdown the system" in query:
        os.system("shutdown /s /t 5")

    elif "restart the system" in query:
        os.system("shutdown /r /t 5")

    elif "activate sleep mode" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


    elif "goodbye" in query:
        speak("thanks for using me, have a good day ahead")
        sys.exit()


root.mainloop()

#if __name__ == '__main__':
    #while True:
    #    taskexecution()