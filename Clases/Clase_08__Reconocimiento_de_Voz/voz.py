import speech_recognition as sr
import webbrowser as wb

reconocimiento = sr.Recognizer()

with sr.Microphone() as source:
    try:
        print("Hola, soy Py-ssistant. ¿En qué te puedo ayudar?")
        audio = reconocimiento.listen(source)
    except Exception:
        print(Exception)
    finally:
        frase = reconocimiento.recognize_google(audio, language='es-EC')
        print(f"Buscando: '{frase}' en Google")

url = f"https://www.google.com/search?q={frase}"
wb.open(url)