#password generator
from tkinter import * 
import string
import random
import time

def program():
    
    char = string.ascii_letters + string.digits
    x = input("Password generator - select difficulty:\n\n-easy\n-medium\n-hard\n-custom\n: ")
    x.lower()


    if x == "easy":
        sample1 = random.sample(char,6)
        print("Password generating...")
        time.sleep(2.3)
        for i in sample1:
            print (i, end="")
        
    elif x == "medium":
        sample2 = random.sample(char,10)
        print("Password generating...")
        time.sleep(2.3)
        for i in sample2:
            print (i, end="")
        
    elif x == "hard":
        sample3 = random.sample(char,14)
        print("Password generating...")
        time.sleep(2.3)
        for i in sample3:
            print(i, end="")
    
    elif x == "custom":
        ans1 = int(input("Number of characters: "))
        sample4 = random.sample(char,ans1)
        print("Password generating...")
        time.sleep(2.3)
        for i in sample4:
            print(i , end="")
        

program()

#restart code
restartX = input("\nDo you want another password: ")
restartX.lower()
if restartX == "yes":
    program()
elif restartX == "no":
    print("Goodbye...")
    time.sleep(1.9)
    exit()
    
    

    
    
    

