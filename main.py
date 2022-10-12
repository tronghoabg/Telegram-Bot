from aiogram import Bot, Dispatcher, executor, types
import pyqrcode
import requests

bot = Bot(token='5435752958:AAFPTdbfqUAumSaBj-3B6PnpZhQ-mHR50MQ')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im Venus Bot")

@dp.message_handler(commands=['px'])
async def welcome(message: types.Message):
    await message.answer("Hello! Im Venus Bot")

@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await message.answer_photo('https://avatars.githubusercontent.com/u/62240649?v=4')

@dp.message_handler()
async def qr(message: types.Message):
    #text = pyqrcode.create(message.text)
    #text.png('code.png', scale=5)
    #await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


def SharePixcel(idAcc_Ads):
    idPixcel = "449542583803743"
    idBM = "606755291020760"
    Token = "EAAvDoveZCiQoBAMzqMxZAMMICjimm13oHLvOKbhbMWztmm3yBD0P9nfxSpONszAnu6qcIJy4KDrQ9WFmPnU7VfmzLLuG5rByFygbRUkzyWrKbj1G2lL1kgkYUnCrOjtcXRbwbbcSlBg6zsCHew9KRDWkbqOTZADjrmrXmAA0a0XQ0B1GjZAFlctLQ06K1yjw8SNk05rGc4LaqpWIcAZC7YF1ZBly2WmsKXwZAumBZBlcVorZAKWrfhjGU"
    url =  "https://graph.facebook.com/v15.0/" + idPixcel + "/shared_accounts?account_id=" + idAcc_Ads  + "S&business=" +  idBM + "&access_token=" + Token + ""



if __name__ == '__main__':
    executor.start_polling(dp)