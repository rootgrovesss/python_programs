'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1.Randomly generate two lists to test this
2.Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

'''

import random

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_numbers = []

for i in list1:
    for j in list2:
        if i == j and i not in common_numbers :
            common_numbers.append(i)        
print common_numbers    


#list_a_b = list(set(a + b))
#list_a_b.sort()
#print list_a_b 


#TRYING ON RANDOM SETS
m = input("Enter range : ")
n = input("Enter lenght of list a : ")
o = input("Enter lenght of list b : ")

a = random.sample(range(m), n)
b = random.sample(range(m), o)


for i in a:
    for j in b:
        if i == j and i not in common_numbers :
            common_numbers.append(i)        
print common_numbers    
