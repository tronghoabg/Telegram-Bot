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
    await message.answer('Vui lòng nhập cú pháp /px (x) x có thể là 1 , 2 , 3')


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
    headerscookie = {'cookie': 'sb=AxtJYx8IlsDg0T71msvaG3QF;wd=1920x979;datr=AxtJY1jnAkhw3iwMGtqVppAw;locale=vi_VN;c_user=100038154123301;xs=37%3AVIUGDyuScRUapg%3A2%3A1665735595%3A-1%3A6276%3A%3AAcXRiBDX1HxrLu_OdBhnqgPPqNIHwwR4S7kqbA8OXQ;fr=00yc3rz6exrFwpgrw.AWWksRIhW9Qz9kIv8Rh5RLJGzzw.BjSRyS.AO.AAA.0.0.BjSRyV.AWU0DsXKrIQ;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1665735840188%2C%22v%22%3A1%7D;cppo=1;usida=eyJ2ZXIiOjEsImlkIjoiQXJqcWkxMTRhYjFqNSIsInRpbWUiOjE2NjU3MzYxMzZ9;' }
    dataid = {"account_id": idAcc_Ads, "business": "606755291020760",
              "access_token": "EAABsbCS1iHgBAIv7NAlBwo7oN3asZBWZCTVZBkr4AycKyZAZC3kCpdLZB4jOs5Vi3ZAUiP7wYbM5Dir3eVTZAYpyiAPte7wnRJOvHhHztWK3sTnHxdgbxpJ1E3U7gsUq0E0GayF3hZBDOKDD1bAmlPKwhOZBaJYk1HX9EyG8tX4thnxwZDZD"}
    url = "https://graph.facebook.com/v15.0/" + dictPixel[idPixel]['id'] +"/shared_accounts/"
    response = requests.post(url, data=dataid, headers=headerscookie).json()

    try:
        result = response['success']
        result = "✅ Share pixel " + dictPixel[idPixel]['name']  + " thành công cho id ADS Acc: " + idAcc_Ads
    except:
        try:
            result =  "⛔ " + response['error']['error_user_msg']
        except:
            result = "⛔ " + response['error']['message']
    print(dictPixel[idPixel]['name'])
    print(response)
    return result


if __name__ == '__main__':
    executor.start_polling(dp)
