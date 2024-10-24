import speech_recognition as sr
import webbrowser
import pyttsx3
import sphinx


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":  
    speak("Hey Samy, your senorita is initializing.")
    while True:
        #listen for the wake word senorita
        #contain audio from the microphpne
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            audio = r.listen(source)

        

        #recognize speech using sphinx
        try:
            command = r.recognize_sphinx(audio)
            print(command)

        except sr.UnknownValueError:
            print("sphinx could not understand audio")

        except sr.RequestError as e:
            print("Sphinx error:{0}".format(e))
                          


