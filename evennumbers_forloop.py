a = input("Enter a number:")
print("you entered <" +a +">")
b = input("How many odd numbers you wish to print?")
print("Printing " +b + " odd numbers after " +a)
if int(a) % 2 == 1:
    c = int(a) + 1
    i = 0
    for i in range(int(b)):
        print(c)
        i+=1
        c+=2

elif int(a) % 2 == 0:
    c = int(a) + 2
    i = 0
    for i in range(int(b)):
        print(c)
        i+=1
        c+=2