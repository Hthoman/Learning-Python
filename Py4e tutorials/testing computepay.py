
def computepay():
    if overtime==False:
       pay=hours*rate
    elif overtime==True:
        pay= hours* (rate*1.5)
    return pay

hours=1
rate=2
overtime=False
computepay()
