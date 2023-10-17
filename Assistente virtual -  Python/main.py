import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
from gtts import gTTS
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()

def fala(texto):
    tts = gTTS(texto, lang='pt-br')
    tts.save("resposta.mp3")
    os.system("start resposta.mp3")



maquina.runAndWait()


def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()

            if 'sofia' in comando:
                comando = comando.replace('sofia', '')
                maquina.say(comando)
                maquina.runAndWait()
    except sr.WaitTimeoutError:
        print('Tempo limite para fala excedido')
    except sr.UnknownValueError:
        print('Não foi possível entender a fala')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são ' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, sentences=2)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'navegador' in comando:
        os.system("start opera.exe")
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()
    elif 'canal do youtube' in comando:
        canal = comando.replace('canal do youtube', '')
        pywhatkit.playonyt(canal)
        maquina.say('Encontrando canal')
        maquina.runAndWait()

comando_voz_usuario()
