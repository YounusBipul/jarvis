# jarvis

jarvis.py is a speech recognition programme that can recognize (using google's speech to text convertion) a few commands and act on it.
* Search on google
* Search on youtube
* Open a text file and write what ever u will tell it
* It can search for a mp3 file in a particular directory and run it

#### Requirements
* SpeechRecognition
* win32com
* pyaudio
* pynput

#### approach
uses keyword matching technique to identify user commands

#### User Guide
* If you want to search something on google:<br/>
  speak : Search on Google (keywords: search, google)<br/>
  jarvis: What do you want me to search on google?<br/>
  speak: {{serch text}}<br/>
  
* If you want to search something on youtube:<br/>
  speak : Search on youtube (keywords: search, youtube)<br/>
  jarvis: What do you want me to search on youtube?<br/>
  speak: {{serch text}}<br/>
  jarvis: should i play the first video ?
  speak: {{ answer }} (keyword: yes/yeah)
  
* If you want to write something on a text file:<br/>
  speak : Open a text file (keywords: open, text, file)<br/>
  jarvis: what should be the file name ?<br/>
  speak: {{file_name}}<br/>
  jarvis: keep speaking the lines you want to write.<br/>
  speak : {{what ever you want}}<br/>
  <br/>
  other command in text file writing<br/>
  comma, period, save it.
  
