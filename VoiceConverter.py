import speech_recognition as sr


recognizer = sr.Recognizer()


def get_voice_command():
   with sr.Microphone() as source:
       print("Listening...")
       audio = recognizer.listen(source)
       try:
           command = recognizer.recognize_google(audio)
           print("You said:", command)
           return command.lower()
       except sr.UnknownValueError:
           print("Sorry, I didn't catch that.")
       except sr.RequestError:
           print("Could not request results; check your internet connection.")



