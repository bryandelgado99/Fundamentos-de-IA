import speech_recognition as sr

reconocimiento = sr.Recognizer()

archivo = sr.AudioFile('record.wav')

with archivo as source:
    audio = reconocimiento.record(source)

frase = reconocimiento.recognize_google(audio, language='es-EC')
print(f"Acabas de decir: {frase}")