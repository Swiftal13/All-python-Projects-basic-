#inch + cm - converter

x = int(input("digit: "))
y = int(input("1  -  inch to cm    2  -  cm to  inch:"))
if y == 1:
        print(x*2.54, "cm")
elif y == 2:
    print(x*0.393700787, "inches")
else:
    print("please choose 1 or 2: ")

