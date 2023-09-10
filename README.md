# uTelgram-Bot
home automation with (Arduino/Telegram/MicroPython)

With this project you will be able to connect any device in your home and remotely manage it via telegram with telegram bots+arduino+programming !!

In the Main file you will find an example of use featuring lights and buttons to play with (Feel free to recreate the scenary to check everything)


1.- We will need:
     - x1 arduino esp32 s3 (MicroPython) [Due to multi threading. we will need this model or a more powerfull one]
     - x1 Telegram Token


2.- Septs to follow
      - Create a Telegram Bot | Example --> https://www.youtube.com/watch?v=URPIZZNr_2M
      - Modify Main.py with the data needed (wifi, bot token)
      - Ready to go!






#########
Using custom keyboards
You can define custom keyboards to send with a reply

from utelegram import ReplyKeyboardMarkup, KeyboardButton

keyboard = [
    [KeyboardButton('Btn1')], #each list is a row, each element is a column
    [KeyboardButton('Btn2'), KeyboardButton('Btn3')],
]

reply_keyboard = ReplyMarkupKeyboard(keyboard) #pass your array as the keyboard

@bot.add_message_handler('^Show keyboard')
def show(update):
    update.reply('here it is!', reply_markup=reply_keyboard)


######### (custom keyboards via --> https://github.com/gabrielebarola/telegram-upy)
