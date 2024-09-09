import speech_recognition as sr

# Init
recognizer = sr.Recognizer()

# Use microphone
with sr.Microphone() as source:
    print("Por favor, di algo:")
    audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to recognize audio
        texto = recognizer.recognize_google(audio, language='es-ES')
        print(f"Dijiste: {texto}")
    except sr.UnknownValueError:
        print("No pude entender lo que dijiste.")
    except sr.RequestError as e:
        print(f"Error con Google Speech Recognition: {e}")