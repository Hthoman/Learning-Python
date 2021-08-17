#Write a program to pront for hours and rate per hour to calculate gross pay

h= input("enter the hours you worked:") #ask for hours
r= input ("enter your hourly rate:" ) #ask for rate
pay=0


def computepay(hours, rate):
    if hours < 40:
        print('normal rate')
        pay = hours*rate
    else:
         print('overtime rate')
         pay = hours*(rate*1.5)
    return pay
    
    

try:    #check for if the user entered numeric values 
    h= float(h) #convert hours to float
    r= float(r)  #convert rate to float
except:
    print( "Error Please enter numeric input")
    quit()
    
pay=computepay(h,r)

print("your gross pay is ", pay)  #print the result 

