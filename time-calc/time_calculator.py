from datetime import datetime, timedelta

def add_time(strt, dur, weekd=""):
  
    start = strt
    duration = dur
    dow = weekd

    answer = str()
    dW = int()
    wday = str()
    day = int()
  
    weekd = {"Monday": 0, "Tuesday": 1, "Wednesday" : 2, "Thursday" : 3 , "Friday" : 4, "Saturday" : 5, "Sunday" : 6 }

    aT = duration.split(':')    
    dS = datetime.strptime(start,'%I:%M %p')

    h = int(aT[0])
    m = int(aT[1])

    xp = timedelta(hours=h,minutes=m) 
    ntime = dS + xp 
    ltime = ntime.strftime('%I:%M %p')

    if ltime[0] == '0':
        newtime = ltime.replace('0','',1)
    else:   
        newtime = ltime
    


    if dow:
        wStart = start+" "+dow
        for k,v in weekd.items():
            if k.lower() == dow.lower():
                dS = datetime.strptime(wStart,'%I:%M %p %A')    
                dW = dS.weekday() + v            
                day = (dW + ntime.day - 1) % 7
            if day == v: 
                wday = k 

        if ntime.day == 0 or ntime.day == 1:
            answer = newtime+', '+wday 
        elif ntime.day == 2: 
            answer = newtime+', '+wday+' (next day)' 
        elif  ntime.day > 2: 
            answer = newtime +', '+wday+' ({} days later)'.format(ntime.day-1)
        
        return answer
    

    if ntime.day == 0 or ntime.day == 1:
        return newtime

    elif ntime.day == 2: 
        answer = newtime +' (next day)' 
        return answer

    elif ntime.day > 2: 
        answer = newtime + ' ({} days later)'.format(ntime.day-1)
        return answer






