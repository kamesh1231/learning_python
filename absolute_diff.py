# get the first number
# print(enter first input)
x = input("enter first input")
print("first value is" + x)
y = input("enter second input")
print("second value is" + y)
# sub the numbers and store the results
print("results")
z = (int(x) - int(y))
if z < 0:
    print(-z)
else:
    print(z)