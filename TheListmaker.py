#This code imports the necessary modules.
from subprocess import call

print("")
namstr =  input("Welcome to the listmaker. Please give your list a name: ")
print("")
numelem = input("How many elements would you like to add to the list?: ")
print("")

totelem = []

for x in range(int(numelem)):
    ele = input("Please add an element to the list: ")
    print("")
    totelem.append(ele)

print("")
print("You will find your list in the same folder as this code.")
print("")

titstr = namstr + ".txt"

outfile = open(titstr, "w")

for elem in totelem:
    outfile.write(elem +  '\n')

outfile.close()

print("")
agstr = input("Press 'y' to do more list work or 'r to move to 'The Randomizer': ")

if agstr == 'y':
    call(["python", "TheListmaker.py"])

if agstr == 'r':
    call(["python", "TheRandomizer.py"])

## THE GHOST OF THE SHADOW ##