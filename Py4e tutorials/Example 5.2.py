largest = None
smallest = None
print("Please enter a sequence of numbers to determine the highest and lowest! Type 'done' when completed")

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num=int(num)
        if num == 420 or num==69:
            print( "nice nice nice")
    except:
        print("Invalid input")
        continue
    for i in [num]:
        if smallest is None:
            smallest = i
        elif i < smallest:
            smallest = i
        if largest is None:
            largest= i
        elif i > largest:
            largest = i

print("Maximum is", largest)
print("Minimum is", smallest)
