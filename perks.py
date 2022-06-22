import random
import csv

s_perks = ['Dead Hard', 'Lithe', 'Head On', 'Better Together', 'Bond', 'Inner Strength','Up the Ante']
#k_perks = ['No Escape', 'Bitter Murmur','Iron Grasp','Beast of Prey','Brutal Strength','Lightborn','Shadowborn']



file = open("killer_perks.csv", "r")
csv_reader = csv.reader(file)

k_perks = []
for row in csv_reader:
    k_perks.append(row)

file = open("survivor_perks.csv", "r")
csv_reader = csv.reader(file)

s_perks = []
for row in csv_reader:
    s_perks.append(row)


print("\n Hey Baby!")
playerInput = int(input("Are you playing Killer(1) or Survivor(2)?: "))
playOn = 1



if(playerInput == 2):
    print("\n")
    print(random.sample(s_perks, 4))
    while (playOn == 1):
        anotherOne = int(input("\n Need another? Yes(1) or No(2): "))
        if(anotherOne == 1):
            print(random.choice(s_perks))
        else:
            playOn = 2

else:
    print("\n")
    print(random.sample(k_perks,4))
    while (playOn == 1):
        anotherOne = int(input("\n Need another? Yes(1) or No(2): "))
        if(anotherOne == 1):
            print(random.choice(k_perks))
        else:
            playOn = 2


print("\n")
print("Good luck Baby!\n")
