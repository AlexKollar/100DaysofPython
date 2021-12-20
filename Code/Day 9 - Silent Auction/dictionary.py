programmingDict = {
    "Bug" : "Bug(n):\n An error in your code that prevents it from running.\n",
    "Function" : "Function(n):\n A piece of code that you can easily call over and over.\n",
    "Loop" : "Loop(v):\n The action of doing something over and over. \n Some call this insanity.\n"
}

print(programmingDict["Bug"])
print(programmingDict["Function"])
print(programmingDict["Loop"])

#adding new items to the dictionary:
programmingDict["Hello World"] = "Hello Word(v): \n The most basic bitch program you can write. \n It literally prints hello world.\n"

#now print it out
print(programmingDict["Hello World"])

#You can wipe an entire dictionary like this: 
#programmingDict = {}

#You can optionally use an empty dictionary as follows;
emptyDict = {}
#You can obviously add things to the dictionary.
emptyDict["Basic Bitch"] = "Basic Bitch(n): \n Starbucks..."
print(emptyDict["Basic Bitch"])

#You can ALSO modify things in the dictionary as follows:
emptyDict["Basic Bitch"] = "Basic Bitch(n): \n A Venti Quad Shot Caramel Mach Addicted White Girl. \n Cythes was here :D"
print(emptyDict["Basic Bitch"])

#Looping through a dictionary:

for key in programmingDict:
    #print(key)
    print(programmingDict[key])

