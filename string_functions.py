inpt = input("choose between a-k")
if inpt == 'a':
      print("you have chosen the capitalize function")
      print("capitalize function converts the first character to upper case ")
      a1 = input("what is the string?")
      a2 = a1.capitalize()
      print(a2)

elif inpt == 'b':
      print("you have chosen the casefold function")
      print("casefold function converts string into lowercase")
      b1 = input("what is the string?")
      b2 = b1.casefold()
      print(b2)

elif inpt == 'c':
      print("you have chosen the center function")
      print("capitalize function returns a centered string ")
      c1 = input("what is the string?")
      c2 = c1.center(int(input("what is the number?")))
      print(c2)

elif inpt == 'd':
      print("you have chosen the count function")
      print("Count function returns the number of times a specified value occurs in a string")
      d1 = input("what is the string?")
      d2 = d1.count(input("what is the character?"))
      print(d2)

elif inpt == 'e':
      print("you have chosen the endswith function")
      print("Endswith function returns true if the string ends with the specified value")
      e1  = input("what is the string?")
      e2 = e1.endswith(input("what string?"))
      print(e2)

elif inpt == 'f':
      print("you have chosen the find function")
      print("find function Searches the string for a specified value and returns the position of where it was found")
      f1 = input("what is the string?")
      f2 = f1.find(input("which one?"))
      print(f2)

elif inpt == 'g':
      print("you have chosen the format function")
      print("format function Formats specified values in a string")
      inpt1 = input("1 or 2")
      if inpt1 == '1':
            g1 = input("what is the string?")
            g2 = g1.format(input("what is the format?"))
            print(g2)
      elif inpt1 == '2':
            g1 = input("what is the string?")
            g2 = g1.format(input("what is the format?"), input("what is the format?"))
            print(g2)
      else:
            print("unknown")

elif inpt == 'h':
      print("you have chosen the index function")
      print("index function Searches the string for a specified value and returns the position of where it was found")
      h1 = input("what is the string?")
      h2 = h1.index(input("what is the character?"))
      print(h2)

elif inpt == 'i':
      print("you have chosen the split function")
      print("split function Splits the string at the specified separator, and returns a list")
      i1 = input("what is the string?")
      i2 = i1.split()
      print(i2)

elif inpt == 'j':
      print("you have chosen the slice function")
      print("slice function is used to slice the string")
      j1 = input("what is the string?")
      j2 = j1[int(input("what is start")):int(input("what is end"))]
      print(j2)

elif inpt == 'k':
      print("you have chosen the partition function")
      print("partition function splits the string into a tuple containing three elements")
      k1 = input("what is the string?")
      k2 = k1.partition(input("which substring?"))
      print(k2)

else:
      print("unknown")