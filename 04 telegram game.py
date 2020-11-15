import telebot #Импортируем(подключаем) модуль с командами для телеграма
from random import randint #Подключаем функцию генерации случайных чисел


#Подключаемся к боту через его ТОКЕН
bot = telebot.TeleBot('1486786215:AAFAgulzxpkgprRu0Wt6yH5NO725xRZGEUI')



random_number = 0 #Число, которое потом заменится на случайное


#########  ОТВЕТ НА КОМАНДУ START
@bot.message_handler(commands=['start']) #ловим команду START
def start_message(message):
    global random_number   #разрешаем функции start_message менять переменную random_number
    bot.send_message(message.chat.id, "Привет, рад тебя видеть!") #Отвечаем на команду START
    random_number = randint(0, 100) #ГЕНЕРАЦИЯ СЛУЧАЙНОГО ЧИСЛА


######## OТВЕТ НА ТЕКСТОВОЕ СООБЩЕНИЕ
@bot.message_handler(content_types = ['text'])#Ловим сообщения с текстом
def otvet (message):
    try: #Попытайся сделать это
        user_number = int(message.text) #Превращаем ответ пользователя из строки(str)  число(int)

        if user_number == random_number:
            bot.send_message(message.chat.id, "PERFECT! You guessed ")  
        
        elif user_number > random_number:
            bot.send_message(message.chat.id, "Too big")
            
        else:
            bot.send_message(message.chat.id, "Too small")
            
     
    except:
        bot.send_message(message.chat.id, "WRONG! ONLY NUMBERS")  
                

        
       
    
    #bot.send_message(message.chat.id, random_number)
    


bot.polling() #Запрос сообщений
