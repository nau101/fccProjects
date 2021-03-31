from datetime import datetime, timedelta

start = "6:30 PM"
duration = "6:12"
dow = "tuesday"


dW = None


weekd = {"Monday": 0, "Tuesday": 1, "Wednesday" : 2, "Thursday" : 3 , "Friday" : 4, "Saturday" : 5, "Sunday" : 6 }

aT = duration.split(':')    
dS = datetime.strptime(start,'%I:%M %p')

h = int(aT[0])
m = int(aT[1])

xp = timedelta(hours=h,minutes=m) 


if dow != None:
    wStart = start+" "+dow
    print(wStart)
    for k,v in weekd.items():
        if k.lower() == dow.lower():
            dS = datetime.strptime(wStart,'%I:%M %p %A')    
            dW = dS.weekday() + v
        if dW == v:
            wday = k



ntime = dS + xp 

newtime = ntime.strftime('%I:%M %p')

print(newtime, wday)
