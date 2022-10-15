import requests


headerscookie = {'cookie': 'sb=dy84Y2L5FR505BCjz5oatByb;datr=dy84Y39bGrlDwusArObAqw-q;c_user=100038154123301;cppo=1;dpr=1;presence=EDvF3EtimeF1665852199EuserFA21B38154123301A2EstateFDutF0CEchF_7bCC;xs=30%3Av4fb68UbILEtCg%3A2%3A1665756748%3A-1%3A6276%3A%3AAcW6kIyJPKAy44PWjRfJ_fR94JJo-XdDUzpxYCwrdg;wd=1920x937;usida=eyJ2ZXIiOjEsImlkIjoiQXJqdDJzNzgxdHAxdiIsInRpbWUiOjE2NjU4NTc2OTF9;fr=00sKONM56GGtwnxmg.AWX6e_vOnrykbchW4lO-T11mBb8.BjSvJV.Hb.AAA.0.0.BjSvib.AWWH7I0jiro;' }

pram = {"aggregation": "event_total_counts", "access_token": "EAAQUZAS3L8KIBAAFbeCYABcDrKal6keOlh9vokwGTAVTc2grXNAFxAno7qUkFd0QDOM3s0sgmZCDsnyt6Qtet4eYJ70LXFXVZCx7L7ZBpbPbQmc5rHOKUEqc20OiEFEJsGcaRZAmab3DIoUoLzTgRC3Kt5wktk4olKqCITGQ8dSF0p8vwO4L0sINDe9vi1pcqTeAyZBlI1Cy9GdZA6Badwfv5VsUFpdZCT1YxDW9O2yizypkLLeCPAiA"}
#url = "https://graph.facebook.com/v15.0/" + dictPixel[idPixel]['id'] +"/stats?"


url = "https://graph.facebook.com/v15.0/449542583803743/stats"

a = requests.get(url, params=pram, headers=headerscookie)


print(a)