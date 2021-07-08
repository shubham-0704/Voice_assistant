def say(text):
    tts=gTTS(text=text,lang='en')
    fname='temp.mp3'
    tts.save(fname)
    playsound.playsound(fname)