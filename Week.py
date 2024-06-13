num = int(input('Enter number(0<= num >= 6):'))

if(num == 0):
    print("Monday" , end = " ")
elif num == 1:
    print("Tuesday", end = " ")
elif num == 2:
    print("Wednesday", end = " ")
elif num == 3:
    print("Thursday" , end = " ")
elif num == 4:
    print("Friday", end = " ")
elif num == 5:
    print("Saturday", end = " ")
elif num == 6:
    print("Sunday", end = " ")
else:
    print("Invalid Input", end = " ")