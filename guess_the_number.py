import telebot
import random

token = '1787466603:AAEgc4lY-WuGiYRMiSDf0YAQQKJU9xYpod0'

bot = telebot.TeleBot(token)
r = random.randint(1, 100)
print(r)



@bot.message_handler(commands=["help"])
def help(message):

    bot.send_message(message.chat.id, 'Я ничем не могу помочь')

@bot.message_handler(commands=['r'])
def random_number(message):
    global r
    r = random.randint(1, 100)
    print(r)

@bot.message_handler(content_types = ["text"])
def echo(message):
    text = message.text

    if not text.isdigit():
        bot.send_message(message.chat.id, 'Это игра "Угадай число", мне нужны только цифры')
        return
    user_number = int(text)

    if user_number == r:
        bot.send_message(message.chat.id, 'Ты угадал')
    if user_number > r:
        bot.send_message(message.chat.id, 'Слишком много')
    if user_number < r:
        bot.send_message(message.chat.id, 'Слишком мало')


## =============================================
if __name__ == '__main__':
    bot.polling()

