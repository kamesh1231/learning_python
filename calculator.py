
print("select operation?")
print("1.Add")
print("2.Subtract")

inpt = input("enter choice(1/2): ")


if inpt == '1':
    a = float(input("enter the first number"))
    b = float(input("enter the second number"))
    print(int(a) + int(b))

elif inpt == '2':
    a = float(input("enter the first number"))
    b = float(input("enter the second number"))
    print(int(a) - int(b))
else:
    print("invalid")