import requests
import datetime

payload = {
'log':'namvenus',
'pwd':'Nam123nam10tr$',
'wp-submit':'Log+In'
}
after = '2022-10-01T00:00:00'
before = datetime.datetime.now().replace(microsecond=0).isoformat()

session = requests.Session()
res = session.post('https://curilic.com/wp-login.php/', data=payload)
res = session.get('https://curilic.com/wp-admin/admin.php?page=wc-admin&path=%2Fanalytics%2Foverview')
res = res.text
wpcookie = res[int(res.find('createNonceMiddleware( "')) + 24 : int(res.find('createNonceMiddleware( "')) + 34]
print(wpcookie)
headerwp = {'x-wp-nonce':wpcookie}
reponse = session.get('https://curilic.com/wp-json/wc-analytics/reports/performance-indicators?after='+ after + '&before=' + before + '&stats=revenue/total_sales,revenue/net_revenue,orders/orders_count,orders/avg_order_value,products/items_sold,revenue/refunds,coupons/orders_count,coupons/amount&_locale=user',headers=headerwp).json()
print(reponse)
res = reponse[0]['label'] + ': ' +  str(round(reponse[0]['value'],2)) + '\n'\
        + reponse[1]['label'] + ': ' +  str(round(reponse[1]['value'],2)) + '\n'\
        + reponse[2]['label'] + ': ' + str(round(reponse[2]['value'],2)) + '\n'\
        + reponse[3]['label'] + ': ' + str(round(reponse[3]['value'],2)) + '\n'\
        + reponse[4]['label'] + ': ' + str(round(reponse[4]['value'],2)) + '\n'\
        + reponse[5]['label'] + ': ' + str(round(reponse[5]['value'],2)) + '\n'\
        + reponse[6]['label'] + ': ' + str(round(reponse[6]['value'],2)) + '\n'\

print(res)
