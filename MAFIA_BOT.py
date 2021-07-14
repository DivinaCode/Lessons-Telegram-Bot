import telebot
import random
from telebot import types

TOKEN = '1787466603:AAEgc4lY-WuGiYRMiSDf0YAQQKJU9xYpod0'
bot = telebot.TeleBot(TOKEN)

COMMISSAR = 'Комиссар'
MAFIA = 'Мафия'
DOCTOR = 'Доктор'
CITIZEN = 'Житель'

game = False


class Player():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.isAlive = True
        self.role = None

    def set_role(self, role):
        self.role = role


players = []


@bot.message_handler(commands=['start'])
def start(message):
    """
    Тут происходит регистрация новых игроков
    :param message:
    :return:
    """
    if game:  ##  Если игра началась, то новые игроки НЕ МОГУТ присоединиться
        bot.send_message(message.chat.id, "Игра уже началась")
        return

    id = message.chat.id
    name = message.from_user.first_name

    for p in players:  ## Проверем, что игрок ещё не зарегистрирован
        if p.id == id:
            bot.send_message(id, "Ты уже зарегистрирован")
            return

    ## РЕГИСТРАЦИЯ игрока
    for p in players:
        bot.send_message(p.id, f'Игрок {name} присоединился к игре')

    player = Player(id, name)
    players.append(player)
    bot.send_message(message.chat.id, f'Ты зарегистрирован под именем {name}. Правила игры - /help')


## TODO : Дописать правила игры
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "загугли сам")


@bot.message_handler(commands=['players'])
def show_players(message):
    if players == []:
        bot.send_message(message.chat.id, 'Игроков пока нет :(')
        return

    names = [p.name for p in players]
    bot.send_message(message.chat.id, '\n'.join(names))


@bot.message_handler(commands=['start_game'])
def start_game(message):
    global game

    if game:
        bot.send_message(message.chat.id, 'Игра уже началась')
        return

    if len(players) < 4:
        bot.send_message(message.chat.id, f'Недостаточно игровков, нужно ещё {4 - len(players)}')
        return

    random.shuffle(players)
    roles = [MAFIA, MAFIA, COMMISSAR, DOCTOR]
    for p in players:
        if p.name == 'Katy':
            #role = 'Ведущий'
            role = "Комиссар"
        elif roles:
            role = roles.pop()
        else:
            role = CITIZEN

        p.set_role(role)
        bot.send_message(p.id, f'Игра началась, вы - {p.role}')

    game = True


@bot.message_handler(commands=['commissar'])
def check_mafia(message):
    keyboard = types.InlineKeyboardMarkup()

    for p in players:
        if p.role != "Комиссар":
            btn = types.InlineKeyboardButton(p.name, callback_data=f'{COMMISSAR[0]}{p.name}')
            keyboard.add(btn)
    bot.send_message(message.chat.id, 'Кого нужно проверить', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    role = call.data[0]
    name = call.data[1:]

    if role == COMMISSAR[0]:
        for p in players:
            if p.name == name:
                if p.role == MAFIA:
                    bot.send_message(call.message.chat.id, f"{p.name}  мафия")
                else:
                    bot.send_message(call.message.chat.id, f"{p.name} не  мафия")

        bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '')# удаляем кнопки у последнего сообщения


if __name__ == '__main__':
    bot.polling()
