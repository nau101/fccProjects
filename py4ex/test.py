from datetime import datetime, timedelta

start = "6:30 PM"
duration = "205:12"
dow = ''

dS = datetime.strptime(start,'%I:%M %p')
aT = duration.split(':')

h = int(aT[0])
m = int(aT[1])

xp = timedelta(hours=h,minutes=m)

ntime = dS + xp

newtime = ntime.strftime('%I:%M %p')

print(newtime)
