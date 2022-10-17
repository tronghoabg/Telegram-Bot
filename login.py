import requests
from bs4 import BeautifulSoup
payload = {'log': 'Namvenus', 'pwd': 'Namvenus@1268'}
url = 'https://curilic.com/wp-login.php'

session = requests.Session()
session.post(url, data=payload)
html = session.get('https://curilic.com/wp-admin/admin.php?page=wc-admin&path=%2Fanalytics%2Foverview&period=custom&compare=previous_year&after=2022-10-13&before=2022-10-16')

soup = BeautifulSoup(html.content, "html.parser")

#result = soup.find_all("span", "components-truncate")
print(soup)
