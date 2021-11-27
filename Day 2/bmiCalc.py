print("Body Mass Index Calculator\n")
height = input("What is your height in ft: ")
weight = input("What is your weight in lbs: ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)