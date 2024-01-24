# Importamos la libreria de speech_recognition
import speech_recognition as sr
# Importamos la libreria para abrir el navegador
import webbrowser as wb

# Llamamos al método principal de speecgh rcognition
reconocimiento = sr.Recognizer()

# Creamos el método de manejo de excepciones
with sr.Microphone() as source:
    try:
        print("Hola, soy Py-Tube. ¿En qué te puedo ayudar?")
        voice = reconocimiento.listen(source)
    except Exception:
        print(Exception)
    finally:
        frase = reconocimiento.recognize_google(voice, language='en-US')
        print(f"Buscando: '{frase}' en Youtube")

youtube_url = f"https://www.youtube.com/results?search_query={frase}"
wb.open(youtube_url)