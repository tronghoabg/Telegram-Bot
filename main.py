from aiogram import Bot, Dispatcher, executor, types
import pyqrcode

bot = Bot(token='5435752958:AAFPTdbfqUAumSaBj-3B6PnpZhQ-mHR50MQ')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im Venus Bot")

@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await message.answer_photo('https://avatars.githubusercontent.com/u/62240649?v=4')

@dp.message_handler()
async def qr(message: types.Message):
    #text = pyqrcode.create(message.text)
    #text.png('code.png', scale=5)
    #await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))
    print(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)