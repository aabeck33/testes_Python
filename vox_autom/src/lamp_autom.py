##########################################################################
# Projeto DIO - IoT
#
# Instalação das Bibliotecas:
#       conda install -c anaconda pyaudio
#       pip install SpeechRecognition
#       pip install pyttsx3
#       conda install -c anaconda pyserial
#
##################################

import speech_recognition as sr
import pyttsx3
import serial
import threading
import time

text="DESATIVADO"

r = sr.Recognizer()

mic = sr.Microphone()

engine = pyttsx3.init()

conectado = False
porta = 'COM7' # linux ou mac em geral -> '/dev/ttyS0'
velocidadeBaud = 9600 # Velocidade de transmissão Serial

mensagensRecebidas = 1;
desligarArduinoThread = False

try:
    # Inicia a conexão com a porta serial com a chamada ao método serial.Serial(PORTA_SERIAL, BAUD_RATE).
    SerialArduino = serial.Serial(porta,velocidadeBaud, timeout = 0.2)
except:
    print("Verificar porta serial ou religar arduino")

def handle_data(data):
    global mensagensRecebidas
    print("Recebi " + str(mensagensRecebidas) + ": " + data)
    mensagensRecebidas += 1

def read_from_port(ser):
    global conectado, desligarArduinoThread
   
    while not conectado:
        conectado = True

        while True:
           reading = ser.readline().decode()
           if reading != "":
               handle_data(reading)
           if desligarArduinoThread:
               print("Desligando Arduino")
               break

lerSerialThread = threading.Thread(target=read_from_port, args=(SerialArduino,))
lerSerialThread.start()

print("Preparando Arduino")
time.sleep(2)
print("Arduino Pronto")

with mic as fonte:
    while(text=="DESATIVADO"):
        r.adjust_for_ambient_noise(fonte)
        print("Estou ouvindo")
        audio = r.listen(fonte)
        print("Enviando para reconhecimento")
       
        try:
            text = r.recognize_google(audio, language= "pt-BR")
            if(text=="ativar"):
                print("Ativando reconhecimento de fala!")
                engine.say("Ativando reconhecimento de fala!")
                engine.runAndWait()
                engine.stop()
            else: text="DESATIVADO"
        except:
            text="DESATIVADO"
           
    while(text=="ativar"):
        r.adjust_for_ambient_noise(fonte)
        print("Fale alguma coisa")
        audio = r.listen(fonte)
        print("Enviando para reconhecimento")
       
        try:
            fala = r.recognize_google(audio, language= "pt-BR")
            print("Você disse: {}".format(fala))
           
            if (fala=="ligar a luz"):
                print("Enviando")
                SerialArduino.write('ligar luzes\n'.encode())
                time.sleep(2)
               
                engine.say("Ligando as luzes!")
                engine.runAndWait()
                engine.stop()
               
            elif (fala=="Desligar a luz"):
                print("Enviando")
                SerialArduino.write('desligar luzes\n'.encode())
                time.sleep(2)
               
                engine.say("desligando as luzes")
                engine.runAndWait()
                engine.stop()
           
            elif ((fala=="obrigado")or(fala=="Obrigado")):               
                engine.say("De nada, estou a sua disposição.")
                engine.runAndWait()
                engine.stop()
               
            elif (fala=="dispensada"):
                engine.say("Tudo bem, desativando reconhecimento de fala.")
                engine.runAndWait()
                engine.stop()
                text="DESATIVADO"
           
               
        except:
            print("Não entendi o que você disse")
           
            engine.say("Não entendi o que você disse, pode repetir?")
            engine.runAndWait()
            engine.stop()