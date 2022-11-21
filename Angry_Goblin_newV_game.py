
import random
print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")
name = input("Type in your name:")

print(name + ", do you think you can find the goblin hiding in the kitchen cupboards?")

a = "|_|"
level = input("What level do you choose? [5-50]")
print(a*int(level))


inpt_in = True

while inpt_in:

    inpt = input("Which cupboard do you think the goblin is in [type in number]:")

    randm = random.randint(5,50)

    if int(inpt) == randm:
        print("Well done!! You have found the goblin. He was so scared he ran away.")
        break
    else:
        print("Sorry! The goblin is still lurking somewhere else")