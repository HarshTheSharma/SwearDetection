#imports
import speech_recognition as sr

#variables
recognizer = sr.Recognizer()

#A loop comparing speech from the microphone to the variable above
with sr.Microphone() as source:
    print('Please start speaking:\n')
    while True:
        audio_input = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_input)
            if "*" in text.lower():
                print('asterisk detected in the speech.')
                #The API automatically replaces swear words with a set of asterisks, this if statment checks for this.
                swore = True
        except Exception as e:
            print('Please speak again.')
