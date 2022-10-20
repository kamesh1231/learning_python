x = input("what is your year?")

if float(x) % 400 == 0:
    print(x + ' is a leap year as it is divisible by 400')
elif float(x) % 100 == 0:
    print(x + ' is not a leap year as it is divisible by 100 and not by 400')
elif float(x) % 4 == 0:
    print(x + ' is a leap year as it is divisible by 4 but not by 100 and by 400')
else:
    print('not a leap year')