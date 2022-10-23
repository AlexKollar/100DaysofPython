#top Level (Global) Vars
playerHeath = 10
enemies = "Skeleton"

"""
Global constants are variable that dont change like for instance pi
However they are differentiated by using all uppercase. 
"""

def increaseEnemies():
    global enemies #avoid modifying global scope like this. Prone to bugs
    enemies = "Zombie"
    print(f"Enemies inside function: {enemies}")

increaseEnemies()
print(f"Enemies outside of function: {enemies}")

#local scope
def drinkPotion():
    potionStrenght = 2
    print(f"Potion Strenght: {potionStrenght}")

drinkPotion()
"""
Local scope = any variable that is nested inside of a function. 
It can only be called within the function it resides in. If you 
tried to print potion strenght outside of the function it would 
error out
"""

#global scope
def drinkAgain():
    potionStr = 2
    healing = playerHeath + potionStr
    print(f"Health is currently: {playerHeath}")
    print(f"You drank a potion \nYour health is now: {healing}")

drinkAgain()
"""
Global scope gives you access to any top level variable anywhere in the script
Top Level Var = any variable that is not created within a function 
These can exist anywhere in the code not just the top of the file. 
Though for organization it would be good to keep them there.

THERE IS NO SUCH THING AS BLOCK SCOPE IN PYTHON
"""
