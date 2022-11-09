def sub(x, y):
    sub1 = int(x) - int(y)
    print(sub1)

a = input("please input first number")
while int(a) < 0:
    print("invalid format")
    input("Please input first number again")
    if int(a) > 0:
      break
    print(a)
b = input("please input second number")
if int(b) < 0:
    print("invalid format")
else:
   print(b)

sub(a, b)