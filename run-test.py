import datetime


today =  datetime.datetime.now()
today = today.replace(hour=0, minute = 0, second = 0 )
fday =   today - datetime.timedelta(days=30)

#tdnew =  datetime.datetime.now() +  datetime.timedelta(days=-1)


print(today, fday)



