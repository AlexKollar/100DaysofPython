import random
print("Who pays the bill")
nameString = input("Give me everyones names seperated by a comma:\n")
names = nameString.split(", ")
rndmName = random.randint(0, len(names))
print(names[rndmName] + " Is going to buy the meal today!")