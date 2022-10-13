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
    await message.answer("Đang share pixcel id: " + idAcc_Ads)
    res = SharePixcel(idAcc_Ads)
    await message.answer(res)



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
    headerscookie = {
        'cookie': 'sb=o6A7Y8Xfm5pZcjjO5UqGWX38; datr=o6A7Y2XR6IdFQZSAwQrlguoq; c_user=100038154123301; cppo=1; dpr=1; usida=eyJ2ZXIiOjEsImlkIjoiQXJqb3Z1MHp2M3NmZyIsInRpbWUiOjE2NjU2NjA2MzF9; xs=8:aODLzMa7UVIiuA:2:1664852152:-1:6276::AcVQBDjAUETvEgR6YoQPh9lWdmSjNKdELk2AAMzJvdk; fr=0FwVE48LQfBIO8i3r.AWWef5X2XtapL2c80eA42eg7-v8.BjR_es.5T.AAA.0.0.BjR_es.AWVwZgIbksc; presence=C{"t3":[{"i":"u.100009953598724"}],"utc3":1665661151999,"lm3":"u.100034994394353","v":1}; wd=899x977" '}
    dataid = {"account_id": idAcc_Ads, "business": "606755291020760",
              "access_token": "EAABsbCS1iHgBAArLduhvb9zgqFFCgZCDAAA8HetB6ZBcDgt5MBvPfyJWXqmvU2TDNfjFnFmTfWrGCusff9mJmM6hLteWrG7ZBsAP5AudXU0KNaRUnWPahFQxZCTk5gHSkmrqIsQ6oegwZCyTBqdLzOzD7zgXntR4jo8epeYeffSwnyN4QGVc8"}
    url = "https://graph.facebook.com/v15.0/356037233410519/shared_accounts/"
    response = requests.post(url, data=dataid, headers=headerscookie).json()
    print(response)
    return response



if __name__ == '__main__':
    executor.start_polling(dp)
