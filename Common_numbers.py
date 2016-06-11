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

a = random.sample(range(100), 10)

b = random.sample(range(100), 10)


for i in a:
    for j in b:
        if i == j and i not in common_numbers :
            common_numbers.append(i)        
print common_numbers    
