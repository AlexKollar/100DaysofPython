#Import Random Module
import random
#Print Greeting
print("Heads or Tails:\n")
pressEnter = input("Press Enter to flip")
if pressEnter == "Enter" or "Return":
  #Use random module to generate between 0 and 1
  randomSide = random.randint(0, 1)
  #Logic output
  if randomSide == 1:
    print("Heads")
  else:
    print("Tails")
else:
  print("Invalid")
