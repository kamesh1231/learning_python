def sum(x, y):
    sum1 = int(x) + int(y)
    print(sum1)


print("enter first input")
a = input()
if int(a) < 0:
    print("not valid")
else:
    print("first value is " + a)
print("enter second input")
b = input()
if int(b) < 0:
    print("not valid")
else:
    print("second value is " + b)


sum(a, b)


