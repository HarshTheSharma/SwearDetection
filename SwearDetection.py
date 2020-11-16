import speech_recognition as sr

recognizer = sr.Recognizer()
key_phrase = '*'
# The Google API censors swear words with *s

with sr.Microphone() as source:
    print('Please start speaking:\n')
    while True:
        audio_input = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_input)
            if key_phrase.lower() in text.lower():
                print('Keyword detected in the speech.')
                swore = True
        except Exception as e:
            print('Please speak again.')
