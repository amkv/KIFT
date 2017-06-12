import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id) #16 intonations #22 Portal #28 37 39 female #38 russian style
# print voice.id
engine.say("This is my test")
# engine.rec("This is my test", 'test.wav')
engine.runAndWait()
