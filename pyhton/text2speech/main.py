import pyttsx3
names = ["Ashish","Namdeo"]

for name in names:
    engine = pyttsx3.init()
    engine.say(f"shoutout to {name}")
    engine.runAndWait()