
print("you have chosen the slicing function")
print("slice function is used to slice the list")

j1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    inpt = input()

    j1.append(inpt)

print(j1)
print("you entered :" + str(j1))
j2 = len(j1)
j3 = j1[1: (j2-1)]
j4 = j1[2: j2]
j5 = j1[0: (j2-2)]
a = (len(j1)) % 2

print("Slice of " + str(j1) + " after removing first and last values " + str(j3))
print("Slice of " + str(j1) + " after removing first two values " + str(j4))
print("Slice of " + str(j1) + " after removing last two values " + str(j5))

if a == 0:
    b = j2/2
    print("mid index is " + str(b))
    j7 = j1[0: int(b)]
    j8 = j1[int(b): int(j2)]
    print("First half of the slice is : " + str(j7))
    print("Second half of the slice is : " + str(j8))

elif a == 1:
    b = (j2-1) / 2
    print("mid index is " + str(b))
    j6 = j1[0: int(b)]
    j9 = j1[int(b): int(j2)]
    print("First half of the slice is : " + str(j6))
    print("Second half of the slice is : " + str(j9))
