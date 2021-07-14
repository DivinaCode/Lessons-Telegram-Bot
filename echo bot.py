import telebot #Импортируем(подключаем) модуль с командами для телеграма

#Подключаемся к боту через его ТОКЕН
bot = telebot.TeleBot('1486786215:AAFAgulzxpkgprRu0Wt6yH5NO725xRZGEUI')



last_message = "Привет" #Переменная, в которой будет храниться последнее сообщение


@bot.message_handler(commands=['start']) #ловим команду START
def start_message(message):
    bot.send_message(message.chat.id, "Привет, рад тебя видеть!") #Отвечаем на команду START

##############################################################
 
@bot.message_handler(commands=['photo']) #ловим команду PHOTO
def send_picture(message):
    with open("cat81.jpg", 'rb') as cat: #Загружем свою картинку
        bot.send_photo(message.chat.id, cat) #Шлём фото кота

##############################################################

@bot.message_handler(content_types = ['text'])#Ловим сообщения с текстом
def otvet (message):
    global last_message 
    bot.send_message(message.chat.id, message.from_user.first_name +", "+ last_message)
    last_message = message.text #


bot.polling() #Запрос сообщений
