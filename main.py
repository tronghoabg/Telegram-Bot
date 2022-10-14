from aiogram import Bot, Dispatcher, executor, types
import pyqrcode
import requests

bot = Bot(token='5774231926:AAFwJiyc57wH-UX_Q0sazXZL3gZERhySOUI')
dp = Dispatcher(bot)

dictPixel = {   1:
            {'id': '449542583803743',
            'name': 'Pixel Nữ 25+'},
            2 :
            {'id' : '969729217756981',
            'name': 'Pixel 25+'},
            3:
            {'id' : '753517695875549',
            'name': 'Pixel 30+'},
            }

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("🤖 Hello! Im Venus Bot")


@dp.message_handler(commands=['px'])
async def welcome(message: types.Message):
    await message.answer('Vui lòng nhập cú pháp /px(x) x có thể là 1 , 2 , 3')


@dp.message_handler(commands=['px1'])
async def welcome(message: types.Message):
    idAcc_Ads = message.text[5:50]
    if len(idAcc_Ads) == 0 :
        await message.answer('⛔ Có vẻ bạn chưa nhập id Ads acc')
    elif  len(idAcc_Ads) > 0 and len(idAcc_Ads)  < 10:
        await message.answer('⛔ id Ads Acc bạn nhập là quá ngắn, Vui lòng kiểm tra lại')
    else:
        await message.answer("🤖 Đang share pixcel cho Ads Acc id: " + idAcc_Ads)
        idpixel = 1
        res = SharePixel(idAcc_Ads, idpixel)
        await message.answer(res)


@dp.message_handler(commands=['px2'])
async def welcome(message: types.Message):
    idAcc_Ads = message.text[5:50]
    if len(idAcc_Ads) == 0 :
        await message.answer('⛔ Có vẻ bạn chưa nhập id Ads acc')
    elif  len(idAcc_Ads) > 0 and len(idAcc_Ads)  < 10:
        await message.answer('⛔ id Ads Acc bạn nhập là quá ngắn, Vui lòng kiểm tra lại')
    else:
        await message.answer("🤖 Đang share pixcel cho Ads Acc id: " + idAcc_Ads)
        idpixel = 2
        res = SharePixel(idAcc_Ads, idpixel)
        await message.answer(res)

@dp.message_handler(commands=['px3'])
async def welcome(message: types.Message):
    idAcc_Ads = message.text[5:50]
    if len(idAcc_Ads) == 0 :
        await message.answer('⛔ Có vẻ bạn chưa nhập id Ads acc')
    elif  len(idAcc_Ads) > 0 and len(idAcc_Ads)  < 10:
        await message.answer('⛔ id Ads Acc bạn nhập là quá ngắn, Vui lòng kiểm tra lại')
    else:
        await message.answer("🤖 Đang share pixcel cho Ads Acc id: " + idAcc_Ads)
        idpixel = 3
        res = SharePixel(idAcc_Ads, idpixel)
        await message.answer(res)


@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await message.answer_photo('https://avatars.githubusercontent.com/u/62240649?v=4')


@dp.message_handler()
async def qr(message: types.Message):
    print('')
    # text = pyqrcode.create(message.text)
    # text.png('code.png', scale=5)
    # await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))

def SharePixel(idAcc_Ads, idPixel):
    result = ""
    headerscookie = {
        'cookie': 'sb=o6A7Y8Xfm5pZcjjO5UqGWX38; datr=o6A7Y2XR6IdFQZSAwQrlguoq; c_user=100038154123301; cppo=1; dpr=1; usida=eyJ2ZXIiOjEsImlkIjoiQXJqb3Z1MHp2M3NmZyIsInRpbWUiOjE2NjU2NjA2MzF9; xs=8:aODLzMa7UVIiuA:2:1664852152:-1:6276::AcVQBDjAUETvEgR6YoQPh9lWdmSjNKdELk2AAMzJvdk; fr=0FwVE48LQfBIO8i3r.AWWef5X2XtapL2c80eA42eg7-v8.BjR_es.5T.AAA.0.0.BjR_es.AWVwZgIbksc; presence=C{"t3":[{"i":"u.100009953598724"}],"utc3":1665661151999,"lm3":"u.100034994394353","v":1}; wd=899x977" '}
    dataid = {"account_id": idAcc_Ads, "business": "606755291020760",
              "access_token": "EAABsbCS1iHgBAEDmQCZBRg9ZBZB0TyH7C1HSThJE9ZCfMZBf5b6ZBrbu0elbZA33fZCZAOI6fvWHURnw7rivMGSz1wWtEfFZCFDIqf2shf9C2aeduDW5NsPwri1CD1BBVvMUxbtKTnzRMcsr6Luka1Hdyt3qpbTOgDKP5aNsvKknWRgOPdbquICnzB"}
    url = "https://graph.facebook.com/v15.0/" + dictPixel[idPixel]['id'] +"/shared_accounts/"
    response = requests.post(url, data=dataid, headers=headerscookie).json()

    try:
        result = response['success']
        result = "✅ Share pixel " + dictPixel[idPixel]['name']  + " thành công cho id ADS Acc: " + idAcc_Ads
    except:
        result = "⛔ Share pixel không thành công, có thể do sai id ADS Acc: " + idAcc_Ads

    print(dictPixel[idPixel]['name'])
    print(response)
    return result


if __name__ == '__main__':
    executor.start_polling(dp)
