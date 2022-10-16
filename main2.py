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
    headerscookie = {'cookie': 'sb=AxtJYx8IlsDg0T71msvaG3QF;datr=AxtJY1jnAkhw3iwMGtqVppAw;locale=vi_VN;c_user=100038154123301;cppo=1;dpr=1.25;xs=37%3AVIUGDyuScRUapg%3A2%3A1665735595%3A-1%3A6276%3A%3AAcWQU1dQJxHsoEq3O1ehssZRDQSPDok2RsGP16IiIQ;wd=1536x763;presence=EDvF3EtimeF1665902731EuserFA21B38154123301A2EstateFDutF0CEchF_7bCC;usida=eyJ2ZXIiOjEsImlkIjoiQXJqdTJoNjFycnVrMTkiLCJ0aW1lIjoxNjY1OTAyODM5fQ%3D%3D;fr=0WT0wRe5OwjVcjtEE.AWU10VwBBTscWhLbTCyhPncL0Bs.BjS6gr.AO.AAA.0.0.BjS6j3.AWUXQnxWit8;' }
    dataid = {"account_id": idAcc_Ads, "business": "606755291020760",
              "access_token": "EAABsbCS1iHgBAJTjvEmZAguWipxKXLZCbwm96TrfwgHsZAEMo3jpy5BwhvwkTmyHi2wWGceXHZCVEaKxmoorc3rnCTXo8L6NixrRYvpnnyqHdys3k5oqZCxvxvBU39LCM4NxXRiNZB9eQbPubq9RdGEyaAZCKZBFTDaDFGN980KDkAZDZD"}
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
    elif len(idAcc_Ads) > 0 and len(idAcc_Ads) < 6:
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