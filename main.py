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
    idAcc_Ads = message.text[4:50]
    url = SharePixcel(idAcc_Ads)
    await message.answer("Đang share pixcel cho Ads Acc (ID:" + idAcc_Ads + ")")
    response = requests.post(url, data= {"account_id": "559097072569947",
                                          "business": "606755291020760"})
    await message.answer(response.text)
    print(response.mess)



@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await message.answer_photo('https://avatars.githubusercontent.com/u/62240649?v=4')


@dp.message_handler()
async def qr(message: types.Message):
    print('hihi')
    # text = pyqrcode.create(message.text)
    # text.png('code.png', scale=5)
    # await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


def SharePixcel(idAcc_Ads):
    idPixcel = "449542583803743"
    idBM = "606755291020760"
    Token = "EAABsbCS1iHgBAFB0kUnsJVCD8zZCXM7OqoL4jgMrdd5ZB6qCjclDxIhLxoS0KFNhZCqoEAXTmgD14YWwBHybp78FEO0vPhYsUYghaiKRJsMkA5FJe5D9yky364IMX6QXv2HqhvgcWE7S7SbuOiwTXIpLT7JTZAw8YXZCXlxqp6O7Y2hgZBm7ZBA"
    url = "https://graph.facebook.com/449542583803743/shared_accounts"
    print(idAcc_Ads)
    print(url)
    return url


if __name__ == '__main__':
    executor.start_polling(dp)
