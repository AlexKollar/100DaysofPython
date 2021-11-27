# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

names_as_lower = f"{name1}{name2}".lower()

# Map each char to 1 if they're in "true" / "love" respectively. Otherwise map them to 0. Then sum.
true_occurances = sum(map(lambda char: 1 if char in "true" else 0, names_as_lower))
love_occurances = sum(map(lambda char: 1 if char in "love" else 0, names_as_lower))

score = true_occurances * 10 + love_occurances

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")