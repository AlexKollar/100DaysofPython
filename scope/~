#global Vars:
import random

logo = """
   _  __           __             _____                 _             _____              
  / |/ /_ ____ _  / /  ___ ____  / ___/_ _____ ___ ___ (_)__  ___ _  / ___/__ ___ _  ___ 
 /    / // /  ' \/ _ \/ -_) __/ / (_ / // / -_|_-<(_-</ / _ \/ _ `/ / (_ / _ `/  ' \/ -_)
/_/|_/\_,_/_/_/_/_.__/\__/_/    \___/\_,_/\__/___/___/_/_//_/\_, /  \___/\_,_/_/_/_/\__/ 
                                                            /___/                        
"""

num = random.randrange(1, 100)

def easyMode():
    attempt = 10
    print(f"You chose easy mode... \nYou have {attempt} to find the number.")
    while attempt > 0:
        guess = int(input("Your guess: "))
        if guess == num:
            print("===== You win! =====")
            break
        elif guess > num:
            attempt -= 1
            print(f"{guess} is greater\nAttempts left: {attempt}")
        elif guess < num:
            attempt -= 1
            print(f"{guess} is less\nAttempts left: {attempt}")
        else:
            print("Something went wrong!")
            break

def hardMode():
    attempt = 5
    print(f"You chose hard mode... \nYou have {attempt} to find the number.")
    while attempt > 0:
        guess = int(input("Your guess: "))
        if guess == num:
            print("===== You win! =====")
            break
        elif guess > num:
            attempt -= 1
            print(f"{guess} is greater\nAttempts left: {attempt}")
        elif guess < num:
            attempt -= 1
            print(f"{guess} is less\nAttempts left: {attempt}")
        else:
            print("Something went wrong!")
            break

#print welcome:
print(f"{logo}\nI'm thinking of a number between 1 and 100")
mode = input("Choose a difficulty. Type \'easy\' or \'hard\': ")
if mode == "easy":
    easyMode()
if mode == "hard":
    hardMode()
