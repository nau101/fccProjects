def computepay(h,r):
    ep = 0
    
    if h > 40:
        et = h - 40
        np = 40 * r
        ep = et*r*1.5
	tp = np + ep
    else:
	tp = h*r		

        
    return tp

hrs = input("Enter Hours:")
rate = input("Enter rate:")
a = float(hrs)
b = float(rate)
p = computepay(a,b)
print("Pay",p)
