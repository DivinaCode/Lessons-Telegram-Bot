import telebot
import random

TOKEN = '1787466603:AAEgc4lY-WuGiYRMiSDf0YAQQKJU9xYpod0'

bot = telebot.TeleBot(TOKEN)

words = ["бетономешалка", 'сосиска', 'корова']
word = words[0]




@bot.message_handler(commands=['start'])
def start_message(message):
    global word
    word = random.choice(words)

    shuffle_word = list(word)
    random.shuffle(shuffle_word)
    shuffle_word = ''.join(shuffle_word)

    bot.send_message(message.chat.id, "Угадай слово: "+ shuffle_word )


@bot.message_handler(content_types=['text'])
def answer(message):
    text = message.text

    if text.lower() == word:
        bot.send_message(message.chat.id, "Ура! Это верное слово! Для нововй игры /start")
    else:
        bot.send_message(message.chat.id, 'Не угадал! Это слово - ' + word)
        bot.send_message(message.chat.id, 'Для новой попытки нажми /start')

if __name__ == '__main__':
    bot.polling()


