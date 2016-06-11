" Find Factor of a number"

number = input("Enter a Number : ")
factor = []
factor = [i for i in range(1,number+1) if number%i == 0]

print factor




