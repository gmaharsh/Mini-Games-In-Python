from random import randint
print("Guess The Number")
n = int(input("Enter The Number"))
m = randint(0,5)

if(n == m):
    print("Today is your day")
else:
    print("Uff, Try Again")