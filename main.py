from telegram.utelegram_ok import Bot, ReplyKeyboardMarkup, KeyboardButton
from machine import Pin
import network
import _thread
import time
import os


def flanco_subida(Boton):  ## only for the use of buttons <activation edge for buttons>
    boton = Boton["boton"]
   
   
    if boton.value() == 0:
        Boton["contador"] += 1
        if Boton["contador"] > 2:
            Boton["contador"] = 2
        elif Boton["contador"] == 1:
           Boton["flanco"] = True
    else:
      Boton["contador"] = 0


#Connect arduino to wifi
####################
def connectar_Wifi(p_xarxa, p_nom_wifi, p_password):
     if not p_xarxa.isconnected():              
         p_xarxa.active(True)                    
         p_xarxa.connect(p_nom_wifi, p_password) 
         _time_inicial = time.time ()
         timeout = 0
         while not p_xarxa.isconnected() and timeout<10:
             time.sleep(0.25)
             timeout = time.ticks_diff(time.time(), _time_inicial)


def connectar_xarxa():
    _xarxa = network.WLAN(network.STA_IF)
    if not _xarxa.isconnected():
        _nom_wifi = "<INSERT WIFI'S SSID>"
        _psw_wifi = "<INSERT WIFI PASSWORD>"
        print('connectant amb la xarxa Wifi ({})'.format(_nom_wifi))
        connectar_Wifi(_xarxa, _nom_wifi, _psw_wifi)
        if _xarxa.isconnected():
             print("Conexion Stablished")
             print('Conexion data (IP/netmask/gw/DNS):', _xarxa.ifconfig())
        else:
             print("No és possible connectar amb el punt d'accés")
    return _xarxa
####################
    

TOKEN = '<INSERT TELEGRAMS BOT TOKEN>'

bot = Bot(TOKEN, connectar_xarxa)
Led = Pin(<Insert LED Pin number>, Pin.OUT, value=0)
alarma = Pin(<ALARM PIN>, Pin.OUT, value=0)

Bonton_Amarillo = {"boton" : Pin(<BUTTON PIN>, Pin.IN, Pin.PULL_UP),
                   "contador" : 0,
                   "flanco" : False}


keyboard = [
        [KeyboardButton('/led_on'), KeyboardButton('/led_off')],
        [KeyboardButton('/alarma_on'), KeyboardButton('/alarma_off')]
        ]
replyKeyboard = ReplyKeyboardMarkup(keyboard)

### Check the "Main" file for more information in how to modify the keyboard




@bot.add_command_handler('alarma_on')
def start(update):
    update.reply('alarma on', reply_markup=replyKeyboard)
    alarma.value(1)

@bot.add_command_handler('alarma_off')
def start(update):
    update.reply('alarma off', reply_markup=replyKeyboard)
    alarma.value(0)

@bot.add_command_handler('led_on')
def start(update):
    update.reply('Led Encendido', reply_markup=replyKeyboard)
    Led.value(1)

@bot.add_command_handler('led_off')
def start(update):
    update.reply('Led Apagado', reply_markup=replyKeyboard)
    Led.value(0)


xarxa = connectar_xarxa()
bot.start_loop()


while True:
    flanco_subida(Bonton_Amarillo)
    if Bonton_Amarillo["flanco"] == True:
        Bonton_Amarillo["flanco"] = False
