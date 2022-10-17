import requests


headerscookie = {'cookie': 'sb=dy84Y2L5FR505BCjz5oatByb;datr=dy84Y39bGrlDwusArObAqw-q;c_user=100038154123301;cppo=1;dpr=1.25;presence=C%7B%22t3%22%3A%5B%7B%22i%22%3A%22u.100034994394353%22%7D%5D%2C%22utc3%22%3A1665858954842%2C%22lm3%22%3A%22u.100082234812595%22%2C%22v%22%3A1%7D;xs=30%3Av4fb68UbILEtCg%3A2%3A1665756748%3A-1%3A6276%3A%3AAcX9rcAm2lppj1GCqE2iYZKQp1_1BO0CN1uEZeCpUg;wd=1920x937;usida=eyJ2ZXIiOjEsImlkIjoiQXJqdDJzNzgxdHAxdiIsInRpbWUiOjE2NjU4NjAxNzZ9;fr=0BUeI3o0kWzt9fSoc.AWVaGCl1pIPsUSRJIa8DyUXZYSs.BjSwHC.Hb.AAA.0.0.BjSwKn.AWUz6mjslNA;' }
pram = {"aggregation": "event_total_counts", "access_token": "EAAQUZAS3L8KIBAM92XzELnwtmAqYKYZCQiY9jTeLqHI2p5LE1aYlOelHPP6a4OdtiB2c2GmJFrmoOhIzZCvJte5Qb95k5oZBcRx1k9DrQcYcXDYm3Yrc6GQTwMWGOAVvTvXKVbfXBdMs9BtUaJK0dSlJpdZAL4ZB6JU9hd4DUlXYyRcqdh4SFwslltVvvPOiIRu23BpeXdZBH3iVZA3cq3r9Rt4VoJhZAZAGNQI66ZCjusTLy2xVz1PL8S5"}
url = "https://graph.facebook.com/v15.0/449542583803743/stats"
res = requests.get(url, params=pram,  headers=headerscookie).json()

print(res)