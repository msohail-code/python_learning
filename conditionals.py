a=3
b=5

'''

if a==b:
    print("matched")
elif a==1:
    print("a is",a)
else:
    print("not matched")

if a==3 and b!=2:
    print("we found it")

'''

arr = ['Monday', 'Tuesday', 'wednesday', "thursday", "friday", "saturday","sunday"]

day = int(input("Enter day#:"))

if day>0 and day<8:
    print(arr[day-1])
else:
    print("Invalid input")


    


