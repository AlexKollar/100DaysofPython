studentScores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 68,
}

studentGrades = {}

for student in studentScores:
    score = studentScores[student]
    if score > 90:
        studentGrades[student] = "Outstanding"
    elif score > 80:
        studentGrades[student] = "Exceeds Expectation"
    elif score > 70:
        studentGrades[student] = "Acceptable"
    else:
        studentGrades[student] = "Fail"
        
print(studentGrades)