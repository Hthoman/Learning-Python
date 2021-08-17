#Write a program to pront for hours and rate per hour to calculate gross pay

hours= input("enter the hours you worked:") #ask for hours
rate= input ("enter your hourly rate:" ) #ask for rate

hours= float(hours) #convert hours to float
rate= float(rate)  #convert rate to float

if hours > 40:   #determine if overtime is worked
    pay= hours* (rate*1.5)  # pay exttra for overtime 
    print("overtime rate")  #notify user 
    
    
else:                 #normal work rate condition 
    print("Normal Rate")
    pay= hours*rate #calculate gross pay

print("your gross pay is ", pay)  #print the result 

