
print("you have chosen the slice function")
print("slice function is used to slice the string")

j1 = input("what is the string?")
j2 = len(j1)
j3 = j1[1 : (j2-1)]
j4 = j1[0 : (j2-2)]
a = (len(j1)) % 2

print(j3)
print(j4)

if a % 2 == 0:
    b = j2/2
    j7 = j1[0 : int(b)]
    j8 = j1[int(b) : int(j2)]
    print(j7)
    print(j8)

elif a % 2 == 1:
    b = (j2-1) / 2
    j7 = j1[0: int(b)]
    j8 = j1[int(b): int(j2)]
    print(j7)
    print(j8)

