import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse
import subprocess


def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Please Wait...")
        speak("Please Wait...")
        text1 = recognizer.recognize_google(audio)
        text = text1.lower()
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        speak("Sorry, I couldn't understand.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        speak(f"Error with the speech recognition service; {e}")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def greet():
    print("Hello, I am Jarvis. How can I assist you today?")
    return "Hello, I am Jarvis. How can I assist you today?"

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    print("Current time is : "+ str(current_time))
    return f"The current time is {current_time}"

def search_google(query):
    search_query = urllib.parse.quote(query)
    search_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(search_url)
def open_application(application_name):
    if "chrome" in application_name.lower():
        # On Windows, use the full path to the Chrome executable
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        try:
            subprocess.Popen([chrome_path])
            print("Opening Chrome")
            speak("Opening Chrome")
        except Exception as e:
            print(f"Error opening Chrome: {e}")
            speak(f"Error opening Chrome: {e}")
    else:
        try:
            subprocess.Popen([application_name], shell=True)
            print(f"Opening {application_name}")
            op = f"Opening {application_name}"
            speak(op)
        except Exception as e:
            print(f"Error opening {application_name}: {e}")
            qu2 = f"Error opening {application_name}"
            speak(qu2)

def main():
    speak(greet())

    while True:
        command = recognize_speech()

        if command:
            if "time" in command:
                time_response = get_time()
                speak(time_response)
            elif "search" in command:
                search_query = command.replace("search for", "").strip()
                if search_query:
                    search_google(search_query)
                    print(f"Searching Google for {search_query}")
                    qu1 = f"Searching Google for {search_query}"
                    speak(qu1)
                else:
                    qu = "Please provide a search query."
                    speak(qu)
            elif "open" in command:
                app_name = command.replace("open", "").strip()
                if app_name:
                    open_application(app_name)
                else:
                    app = "Please provide an application name."
                    speak(app)
            elif "who are you" in command:
                print("I am Jarvis,Made by Rony")
                speak("I am Jarvis,Made by Rony")
            elif "who made you" in command:
                print("Rony made me.")
                speak("Rony made me.")
            elif "who is" in command:
                search_query = command.replace("who is", "").strip()
                if search_query:
                    search_google(search_query)
                    print(f"Searching Google for {search_query}")
                    qu1 = f"Searching Google for {search_query}"
                    speak(qu1)
                else:
                    qu = "I didn't understand."
                    speak(qu)
            elif "jarvis" in command:
                print("Yes!I am here.You can ask me anything.")
                speak("Yes!I am here.You can ask me anything.")
            elif "exit" in command:
                print("Exiting Program.Goodbye!")
                speak("Exiting Program,Goodbye!")
                break
            else:
                print("Sorry, I don't understand that command.")
                spk = "Sorry, I don't understand that command."
                speak(spk)

if __name__ == "__main__":
    main()
