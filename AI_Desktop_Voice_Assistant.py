'''This is an Artificial Intelligence (AI)-based Desktop Voice Assistant,
named Madhusree's Advanced Respondent Intelligent Assistant, or MARIA.

According to the query of the user, it can perform the following tasks :
1. Wish the user as per the time, dictate the weekday, date and time, and introduce itself
2. Search for anything on Wikipedia
3. Play music from the music directory
4. Open any site on the web, such as Google, YouTube, Stack Overflow, Whatsapp, etc.
5. Open any software on the machine, such as Visual Studio, Dev C++, Adobe Reader, etc.
5. Search for anything on Google
6. Search for any video on YouTube
7. Diplay the weather conditions
8. Search for the exact location of the user in Google Maps
9. Play Stone, Paper and Scissor
'''


import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition, pre-requisite : PyAudio
import wikipedia  # pip install wikipedia
import pyautogui
import webbrowser
import datetime
import calendar
import os
import random as re


'''sapi5 is a Microsoft Speech API,
which is responsible for using the in-built voices provided by Windows
'''
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
'''print(voices)  using this, we can see the different voices available in our computer
( there are three in-built voices in my computer - 1.DAVID, 2.HAZEL, 3.ZIRA )
'''
engine.setProperty('voice',voices[2].id)  # I've used the voice of ZIRA


def speak(audio):
    '''for taking an audio voice as the argument,
    and pronounce that audio using the speaker.
    '''
    engine.say(audio)
    engine.runAndWait()


def get_Date_And_Time():
    '''dictates the weekday, month, date and time.'''
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day

    # creating a list of months
    month_names=['January','February','March','April','May','June','July','August',
                 'September','October','November','December']

    # creating a list ordinal numbers
    ordinal_num=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th',
                 '11th','12th','13th','14th','15th','16th','17th','18th','19th','20th',
                 '21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']

    print(f'Today is {weekday},the {ordinal_num[dayNum - 1]} of {month_names[monthNum - 1]}')
    speak(f'Today is {weekday},the {ordinal_num[dayNum - 1]} of {month_names[monthNum - 1]}')

    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"The time is {strTime}")
    hour=int(datetime.datetime.now().hour)
    if hour==0:
        speak(f"The time is 12 a.m {strTime}")
    else:
        speak(f"The time is {strTime}")


def wishMe():
    '''for wishing the user Good Morning, Good Afternoon, etc.,
    according to the time.
    '''
    hour=int(datetime.datetime.now().hour)  # gives the current hour from 0 to 24
    if hour>=5 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    elif hour>=16 and hour<20:
        print("Good Evening!")
        speak("Good Evening!")
    else:
        print("Good Night!")
        speak("Good Night!")
    get_Date_And_Time()
    speak("I am Madhusree's Advanced Respondent Intelligent Assistant, or MARIA. "
          "Please tell me how may I help you.")


def takeCommand():
    '''it takes microphone input from the user and returns string output.'''
    # creating an object of the Recognizer class that belongs to the speech_recognition module
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # keeping 1.5 second of non-speaking audio before a phrase is considered complete
        r.pause_threshold=1.5
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"You said : {query}")
    except:  # if the recognizer does not understand the speech
        print("Say that again please...")
        return "None"
    return query


def perform_Tasks():
    '''for performing the various tasks, as instructed by the user'''
    while 1:
        query=takeCommand().lower()  # Logic for executing tasks based on query

        # for searching something in Wikipedia:
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia", "")
            # This will return the first 2 sentences from th Wikipedia Search
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        # for playing any music from the music directory:
        elif 'play music' in query:
            '''remember to put double backlashes on Windows, 
            in order to avail IntelliSense for the next directory'''
            music_dir="C:\\Users\\USER\\Music"
            # returns a list all the songs in the music directory
            songs=os.listdir(music_dir)
            songs.remove('desktop.ini')  # removing a dll file, that isn't an audio file
            os.startfile(os.path.join(music_dir, songs[re.randint(0, len(songs) - 1)]))

        # for opening any site on the web:
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        # to open any software of the machine:
        elif 'open pycharm' in query:
            codePath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'open visual studio' in query:
            codePath="C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open dev c plus plus' in query:
            codePath="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
        elif 'open adobe reader' in query:
            codePath="C:\\Program Files (x86)\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(codePath)

        # for searching anything on google:
        elif 'search for' in query and 'on youtube' not in query:
            print("Searching google...")
            query=query.replace("search for","")
            url="https://google.com/search?q="+query
            webbrowser.get().open(url)
            speak(f"Here is what I found for {query} on google")

        # for searching any video on YouTube:
        elif 'search for' in query and 'on youtube' in query:
            print("Searching YouTube...")
            query=query.replace("search for","").replace("on youtube","")
            url="https://www.youtube.com/results?search_query="+query
            webbrowser.get().open(url)
            speak(f"Here is what I found for {query} on YouTube")

        # for knowing the weather of current location:
        elif 'weather' in query:
            print("Searching for the weather of current location...")
            url="https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-" \
                "ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=" \
                "weather&gs_l=psy-ab.3.." \
                "35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475..." \
                "1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10.." \
                "0i71j35i39j35i362i39._" \
                "5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            speak(f"Here is what I found on google")

        # to search for my exact location using Google Maps:
        elif 'location' in query:
            print("Searching for the current location...")
            url="https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("As per Google Maps, in or around here")

        # for playing Stone Paper Scissor
        elif 'play stone paper scissor' in query:
            c_Score=0
            p_Score=0
            moves=['stone','paper','scissor']
            opinion=""
            while opinion!='no':
                print("Choose among stone, paper or scissor")
                speak("Choose among stone, paper or scissor")
                cmove=re.choice(moves)
                pmove=takeCommand().lower()
                print(f"I choose {cmove}")
                speak(f"I choose {cmove}")
                print(f"You chose {pmove}")
                speak(f"You chose {pmove}")
                if cmove=='stone' and pmove=='paper':
                    print("You win")
                    speak("You win")
                    p_Score+=1
                elif cmove=='stone' and pmove=='scissor':
                    print("I win")
                    speak("I win")
                    c_Score+=1
                elif cmove=='scissor' and pmove=='paper':
                    print("I win")
                    speak("I win")
                    c_Score+=1
                elif cmove=='scissor' and pmove=='stone':
                    print("You win")
                    speak("You win")
                    p_Score+=1
                elif cmove=='paper' and pmove=='scissor':
                    print("You win")
                    speak("You win")
                    p_Score+=1
                elif cmove=='paper' and pmove=='stone':
                    print("I win")
                    speak("I win")
                    c_Score+=1
                elif cmove==pmove:
                    print("No score for this shot")
                    speak("No score for this shot")
                speak("Do you want to play again?")
                opinion=takeCommand().lower()
            print("My score is :",c_Score)
            speak(f"My score is : {c_Score}")
            print("Your score is :",p_Score)
            speak(f"Your score is : {p_Score}")
            if c_Score>p_Score:
                print("I win the match")
                speak("I win the match")
            elif p_Score>c_Score:
                print("You win the match")
                speak("You win the match")
            else:
                print("The match is drawn")
                speak("The match is drawn")

        # for quiting the service:
        elif 'thank you' or 'goodbye' or 'bye' or 'quit' or 'exit' in query:
            speak('Thank you. I hope you had a good time.')
            exit()

        # if something is said which does not belong to these operations:
        else:
            print("Sorry! I don't understand that...")


# main :
wishMe()
perform_Tasks()