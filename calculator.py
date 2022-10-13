
print("select operation?")
print("1.Add")
print("2.Subtract")

inpt = input("enter choice(1/2): ")


if inpt == '1':
    a = float(input("enter the first number"))
    if int(a) < 0:
        print("not valid")
        exit()
    else:
        print("first value is " + str(a))
    b = float(input("enter the second number"))
    if int(b) < 0:
        print("not valid ")
        exit()
    else:
        print("second value is " + str(b))
    print(int(a) + int(b))

elif inpt == '2':
    a = float(input("enter the first number"))
    if int(a) < 0:
        print("not valid")
        exit()
    else:
        print("first value is " + str(a))
    b = float(input("enter the second number"))
    if int(b) < 0:
        print("not valid ")
        exit()
    else:
        print("second value is " + str(b))
    print(int(a) - int(b))
else:
    print("invalid")