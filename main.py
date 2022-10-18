from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

headerscookie = {'cookie': 'sb=q7VOY8PHXuHh725rVOsTvInf;wd=1920x979;datr=q7VOY_cZnDBBsStiXW6xW9Ef;c_user=100038154123301;xs=21%3AENJvFHNmbKlu7A%3A2%3A1666102705%3A-1%3A6383;fr=0Av79RAfphWeAqNME.AWWEUQ0T-P0beKPCIOGI6ioYOyk.BjTrWr.2B.AAA.0.0.BjTrWz.AWUlgidyNR0;cppo=1;presence=EDvF3EtimeF1666102803EuserFA21B38154123301A2EstateFDutF0CEchF_7bCC;usida=eyJ2ZXIiOjEsImlkIjoiQXJqeWQ0bzFjcG02MCIsInRpbWUiOjE2NjYxMDI5MDl9;'}
token = "EAABsbCS1iHgBAOUpNE8uFkJkqMJ0Wt9H8iLiKk5o07M37DVWKNcXM7srzwQNuJBlQ1b2aitz0wlFJKESu1fHuvhZA9vZBW7SdRRJwEkHxlU9rt0COHu22lBR0vYVUMEXZC8YFAlgUlZCF8lIT5RwRmzDr43JZBu36vQVb3Nkaz7U5sqHib8Gk"

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
    dataid = {"account_id": idAcc_Ads, "business": "606755291020760",
              "access_token": token}
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

def getStats(idPixel, flagstat):
    pram = {"aggregation": "event_total_counts",
            "access_token": token}
    url = "https://graph.facebook.com/v15.0/" + dictPixel[idPixel]['id'] + "/stats"
    resstock = requests.get(url, params=pram, headers=headerscookie).json()
    starttime = "Form time: "  + resstock['data'][0]['start_time'][0:10]  + ' | ' + resstock['data'][0]['start_time'][11:19]

    res =       starttime  + '\n'\
            + resstock['data'][0]['data'][0]['value'] + ': ' + str(resstock['data'][0]['data'][0]['count']) + '\n'\
            + resstock['data'][0]['data'][1]['value'] + ': ' + str(resstock['data'][0]['data'][1]['count']) + '\n'\
            + resstock['data'][0]['data'][3]['value'] + ': ' + str(resstock['data'][0]['data'][3]['count']) + '\n'\
            + resstock['data'][0]['data'][6]['value'] + ': ' + str(resstock['data'][0]['data'][6]['count']) + '\n' \
            + resstock['data'][0]['data'][7]['value'] + ': ' + str(resstock['data'][0]['data'][7]['count']) + '\n' \
            + resstock['data'][0]['data'][8]['value'] + ': ' + str(resstock['data'][0]['data'][8]['count']) + '\n' \

    print(resstock)
    return res

async def stat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text)
    message = update.message



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def share(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text)
    message = update.message
    idAcc_Ads = message.text[5:50]
    idpixel = int(message.text[3])
    flagStat = message.text[5:9]

    if flagStat == "info":
        res = getStats(idpixel, flagStat)
        await update.message.reply_text(res)
        exit()
    print(idAcc_Ads)
    if len(idAcc_Ads) == 0:
        await update.message.reply_text('⛔ Có vẻ bạn chưa nhập id Ads acc')
    elif len(idAcc_Ads) > 0 and len(idAcc_Ads) < 6:
        await update.message.reply_text('⛔ id Ads Acc bạn nhập là quá ngắn, Vui lòng kiểm tra lại')
    else:
        await update.message.reply_text("🤖 Đang share pixcel cho Ads Acc id: " + idAcc_Ads)
        print(int(message.text[3]))
        res = SharePixel(idAcc_Ads, idpixel)
        await update.message.reply_text(res)






app = ApplicationBuilder().token("5774231926:AAFwJiyc57wH-UX_Q0sazXZL3gZERhySOUI").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("px1", share))
app.add_handler(CommandHandler("px2", share))
app.add_handler(CommandHandler("px3", share))
app.add_handler(CommandHandler("px3", share))


app.run_polling()