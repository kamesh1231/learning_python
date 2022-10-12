def sum(x, y):
    sum1 = int(x) + int(y)
    print(sum1)


while True:
    print("enter first input")
    a = input()
    print("enter second input")
    b = input()
    if int(a) < 0:
        print("invalid")
        exit()
    elif int(b) < 0:
        print("invalid")
        exit()
    else:
        print(sum(a,b))