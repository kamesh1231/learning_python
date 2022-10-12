def add(x,y):
    add1 = int(x) + int(y)
    print(add1)

def subtract(x,y):
    subtract1 = int(x) - int(y)
    print(subtract1)

print("select operation?")
print("1.Add")
print("2.Subtract")

while True:
    inpt = input("enter choice(1/2): ")
    if inpt in('1', '2'):
        a = float(input("enter the first number"))
        b = float(input("enter the second number"))

        if inpt == '1':
            print(add(a,b))
        elif inpt == '2':
            print(subtract(a,b))
        else:
            print("invalid")