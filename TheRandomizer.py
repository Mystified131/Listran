#This code imports the necessary modules.

import random
import os
from subprocess import call

content = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\thomasoriginalcode\\Git\\Listran\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt") :
            cline = (str(file)).strip()
            content.append(cline)

print("")

print("Here are the available lists:")

print("")
 
for elem in content:
    print(elem + '\n')

print("")

lisnam = input("Which list would you like to use? Please include the .txt suffix: ")

print("")

try: 
    infile = open(lisnam, "r")

    contentb = []

    aline = infile.readline()

    bline = ""

    while aline:
        bline = aline.strip()
        contentb.append(bline)
        bline = ""
        aline = infile.readline()
    infile.close()

except:
    print("That list did not load properly.")
    print("")
    call(["python", "TheRandomizer.py"])

print("")

xl = len(contentb)

xm = random.randrange(xl)
 
print("A random selection from this list is: " + contentb[xm])

print("")

ag = input("Do you want to try this again? Please press 'y' if so, or 'l' to go to the Listmaker: ")

if ag == 'y':
    call(["python", "TheRandomizer.py"])

if ag == 'l':
    call(["python", "TheListmaker.py"])

## THE GHOST OF THE SHADOW ##
