import requests

print('start')
headerscookie = {'cookie': 'sb=o6A7Y8Xfm5pZcjjO5UqGWX38; datr=o6A7Y2XR6IdFQZSAwQrlguoq; c_user=100038154123301; cppo=1; dpr=1; usida=eyJ2ZXIiOjEsImlkIjoiQXJqb3Z1MHp2M3NmZyIsInRpbWUiOjE2NjU2NjA2MzF9; xs=8:aODLzMa7UVIiuA:2:1664852152:-1:6276::AcVQBDjAUETvEgR6YoQPh9lWdmSjNKdELk2AAMzJvdk; fr=0FwVE48LQfBIO8i3r.AWWef5X2XtapL2c80eA42eg7-v8.BjR_es.5T.AAA.0.0.BjR_es.AWVwZgIbksc; presence=C{"t3":[{"i":"u.100009953598724"}],"utc3":1665661151999,"lm3":"u.100034994394353","v":1}; wd=899x977" '}
dataid = { "account_id": "304989770761180", "business": "606755291020760", "access_token" : "EAABsbCS1iHgBAArLduhvb9zgqFFCgZCDAAA8HetB6ZBcDgt5MBvPfyJWXqmvU2TDNfjFnFmTfWrGCusff9mJmM6hLteWrG7ZBsAP5AudXU0KNaRUnWPahFQxZCTk5gHSkmrqIsQ6oegwZCyTBqdLzOzD7zgXntR4jo8epeYeffSwnyN4QGVc8"}
url = "https://graph.facebook.com/v15.0/356037233410519/shared_accounts/"
response = requests.post(url,data=dataid,headers=headerscookie).json()
print(response['success'])
print(response['error']['message'])