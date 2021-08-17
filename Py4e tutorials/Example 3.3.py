#grade example

grade=input("Please enter your grade on a scale of 0.0 to 1.0")
grade=float(grade)
            
            
if grade > 1 or grade < 0:
            print(" please enter correct score")
            quit()
elif grade >= 0.9:
    print("your grade is a A")
elif grade >= 0.8:
    print("your grade is a B")
elif grade >= 0.7:
     print("your grade is a C")
elif grade >= 0.6:
     print("your grade is a D")
elif  grade < 0.6:
     print("your grade is a F")
