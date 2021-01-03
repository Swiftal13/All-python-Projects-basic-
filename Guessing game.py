answer = int(input("Welcome to the Magic Number guessing game!, try to guess the number between 1 and 100: "))

import random
num = random.randint(10, 100)
attempts = 0


while answer != num:
    if answer > num:
        print("the answer is smaller")
    elif answer < num:
        print("the answer is greater")
    answer = int(input("try again: "))
    attempts = attempts + 1

print("You got it! The number was num: " ,num)
print("Your attemtps are: ", attempts)
