from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

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
def SharePixel(idAcc_Ads, idPixel):
    result = ""
    headerscookie = {'cookie': 'sb=AxtJYx8IlsDg0T71msvaG3QF;wd=1920x979;datr=AxtJY1jnAkhw3iwMGtqVppAw;locale=vi_VN;c_user=100038154123301;xs=37%3AVIUGDyuScRUapg%3A2%3A1665735595%3A-1%3A6276%3A%3AAcXRiBDX1HxrLu_OdBhnqgPPqNIHwwR4S7kqbA8OXQ;fr=00yc3rz6exrFwpgrw.AWWksRIhW9Qz9kIv8Rh5RLJGzzw.BjSRyS.AO.AAA.0.0.BjSRyV.AWU0DsXKrIQ;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1665735840188%2C%22v%22%3A1%7D;cppo=1;usida=eyJ2ZXIiOjEsImlkIjoiQXJqcWkxMTRhYjFqNSIsInRpbWUiOjE2NjU3MzYxMzZ9;' }
    dataid = {"account_id": idAcc_Ads, "business": "606755291020760",
              "access_token": "EAAQUZAS3L8KIBAIKXZCuCs8h1CpyZABS50WsJ23NtiFborgYIezX7PYTZB09npDuvUYJ4DoZAblWwGQMqlpOp6WZBzsZAA1pExuQks4VTbITe8DLvo1CZA0Hv3OS9w3ZB42BGmfx5FZAfRUIdzjOL1pGGuKE6ZCtopuWpUS9OqVabnatnzccKnUZAe8r0H3KNsP7RjQ372qLlnIavfUo7fcDe5I0ca0VQfs6YrCxcVaMhglXZBkdNHIRNMkWe"}
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


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def share(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text)
    message = update.message
    idAcc_Ads = message.text[5:50]
    if len(idAcc_Ads) == 0:
        await update.message.reply_text('⛔ Có vẻ bạn chưa nhập id Ads acc')
    elif len(idAcc_Ads) > 0 and len(idAcc_Ads) < 10:
        await update.message.reply_text('⛔ id Ads Acc bạn nhập là quá ngắn, Vui lòng kiểm tra lại')
    else:
        await update.message.reply_text("🤖 Đang share pixcel cho Ads Acc id: " + idAcc_Ads)
        print(int(message.text[3]))
        idpixel = int(message.text[3])
        res = SharePixel(idAcc_Ads, idpixel)
        await update.message.reply_text(res)


async def getStats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text)
    message = update.message


app = ApplicationBuilder().token("5774231926:AAFwJiyc57wH-UX_Q0sazXZL3gZERhySOUI").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("px1", share))
app.add_handler(CommandHandler("px2", share))
app.add_handler(CommandHandler("px3", share))
app.add_handler(CommandHandler("px3", share))

app.run_polling()