from sys import stdout
import requests, os
import socket
from time import sleep
import os
from termcolor import colored
from bs4 import BeautifulSoup
import time
from datetime import datetime
import pytz

os.system('clear')

ip = socket.gethostbyname(socket.gethostname())
# id acc cần gửi tn
id = '100021668201187'
while True:
    # cookie
    ck = 'datr=bfEqY7HBnL1BlQanMtYvlYIZ;sb=bfEqY7P9-nYN-oyfYk5OUPBi;locale=vi_VN;vpd=v1%3B660x360x2;m_pixel_ratio=2;fr=0Y4t7Q8EB37OYvpMu.AWWG09Ew0JWMzu3k2tzkl0DSJ48.BjKvFt.GF.AAA.0.0.BjKwLC.AWXrhwXOW7U;c_user=100085280666438;xs=20%3Ao64a2eTEnnMZ8w%3A2%3A1663763138%3A-1%3A-1;wd=360x660;'
    try:
        get = requests.get(
            f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile', headers={
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 'cookie': ck,
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
                'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1'}).text
        fb_dtsg = get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest = get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        break
    except:
        print('Cookie sai!!')
os.system('clear')
nd = 'hi'
time.sleep(0.3)

headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    # Requests sorts cookies= alphabetically
    'cookie': ck,
    'origin': 'https://m.facebook.com',
    'referer': 'https://www.facebook.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}

params = {
    'icm': '1',
}

data = {
    f'ids[{id}]': id,
    'body': nd,
    'waterfall_source': 'message',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
}
// gửi
tin
nhắn
response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=data)
print(f' Send Success | {nd}')