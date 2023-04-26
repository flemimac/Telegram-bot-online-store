import telebot
from telebot import types
import sqlite3 as sl

con = sl.connect('database.db', check_same_thread=False)

bot = telebot.TeleBot('6014768020:AAFXQbD37VvsqVBO0wVy83YCHOKzDkGoOrE')

# Фотографии
# Клей
photo_glue1kg = open('C:\BotTelegramPython\database\PVA\PVA3KG.jpg', 'rb')
photo_glue750g = open('C:\BotTelegramPython\database\PVA\PVA750G.jpg', 'rb')
photo_glue250g = open('C:\BotTelegramPython\database\PVA\PVA250G.jpg', 'rb')

# Краска
photo_paint1L = open('C:\BotTelegramPython\database\Paint\PaintDulux1L.jpg', 'rb')
photo_paint25L = open('C:\BotTelegramPython\database\Paint\PaintDulux25L.jpg', 'rb')

# Старт бота
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_store = types.KeyboardButton("Посмотреть ассортимент")
    btn_question = types.KeyboardButton("Задать вопрос")
    markup.add(btn_store, btn_question)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для магазина СтройБаза".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    a = str(message) # Получаем из ответа пользователя "message" и придаем ему аргумент "a"

    # Просмотр ассортимента
    if message.text == "Посмотреть ассортимент": 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_glue = types.KeyboardButton("Клей") 
        btn_paint = types.KeyboardButton("Краска")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn_glue, btn_paint, btn_back)
        bot.send_message(message.chat.id, text='В ассортименте имеется:\n 1. Клей ПВА Момент столяр\n 2. Краска для пола Dulux', reply_markup=markup)
    
    # Клей
    elif message.text == "Клей":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1kg = types.KeyboardButton("Клей 1 кг")
        btn_750g = types.KeyboardButton("750 грамм")
        btn_250g = types.KeyboardButton("250 грамм ")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn_1kg, btn_250g, btn_750g, btn_back)
        bot.send_message(message.chat.id, text='Клей ПВА Момент столяр\n Сколько нужно клея 1 кг, 750 грамм, 250 грамм?', reply_markup=markup)
        
    # Клей 1 кг
    elif message.text == "Клей 1 кг":
        with con:
            data = con.execute("SELECT * FROM database WHERE name=?", [a]) # Проверяет есть ли аргумент "a" в базе данных
            res = data.fetchone()
            if not res: # Если нет - товара нет
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn_750g = types.KeyboardButton("750 грамм")
                btn_250g = types.KeyboardButton("250 грамм ")
                btn_back = types.KeyboardButton("Назад")
                markup.add(btn_250g, btn_750g, btn_back)
                bot.send_message(message.chat.id, text='Товара нет', reply_markup=markup)
            else: # Если да - показывает описание и фото
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn_750g = types.KeyboardButton("750 грамм")
                btn_250g = types.KeyboardButton("250 грамм ")
                btn_back = types.KeyboardButton("Назад")
                markup.add(btn_250g, btn_750g, btn_back)
                bot.send_message(message.chat.id, text='Клей ПВА Момент столяр 1 кг', reply_markup=markup)
                bot.send_photo(message.chat.id, photo_glue1kg)
        
    # Клей 750 грамм
    elif message.text == "750 грамм":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_750g = types.KeyboardButton("1 кг")
        btn_250g = types.KeyboardButton("250 грамм ")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn_250g, btn_750g, btn_back)
        bot.send_message(message.chat.id, text='Клей ПВА Момент столяр 750 грамм', reply_markup=markup)
        bot.send_photo(message.chat.id, photo_glue750g)

    # Клей 250 грамм
    elif message.text == "250 грамм":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_750g = types.KeyboardButton("750 грамм")
        btn_250g = types.KeyboardButton("1 кг ")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn_250g, btn_750g, btn_back)
        bot.send_message(message.chat.id, text='Клей ПВА Момент столяр 250 грамм', reply_markup=markup)
        bot.send_photo(message.chat.id, photo_glue250g)

    # Краска
    elif message.text == "Краска":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1l = types.KeyboardButton("1 литр")
        btn_25l = types.KeyboardButton("2,5 литров")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn_1l, btn_25l, btn_back)
        bot.send_message(message.chat.id, text='Краска для пола Dulux\nСколько нужно краски: 1 литр или 2,5 литров?', reply_markup=markup)

    elif message.text == "1 литр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_25l = types.KeyboardButton("2,5 литров")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn_25l, btn_back)
        bot.send_message(message.chat.id, text='Краска для пола Dulux 1 литр', reply_markup=markup)
        bot.send_photo(message.chat.id, photo_paint1L)
        
    elif message.text == "2,5 литров":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1l = types.KeyboardButton("1 литр")
        btn_back = types.KeyboardButton("Назад")
        markup.add(btn_1l, btn_back)
        bot.send_message(message.chat.id, text='Краска для пола Dulux 2,5 литров')
        bot.send_photo(message.chat.id, photo_paint25L, caption='Желаете купить?', reply_markup=markup)


    # Возврат в главное меню
    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_store = types.KeyboardButton("Посмотреть ассортимент")
        btn_question = types.KeyboardButton("Задать вопрос")
        markup.add(btn_store, btn_question)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для магазина СтройБаза".format(message.from_user), reply_markup=markup)
        
    else:
        bot.send_message(message.chat.id, text='error 1')
             
# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)