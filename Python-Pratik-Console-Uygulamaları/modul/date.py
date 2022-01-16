import datetime 

simdi=datetime.datetime.now()
result=simdi.now()
result=simdi.day
result=simdi.month
result=simdi.year   
result=simdi.hour    

result=simdi.ctime()
result=simdi.strftime("%Y")
result=simdi.strftime("%m")
result=simdi.strftime("%Y %m %d")

# t="29 April 2021 saat 12:12:30" 
# dt=simdi.strptime(t,"%d %m %Y hour %H:%M:%S")
# print(t)

result=simdi+datetime.timedelta(days=10,minutes=500) # tarihi arttırır
result=simdi-datetime.timedelta(days=20)
print(result)