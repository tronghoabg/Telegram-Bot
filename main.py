from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import datetime

headerscookie = {'cookie': 'sb=q7VOY8PHXuHh725rVOsTvInf;wd=1920x979;datr=q7VOY_cZnDBBsStiXW6xW9Ef;locale=vi_VN;c_user=100038154123301;xs=34%3AgJIylZH8tZWuvw%3A2%3A1666172784%3A-1%3A6383;fr=0urvl5vtwo12leyL1.AWXmrH354dblxFVYfUTKDf8CYOA.BjT3OR.2B.AAA.0.0.BjT8dx.AWUUrj5R4Dc;usida=eyJ2ZXIiOjEsImlkIjoiQXJqenYzeDFpZnN3Y2giLCJ0aW1lIjoxNjY2MTcyNzkzfQ%3D%3D;cppo=1;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1666172831185%2C%22v%22%3A1%7D;'}

token = "EAABsbCS1iHgBAJmycXTVZADf1VDfzfwcp6IzuqGq63NSZAZBgQGZCH6nWjakXMv3zQOYrW4oS4f10sZAZCtOTCQOnSCpQTOPSZC7Iu3fJVIfA9CnDZAXCgM7AE79t2uoZBUlk0Py1nklA0PyTyNZAnqZB0iLKfajcjQgicnTCu6YPJJUCgOzlV3oZBl9"

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

def Checkcurrli(day):
    payload = {
        'log': 'namvenus',
        'pwd': 'Nam123nam10tr$',
        'wp-submit': 'Log+In'
    }

    today = datetime.datetime.now()
    fday = today - datetime.timedelta(days=day)

    today = today.replace(microsecond=0).isoformat()
    fday = fday.replace(hour=0, minute=0, second=0)
    fday = fday.replace(microsecond=0).isoformat()

    after = fday
    before =  today

    session = requests.Session()
    res = session.post('https://curilic.com/wp-login.php/', data=payload)
    res = session.get('https://curilic.com/wp-admin/admin.php?page=wc-admin&path=%2Fanalytics%2Foverview')
    res = res.text
    wpcookie = res[int(res.find('createNonceMiddleware( "')) + 24: int(res.find('createNonceMiddleware( "')) + 34]
    print(wpcookie)
    headerwp = {'x-wp-nonce': wpcookie}
    reponse = session.get(
        'https://curilic.com/wp-json/wc-analytics/reports/performance-indicators?after=' + after + '&before=' + before + '&stats=revenue/total_sales,revenue/net_revenue,orders/orders_count,orders/avg_order_value,products/items_sold,revenue/refunds,coupons/orders_count,coupons/amount&_locale=user',
        headers=headerwp).json()
    print(reponse)
    timeline = "Từ : " + after + '\n'\
            + 'Đến: ' + before + '\n\n'\
            '-------OVER VIEW-------\n'
    res = timeline + '\n'\
          +  reponse[0]['label'] + ': ' + str(round(reponse[0]['value'], 2)) + '\n' \
          + reponse[1]['label'] + ': ' + str(round(reponse[1]['value'], 2)) + '\n' \
          + reponse[2]['label'] + ': ' + str(round(reponse[2]['value'], 2)) + '\n' \
          + reponse[3]['label'] + ': ' + str(round(reponse[3]['value'], 2)) + '\n' \
          + reponse[4]['label'] + ': ' + str(round(reponse[4]['value'], 2)) + '\n' \
          + reponse[5]['label'] + ': ' + str(round(reponse[5]['value'], 2)) + '\n' \
          + reponse[6]['label'] + ': ' + str(round(reponse[6]['value'], 2)) + '\n' \

    return res


async def CheckRev(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text)
    message = update.message.text

    if message[4:6].isnumeric():
        day = int(message[4:6])
        res = Checkcurrli(day)
        await  update.message.reply_text(res)
    else:
        await  update.message.reply_text('⛔ sai cú pháp , get all revalue /cu , or get x day /cu x ( day = now - x')

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
app.add_handler(CommandHandler("cu", CheckRev))

app.run_polling()