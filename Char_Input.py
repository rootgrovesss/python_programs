'''

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1.    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
2.  Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''

from datetime import datetime

x = raw_input("Enter Your Name : ")
y = int(input("Enter Your Age : "))
i = input("Enter numebr of times you want to print this output : ")

current_year = datetime.now().year
z = 100 - y
year = current_year + z

for a in range(i):
    print("Hey %s You will be 100 years old in %d" %(x,year))
    
