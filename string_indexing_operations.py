print("you have chosen the index function")
print("index function Searches the string for a specified value and returns the position of where it was found")
h1 = input("what is the string?")
print("You entered :" + h1)
h2 = h1[0]
h3 = h1[len(h1)-1]
a = (len(h1)) % 2
print("The first alphabet of the string is : " + h2)
print("The last alphabet of the string is : " + h3)
print("The length of the string is :  " + str(len(h1)))

if a == 1:
    b = int(len(h1)/2)
    print("mid index is " +str(b))
    h4 = h1[b]
    print("The middle character is : " + h4)

elif a == 0:
    b = int(len(h1) / 2)
    print("mid index is " + str(b))
    h5 = h1[b - 1]
    h6 = h1[b]
    print("The middle character is : " + h5 + " and " + h6)