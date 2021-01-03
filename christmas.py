while True:
    good = []
    name1 = input("Please input name: ")

    counter1 = 0
    ans1 = input(f"Does {name1} believe in Santa : ")
    ans2 = input(f"Did {name1} lose their temper this year : ")
    ans3 = input(f"Does {name1} always say 'please' and 'thank you' : ")
    ans4 = input(f"Does {name1} ever whine : ")
    ans5 = ("What is the nicest thing {name1} has done : ")
    if ans1 == "yes":
        counter1 = counter1 + 1
    elif ans2 == "yes":
        counter1 = counter1 + 1
    elif ans3 == "yes":
        counter1 = counter1 + 1
    elif ans4 == "yes":
        counter1 = counter1 + 1

    elif counter1 >2:
        print(f"{name1} is on the nice list")
        good.append(name1)
    elif counter1 <2:
        print(f"{name1} is on the naughty list")
    elif counter1 == 2:
        print("f{name1} is on the nice list")
    
