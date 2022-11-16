print("you have chosen the index function")
print("index function Searches the string for a specified value and returns the position of where it was found")

h1 = []
n = int(input("Enter number of values : "))
for i in range(0, n):
    inpt = input()

    h1.append(inpt)

print(h1)
print("your list is " +str(h1))
h2 = h1[0]
h3 = h1[len(h1)-1]
a = (len(h1)) % 2
print("The first value of the list is : " + str(h2))
print("The last alphabet of the list is : " + str(h3))
print("The length of the list is :  " + str(len(h1)))

if a == 1:
    h4 = h1[int(len(h1)/2)]
    print("The middle value is : " + str(h4))

elif a == 0:
    h5 = h1[int((len(h1)/2) - 1)]
    h6 = h1[int(len(h1) / 2)]
    print("The middle value is : " + str(h5) + " and " + str(h6))

