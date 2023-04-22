import asyncio
import logging
from aiogram import Bot, Dispatcher, types

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6014768020:AAFXQbD37VvsqVBO0wVy83YCHOKzDkGoOrE")
dp = Dispatcher(bot)

# Фотографии
# Клей
photo_kley1kg = open('C:\BotTelegramPython\database\PVA\PVA3KG.jpg', 'rb')
photo_kley750g = open('C:\BotTelegramPython\database\PVA\PVA750G.jpg', 'rb')
photo_kley250g = open('C:\BotTelegramPython\database\PVA\PVA250G.jpg', 'rb')

@dp.message_handler(commands=("start"))
async def cmd_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_store = types.KeyboardButton("Посмотреть ассортимент")
    btn_question = types.KeyboardButton("Задать вопрос")
    markup.add(btn_store, btn_question)
    await message.answer("Привет, {0.first_name}! Я тестовый бот для магазина СтройБаза".format(message.from_user), reply_markup=markup)

@dp.message_handler()
async def assortment(message: types.Message):
        # Ассортимент
    if message.text == "Посмотреть ассортимент": 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_kley = types.KeyboardButton("Клей")
        btn_nazad = types.KeyboardButton("Назад")
        markup.add(btn_kley, btn_nazad)
        await message.answer('Клей ПВА Момент столяр', reply_markup=markup)

        # Выбор клея
    elif message.text == "Клей":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1kg = types.KeyboardButton("1 кг")
        btn_750g = types.KeyboardButton("750 грамм")
        btn_250g = types.KeyboardButton("250 грамм ")
        btn_nazad = types.KeyboardButton("Назад")
        markup.add(btn_1kg, btn_250g, btn_750g, btn_nazad)
        await message.answer('Клей ПВА Момент столяр\n Сколько нужно клея 1 кг, 750 грамм, 250 грамм?', reply_markup=markup)
        
        # Клей 1 кг
    elif message.text == "1 кг":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_750g = types.KeyboardButton("750 грамм")
        btn_250g = types.KeyboardButton("250 грамм ")
        btn_nazad = types.KeyboardButton("Назад")
        markup.add(btn_250g, btn_750g, btn_nazad)
        await message.answer('Клей ПВА Момент столяр 1 кг', reply_markup=markup)
        bot.send_photo(message.chat.id, photo=photo_kley1kg)
        
        # Клей 750 грамм
    elif message.text == "750 грамм":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_750g = types.KeyboardButton("1 кг")
        btn_250g = types.KeyboardButton("250 грамм ")
        btn_nazad = types.KeyboardButton("Назад")
        markup.add(btn_250g, btn_750g, btn_nazad)
        await message.answer('Клей ПВА Момент столяр 750 грамм', reply_markup=markup)
        bot.send_photo(message.chat.id, photo_kley750g)

        # Клей 250 грамм
    elif message.text == "250 грамм":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_750g = types.KeyboardButton("750 грамм")
        btn_250g = types.KeyboardButton("1 кг ")
        btn_nazad = types.KeyboardButton("Назад")
        markup.add(btn_250g, btn_750g, btn_nazad)
        await message.answer('Клей ПВА Момент столяр 250 грамм', reply_markup=markup)
        bot.send_photo(message.chat.id, photo_kley250g)
    
    # Возврат в главное меню
    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_store = types.KeyboardButton("Посмотреть ассортимент")
        btn_question = types.KeyboardButton("Задать вопрос")
        markup.add(btn_store, btn_question)
        await message.answer("Привет, {0.first_name}! Я тестовый бот для магазина СтройБаза".format(message.from_user), reply_markup=markup)
        
    else:
        await message.answer('error 1')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

