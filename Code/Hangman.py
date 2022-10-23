#step 1 make a word list:
wordList = ["apple", "orange", "pear", "lemon", "watermellon"]

#Step 2 Randomly choose a word from the word less and assign it to a variable
import random
chosenWord = random.choice(wordList)
wordLenght = len(chosenWord)

#testing code
print(f"pssst: the solution is: {chosenWord}")

display = []
for _ in range(wordLenght):
    display += "_"
print(display) 

endOfGame = False

while not endOfGame:
    #Step 3 Ask the user to guess a letter assign to a variable and switch to lowercase
    guess = input("Guess a letter: ").lower()

    #Step 4 Check if the letter guessed matches any of the letters in random word
    for position in range(wordLenght):
        letter = chosenWord[position]
        if letter == guess: 
            display[position] = letter
    print(display)
    
if "_" not in display:
    endOfGame = True
    print("You win!")