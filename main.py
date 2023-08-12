import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
from config import apikey
import subprocess
import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""
def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr = f"Mr. Tiwari: {query}\n Jarvis:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"f{chatStr}"
            },
            {
                "role": "assistant",
                "content": ""
            }
        ],
        # prompt = prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside a try catch block
    say(response["choices"][0]["message"]["content"])
    chatStr += f"{response['choices'][0]['message']['content']}\n"
    return response["choices"][0]["message"]["content"]


def ai(prompt):

    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n ****************** \n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"f{prompt}"
            },
            {
              "role": "assistant",
               "content":""
            }
        ],
            # prompt = prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside a try catch block
    text += response["choices"][0]["message"]["content"]
    #print(text)
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(query):
    speaker.Speak(query)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Error"

if __name__ == '__main__':
    print('Welcome Mr. Tiwari')
    say("Hello I am Jarvis A.I.")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} for you Mr. Tiwari....")
                webbrowser.open(site[1])
            # todo: Add more sites
        if "the time".lower() in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours and {min} minutes")

        elif "open notion".lower() in query.lower():
            subprocess.Popen(r'C:\Users\tiwar\AppData\Local\Programs\Notion\Notion.exe')

        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            say("Goodbye Sir")
            exit()

        elif "reset chat".lower() in query.lower():
            say("Chat has been reset")
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
