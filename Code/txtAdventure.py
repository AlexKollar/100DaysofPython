print("Welcome to Treasure Island")
print("Your goal is to find the treasure!")
choice1 = input("\nYou are standing at a crossroad. Where do you want to go? Type: 'left\' or 'right\' \n").lower()

if choice1 == "left":
  choice2 = input("You find yourself at a lake. Type: 'wait\' to wait for a boat or type 'swim\' to take your chances: \n").lower()
  if choice2 == "wait":
    choice3 = input("You made it. You find a house with three doors type 'red\', 'yellow\' or 'blue\' to go through the corresponding door \n").lower()
    if choice3 == "red":
      print("You are instantly engulfed in flames: Game Over")
    elif choice3 == "yellow":
      print("You enter the door and fall into Cthulu's mouth... Game Over")
    elif choice3 == "blue":
      print("You have found the treasure. A can of Dapper Dan.\n YOU WIN!!")
    else:
      print("You died of dysentery...Terry is a girls name anyway...\nGAME OVER")
  else:
    print("You tried to swim across but hit an invisible barrier. You also got nommed by fred. A megolodon...Game over.")
    
else:
  print("You fell into the void: Game Over!")