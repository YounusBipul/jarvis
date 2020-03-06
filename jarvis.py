"""
Requirements:
1. SpeechRecognition
2. win32com
3. pyaudio
4. pynput
"""
#imports
import speech_recognition as sr
from win32com.client import Dispatch
import webbrowser
from pynput.keyboard import Key, Controller
import time
import os

#search keywords
bot_name="bro"
google_search_keywords=['search','Google']
youtube_search_keywords=['search','YouTube']
songs_keywords=['song','play']
open_textfile_keywords=['open','text','file']

#essential settings
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
music_dir= 'E:/Music/'
recog= sr.Recognizer()
text=""
voice= Dispatch("SAPI.Spvoice")
first_time=True
keyboard = Controller()

#speech to text converter
def get_text():
    with sr.Microphone() as source:
        print("speak")
        audio= recog.listen(source)
        try:
            text= recog.recognize_google(audio)
            print("you said: {}", format(text))
            return text
        except:
            print("Did not understand, Say again")
            voice.speak("couldn't understand. can you please repeat ?")
            return get_text()

#matching command keywords
def test_keywords(command,keywords):
    flag=True
    for keyword in keywords:
        if(keyword not in command):
            flag=False
            return flag
    return flag

#writing on text files
def typechars(c):
    time.sleep(0.2)
    keyboard.press(c)
    keyboard.release(c)
    

while(True):
    text = str(get_text())
    if(first_time==True):
        first_time=False
        voice.speak("please wait for a while, initializing drivers, fetching updates and done! we are ready sir.")

    if(test_keywords(text,google_search_keywords)):
        voice.speak("What do you want me to search on google")
        srch= get_text()
        srch= srch.replace(' ','+')
        voice.speak("here you go")
        webbrowser.get(chrome_path).open("https://www.google.com/search?q="+str(srch))
    elif(test_keywords(text,youtube_search_keywords)):
        voice.speak("What do you want me to search on youtube")
        srch= get_text()
        srch= srch.replace(' ','+')
        voice.speak("here you go")
        webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query="+str(srch))
        time.sleep(5)
        voice.speak("should i play the first video ?")
        line=get_text()
        if("yes" in line or "yeah" in line):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
  
    elif(test_keywords(text,songs_keywords)):
        voice.speak("Yeah sure. Which song do you want to listen?")
        song_name= get_text()
        voice.speak("enjoy the song")
        #os.startfile(music_dir +"*"+ song_name + "*.mp3")
        for file in os.listdir(music_dir):
            if song_name in file:
                #print(os.path.join(music_dir, file))
                print(music_dir+file)
                os.startfile(music_dir+file)
                break
    elif(test_keywords(text,open_textfile_keywords)):
        voice.speak("what should be the file name ?")
        filename= get_text()
        f=open(filename+".txt",'w+')
        f.close()
        os.startfile(filename+".txt")
        voice.speak("keep speaking the lines you want to write.")
        while(True):
            line= get_text()
            if(line=="period"):
                line=". "
            elif(line=="comma"):
                line=", "
            elif(line==""):
                pass
            elif(line=="save it"):
                keyboard.press(Key.ctrl)
                keyboard.press("s")
                keyboard.release(Key.ctrl)
                keyboard.release("s")
                # os.close(filename+".txt")
                break
            else:
                line=line+" "
            for i in line:
                typechars(i)
    elif("thank you" in text or "thanks" in text):
        voice.speak("just an absolute pleasure")
    if (test_keywords(text, bot_name)):
        voice.speak("at your service, sir")