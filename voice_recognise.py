import speech_recognition as sr
from time import sleep

r = sr.Recognizer()

sample_audio = sr.AudioFile('voices/sample3.wav')

def recogniseText():
    with sr.Microphone() as audio_file:
        print("Say smth...")
        audio_content = r.listen(audio_file)
        
        try:
            query = r.recognize_google(audio_content)
            print(f"you said {query}")
        except:
            print("failed")
        
        return query