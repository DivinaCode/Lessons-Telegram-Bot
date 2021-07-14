import telebot
import random


TOKEN = '1787466603:AAEgc4lY-WuGiYRMiSDf0YAQQKJU9xYpod0'
bot = telebot.TeleBot(TOKEN)


words = ['канат', 'фикус', 'адвокат']

word = ''

guess = []

@bot.message_handler(commands = ['start'])
def generate_random_word(message):
    global word


    word = random.choice(words)

    guess.clear()
    for i in range(len(word)):
        guess.append('⭕️')

    bot.send_message(message.chat.id, ''.join(guess))


@bot.message_handler(content_types=['text'])
def answer(message):
    if word == '':
        generate_random_word(message)
        return
    text = message.text

    if len(text) == 1:
        if text in word:
            for i in range(len(word)):
                if text == word[i]:

                    guess[i] = text



            bot.send_message(message.chat.id, ''.join(guess))
            if '⭕️' not in guess:
                bot.send_message(message.chat.id, 'ты угадал слово, начать новую игру /start')

        else:
            bot.send_message(message.chat.id, 'Нет такой буквы')

    else:
        if word == text:
            bot.send_message(message.chat.id, 'Угадал, ачать новую игру /start')

        else:
            bot.send_message(message.chat.id, 'Не угадал, это слово ' + word)

if __name__ == '__main__':

    bot.polling()
