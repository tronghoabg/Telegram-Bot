import requests
session = requests.Session()

ck =  'sb=q7VOY8PHXuHh725rVOsTvInf;datr=q7VOY_cZnDBBsStiXW6xW9Ef;locale=vi_VN;wd=1920x979;c_user=100038154123301;usida=eyJ2ZXIiOjEsImlkIjoiQXJrMng4OTFmb2tvNjUiLCJ0aW1lIjoxNjY2MzE1NDUzfQ%3D%3D;cppo=1;presence=C%7B%22t3%22%3A%5B%7B%22i%22%3A%22u.100082158890658%22%7D%2C%7B%22i%22%3A%22u.100034994394353%22%7D%2C%7B%22i%22%3A%22u.6188525697828138%22%7D%2C%7B%22i%22%3A%22u.6523795057647064%22%7D%5D%2C%22utc3%22%3A1666348115441%2C%22lm3%22%3A%22u.100021668201187%22%2C%22v%22%3A1%7D;xs=34%3Aapf7xbjm0POOCw%3A2%3A1666191978%3A-1%3A6383%3A%3AAcVBjc8zj2ib7ONXmwpzfZGjTX8g171Gt5Dj1KUlmfw;fr=0FRzbLTfkEbQAYDGp.AWVlZE7ixZw5l7j1QDrJV-4Kbd4.BjUpsG.2B.AAA.0.0.BjUpsG.AWXl62cQSEc;'

headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    'cookie': ck,
    'origin': 'https://m.facebook.com',
    'referer': 'https://www.facebook.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}


home = requests.get('https://business.facebook.com/adsmanager/manage/accounts',  headers=headers).text
uid_page = home.split('adAccountId: \\"')[1].split('\\"')[0]
ads_page = requests.get(f'https://business.facebook.com/adsmanager/manage/accounts?act={uid_page}',headers=headers).text
token = ads_page.split('window.__accessToken="')[1].split('"')[0]


print(token)


