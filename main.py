import pyttsx3
import os
import speech_recognition
import subprocess
import wikipedia
import google.generativeai as genai



class voiceEngin:
    def __init__(self):
        self.engin = pyttsx3.init()
    
        self.engin.setProperty('rate', 160)
    
    def say(self, words:str):
        self.engin.say(words)
        self.engin.runAndWait()

class listen:
    def __init__(self):
        self.recognizer= speech_recognition.Recognizer()
        self.miduem = speech_recognition.Microphone()
        self.voiceEngin = voiceEngin()
    def listen_and_recognize(self):

        with self.miduem as source:
            self.voiceEngin.say("listing sir")
            audio = self.recognizer.listen(source)
        try:
            recognized_text = self.recognizer.recognize_sphinx(audio)
            print("The user input is:", recognized_text)
        except speech_recognition.UnknownValueError:
            print("Could not understand!")
        except speech_recognition.RequestError as e:
            print("Error:", e)


class taskManager():
    def __init__(self):
        self.applicationPath = {'chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                                'firefox': r"C:\Program Files\Mozilla Firefox\firefox.exe",
                                'vartualbox': r'"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"' }
        self.voiceEngin = voiceEngin()
    def start_applications(self, appname):
        if appname in self.applicationPath.keys:
            path = self.applicationPath.get(appname)
            process = subprocess.Popen(path)
            return process
    def summary(self, term):
        information = wikipedia.summary(term, sentences=1)
        print(information)
        self.voiceEngin.say(information)
        
genai.configure(api_key="API-KEY")


class Ai:
    def __init__(self):
        self.generation_config = {
                                    "temperature": 0.9,
                                    "top_p": 1,
                                    "top_k": 0,
                                    "max_output_tokens": 100,
                                    "response_mime_type": "text/plain",
                                    }
        self.model = genai.GenerativeModel(
                                            model_name="gemini-1.0-pro",
                                            generation_config=self.generation_config,

                                            )
        self.chat_session = self.model.start_chat(
                            history=[]
                                )
        self.voiceEngin = voiceEngin()
        
    def getresponse(self, term):
        response = self.chat_session.send_message(term)    
        print(response)
        self.voiceEngin.say(f"yes sir the term {term} To my understanding is ")
        self.voiceEngin.say(response.text)
        return response
    
jarvis = Ai()
jarvis.getresponse("you question here ")