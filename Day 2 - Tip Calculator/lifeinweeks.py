#Ask for current age
print("Life in weeks Calculator")
age = input("\nWhat is your current age: ")
#convert age string to int
age_as_int = int(age)
#calculate time left before 90
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = days_remaining * 52
months_remaining = weeks_remaining * 12
#f strings allow you to plop variables right into strings.
message = f"You have: {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left"
print(message)
