# Modelo de reconocimiento de voz

import speech_recognition as sr

def recognize_speech(audio_path):
    """Reconoce el habla en un archivo de audio usando SpeechRecognition."""
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_path) as source:
            print("[INFO] Procesando el archivo de audio...")
            audio = recognizer.record(source)  # Lee el audio completo
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"[INFO] Texto reconocido: {text}")
        return text
    except sr.UnknownValueError:
        print("[ERROR] No se pudo entender el audio.")
        return None
    except sr.RequestError:
        print("[ERROR] Error con el servicio de reconocimiento.")
        return None
