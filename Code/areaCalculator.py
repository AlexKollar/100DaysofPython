import math

print("""
    ___      _     _    ___      _         _      _           
   | _ \__ _(_)_ _| |_ / __|__ _| |__ _  _| |__ _| |_ ___ _ _ 
   |  _/ _` | | ' \  _| (__/ _` | / _| || | / _` |  _/ _ \ '_|
   |_| \__,_|_|_||_\__|\___\__,_|_\__|\_,_|_\__,_|\__\___/_|  
""")

def paintCalc(height, width, cover):
    area = height * width
    numCans = math.ceil(area / cover)
    print(f"You will need {numCans} of paint.")

testHeight = int(input("What is the height of the wall: "))
testWidth = int(input("What is the width of the wall: "))
coverage = 5
paintCalc(height=testHeight, width=testWidth, cover=coverage)