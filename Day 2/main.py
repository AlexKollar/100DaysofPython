#Print welcome message
print("\nTip Calculator")
#Ask for bill total and convert to int
bill = float(input("\nHow much was the bill? $"))
#Ask what percentage you want to give
tip = int(input("\nWhat percentage should the tip be: "))
#Ask how many people will split the bill
people = int(input("\nHow many people to split the bill: "))
tip_as_percent = tip / 100
total_tip_ammount = bill * tip_as_percent
total_bill = bill + total_tip_ammount
bill_per_person = total_bill / people
final_ammount = round(bill_per_person, 2)
#Print results
print(f"\nEach person should pay: ${final_ammount}")