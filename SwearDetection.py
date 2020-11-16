import speech_recognition as sr

r = sr.Recognizer()

keyWord = '*'
#The Google Api replaces swears with *'s

with sr.Microphone() as source:
    print('Please start speaking\n')
    while True: cccccccccccccccccc
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if keyWord.lower() in text.lower():
                print('Keyword detected in the speech.')
                swore = True
        except Exception as e:
            print('Please speak again.')
