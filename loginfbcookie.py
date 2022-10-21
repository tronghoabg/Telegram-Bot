import requests
session = requests.Session()


ck =  'asb=o6A7Y8Xfm5pZcjjO5UqGWX38; datr=o6A7Y2XR6IdFQZSAwQrlguoq; dpr=1; locale=vi_VN; c_user=100038154123301; xs=29:nqMj4yk1dnFfvQ:2:1666191960:-1:6383::AcURmmHsQt7laCf8tCcWzG4WljZpmLjbeX5iuFbbKA; presence=C{"t3":[],"utc3":1666203154895,"lm3":"u.100034994394353","v":1}; wd=1855x384; fr=0DmKkXdZHs130YnYV.AWWwtyMrX927arWfj4cSRTEasOE.BjUDE_.5T.AAA.0.0.BjUEAV.AWVrU0Gb6D4'
coki2 = {
    'cookie':'sb=o6A7Y8Xfm5pZcjjO5UqGWX38; datr=o6A7Y2XR6IdFQZSAwQrlguoq; dpr=1; locale=vi_VN; c_user=100038154123301; xs=29:nqMj4yk1dnFfvQ:2:1666191960:-1:6383::AcVoDqvuWZoF4I8U5lP_hLCxYKwtGVjITDg0YR8l5Q; fr=0MJI7wnuKpSweJfd8.AWWfEiF1BHaEn_AySuJ5TMlzh_w.BjUEAZ.5T.AAA.0.0.BjUEAZ.AWXrkNyQFzA; presence=C{"t3":[],"utc3":1666203678812,"lm3":"u.100034994394353","v":1}; wd=1858x384'
}

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


response = session.get('https://business.facebook.com/', headers=headers)

#response = session.get('https://business.facebook.com/home/accounts/', headers=headerck)

print(response.text)