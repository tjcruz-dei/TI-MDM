import pyttsx3

def speak(text: str):
    engine = pyttsx3.init()

    change_voice(engine, "pt_PT", "VoiceGenderFemale")
    # Optional settings
    engine.setProperty("rate", 160)   # speaking speed
    engine.setProperty("volume", 1.0) # 0.0 to 1.0

    engine.say(text)
    engine.runAndWait()

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))


if __name__ == "__main__":
    speak("Olá! Atirei o pau ao gato")
