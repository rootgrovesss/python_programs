'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.

Hint: how does an even / odd number react differently when divided by 2?

Extras:

1.If the number is a multiple of 4, print out a different message.

2.Ask the user for two numbers: one number to check (call it num) and
one number to divide by (check). If check divides evenly into num,tell that
to the user.If not, print a different appropriate message.

'''

x = input("Enter a number : ")

if x%2 == 0:
    if x%4 == 0:
        print "It is multiple of 4"
    else:
        print "It is an even number"
else:
    print "It is an odd numebr"

#EXTRA 2

y = input("Enter First Number : ")
z = input("Enter Second Number : ")

if y%z == 0:
    print "%d is divisible by %d" %(y,z)
else:
    print "%d is not divisible by %d" %(y,z)
