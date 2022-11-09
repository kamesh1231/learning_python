def calculator_test():
    print("select operation?")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiplication")
    print("4.Divide")
    print("5.Modulus")
    print("6.quotient")
    print("7.exponential")

inpt = input("enter choice(1/2/3/4/5/6/7): ")


if inpt == '1':
    a = input("enter the first number")
    if int(a) < 0:
        print("not valid")
        exit()
    else:
        print("first value is " + a)
    b = input("enter the second number")
    if int(b) < 0:
        print("not valid ")
        exit()
    else:
        print("second value is " + b)
    print(int(a) + int(b))

elif inpt == '2':
    a = input("enter the first number")
    if int(a) < 0:
        print("not valid")
        exit()
    else:
        print("first value is " + a)
    b = input("enter the second number")
    if int(b) < 0:
        print("not valid ")
        exit()
    else:
        print("second value is " + b)
    print(int(a) - int(b))
elif inpt == '3':
    a = input("enter the first number")
    if int(a) < 0:
        print("not valid")
        exit()
    else:
        print("first value is " + a)
    b = input("enter the second number")
    if int(b) < 0:
        print("not valid ")
        exit()
    else:
        print("second value is " + b)
    print(int(a) * int(b))
elif inpt == '4':
    a = input("enter the first number")
    if int(a) < 0:
        print("not valid")
        exit()
    else:
        print("first value is " + a)
    b = input("enter the second number")
    if int(b) < 0:
        print("not valid ")
        exit()
    else:
        print("second value is " + b)
    print(int(a) / int(b))
elif inpt == '5':
    a = input("enter the first number")
    if int(a) < 0:
        print("not valid")
        exit()
    else:
        print("first value is " + a)
    b = input("enter the second number")
    if int(b) < 0:
        print("not valid ")
        exit()
    else:
        print("second value is " + b)
    print(int(a) % int(b))
elif inpt == '6':
    a = input("enter the first number")
    if int(a) < 0:
        print("not valid")
        exit()
    else:
        print("first value is " + a)
    b = input("enter the second number")
    if int(b) < 0:
        print("not valid ")
        exit()
    else:
        print("second value is " + b)
    print(int(a) // int(b))
elif inpt == '7':
    a = input("enter the first number")
    if int(a) < 0:
        print("not valid")
        exit()
    else:
        print("first value is " + a)
    b = input("enter the second number")
    if int(b) < 0:
        print("not valid ")
        exit()
    else:
        print("second value is " + b)
    print(int(a) ** int(b))
else:
    print("invalid")


calculator_test()