# import an external module pyttsx3 and ue it 
# Text to Speech (TTS) library for Python 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.

import pyttsx3
engine = pyttsx3.init()

engine.say("Teri maa ki bkl")
engine.runAndWait()