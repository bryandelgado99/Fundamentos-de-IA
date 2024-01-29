'''
Prueba 1 - Segundo Bimestre
Nombres: Delgado Bryan y Revelo Ingrith
Fecha: 29/01/2024

Parte de casa seleccionada: Cocina
'''
import pyttsx3
import speech_recognition as sr

# Inicializamos el texto a voz
engine = pyttsx3.init()

# Configuramos el texto a voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# Importamos Speech Recognition y lo incializamos
reconocimiento =  sr.Recognizer()

archivo = sr.AudioFile('humo.wav')

with archivo as source:
    try:
        engine.say(" Hola, soy tu asistente Pyssistant. ¿En qué puedo ayudarte?")
        engine.runAndWait()

        audio = reconocimiento.record(source)
        frase = reconocimiento.recognize_google(audio, language='es-EC')
        print(frase)

        if "microondas" in frase:
            engine.say("Ok, Abriendo el microondas")
            print("Ok, Abriendo el microondas")
            engine.runAndWait()
        elif "compras" in frase:
            engine.say("Analizando la lista de compras, espera un momento...")
            print("Analizando la lista de compras, espera un momento...")
            engine.runAndWait()
        elif "humo" in frase:
            engine.say("Encendiendo detector de humo, espera un momento...")
            engine.runAndWait()
        elif "horno" in frase:
            engine.say("Encendiendoel horno, espera un momento...")
            engine.runAndWait()
        else:
            engine.say("No entendi lo que dijiste. ¿Puedes reprtirlo?")
            engine.runAndWait()
    except Exception:
        print(Exception)
