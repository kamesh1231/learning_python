def quot(x, y):
    quot1 = int(x) // int(y)
    print(quot1)


print("enter first input")
a = input()
if int(a) < 0:
    print("not valid")
    exit()
else:
    print("first value is " + a)
print("enter second input")
b = input()
if int(b) < 0:
    print("not valid ")
    exit()
else:
    print("second value is " + b)

quot(a, b)