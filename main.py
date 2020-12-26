# importing libraries
import pyaudio
import speech_recognition as mr


joeListener = mr.Recognizer()

stopListening = False

while not stopListening:
    try:
        with mr.Microphone() as source:
            voiceCommand = joeListener.listen(source)
            command = joeListener.recognize_google(voiceCommand)
            print(command)
            if 'joe' in command.lower():
                print("Listening . . . ")
                print(command)
            if 'stop' in command.lowe():
                print("always a pleasure!, ciao! ")
                stopListening = True

    except:
        pass
