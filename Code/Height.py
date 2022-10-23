studentHeights = input("Input a list of student heights: ").split()
for n in range(0, len(studentHeights)):
  studentHeights[n] = int(studentHeights[n])

#Make your own sum()
totalHeight = 0
for height in studentHeights:
  totalHeight += height

#Make your own len()
numberOfStudents = 0
for student in studentHeights:
  numberOfStudents += 1

print(f"\nThe total height of the {numberOfStudents} students is: { totalHeight}")  
