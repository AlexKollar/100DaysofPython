import random

#Setup variables for RPS ASCII Art
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
gameImages = [rock, paper, scissors]
#Print Greeting
print("Lets play Rock Paper Scissors")
#Gather user input
playerChoice = int(input("Choices:\n0.) Rock\n1.) Paper\n2.) Scissors\nEnter the number of your choice: "))
#Check that player is not cheesing the system by using false numbers.
if (playerChoice >= 3) or (playerChoice < 0):
  print("You typed an invalid number: You Lose!")
else:
  #Print the images
  print(gameImages[playerChoice])
  computerChoice = random.randint(0, 2)
  print("Computer chose: ")
  print(gameImages[computerChoice])
  #Game Logic
  if (playerChoice == 0) and (computerChoice == 2):
    print("You Win!")
  elif (computerChoice > playerChoice):
    print("You Lose!")
  elif (playerChoice > computerChoice):
    print("You Win!")
  elif (computerChoice == 0) and (playerChoice == 2):
    print("You Lose!")
  elif(playerChoice == computerChoice):
    print("Its a draw!")