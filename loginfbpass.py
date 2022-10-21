import requests
import datetime


session = requests.Session()
res = session.get('https://mbasic.facebook.com')
res = res.text
cookieoutsite = session.cookies.get_dict()
cookieoutsite = 'datr=' + cookieoutsite['datr'] +'; sb=' +cookieoutsite['sb']
lsd = res[int(res.find('name="lsd"')) + 18 : int(res.find('name="lsd"')) + 29]


headercookie = {'cookie': cookieoutsite}

payload = {
'email':'tronghoabg@icloud.com',
'pass':'xxxxxx!',
'lsd': lsd
}




res = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8', data=payload)

print(cookieoutsite)
print(lsd)


print(res.text)


