studentScores = input("Input a list of student scores: ").split()
for n in range(0, len(studentScores)):
  studentScores[n] = int(studentScores[n])

highestScore = 0 
for score in studentScores:
  if score > highestScore:
    highestScore = score
print(f"\nThe highest score in the class is: {highestScore}")