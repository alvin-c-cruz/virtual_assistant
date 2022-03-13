import speech_recognition as sr
import sounddevice as sd
import os
import wavio
import pyttsx3

from commands import command

fps = 44100
duration = 3

print("Recognition...")

audioF = 'output.wav'

rec = sr.Recognizer()
engine = pyttsx3.init()
engine.say('I am Jarvis')
engine.say('What can I do for you?')
engine.runAndWait()


def say(text):
    engine.say(text)
    engine.runAndWait()


loop = True
while loop:
    recording = sd.rec(duration * fps, samplerate=fps, channels=2)
    sd.wait()
    wavio.write(audioF, recording, fps, sampwidth=2)
    with sr.AudioFile(audioF) as sourceF:
        audio = rec.record(sourceF)
    try:
        text = rec.recognize_google(audio)
        if text == 'shutdown':
            say("Shutting down. Thank you and good bye.")
            loop = False
        else:
            if text:
                cmd = command(text)
                if cmd:
                    say(cmd)
                else:
                    say("Command not available.")
    except Exception as e:
        print(e)

os.remove(audioF)
print("Done!")