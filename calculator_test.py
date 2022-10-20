
print("select operation?")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Divide")
inpt = input("enter choice(1/2/3/4): ")


if inpt == '1':
    a = float(input("enter the first number"))
    b = float(input("enter the second number"))
    print(int(a) + int(b))

elif inpt == '2':
    a = float(input("enter the first number"))
    b = float(input("enter the second number"))
    print(int(a) - int(b))

elif inpt == '3':
    a = float(input("enter the first number"))
    b = float(input("enter the second number"))
    print(int(a) * int(b))

elif inpt == '4':
    a = float(input("enter the first number"))
    b = float(input("enter the second number"))
    print(int(a) / int(b))
else:
    print("invalid")