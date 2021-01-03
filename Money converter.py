#Money converter

pounds = int(input("Type in amount: £"))
answer = str(input("E = Euros     Y = Yen    D = Dollars   R = Rial   Y = Yuan: "))


if answer == "E":
    print (str(pounds * 1.09) + " Euros")
elif answer == "Y":
    print (str(pounds * 134.45) + " Yuan")
elif answer == "D":
    print (str(pounds * 1.28) + " Dollars")
elif answer == "R":
    print (str(pounds * 53736.93) + " Rial")
elif answer == "Y":
    print (str(pounds * 8.68) + " Yuan")
else:
    print("Invalid, please type a valid number")







