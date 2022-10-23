import random
print("""       .....           .....
   ,ad8PPPP88b,     ,d88PPPP8ba,
  d8P"      "Y8b, ,d8P"      "Y8b
 dP'           "8a8"           `Yd
 8(              "              )8
 I8      The Love Calculator    8I
  Yb,           2.0            ,dP
   "8a,                     ,a8"
     "8a,                 ,a8"
       "Yba             adP"   
         `Y8a         a8P'
           `88,     ,88'
             "8b   d8"
              "8b d8"
               `888'
                 "
      
""")

name1 = input("What is your name: ")
name2 = input("What is thier name: ")

loveScore = random.randint(1, 100)

if loveScore <= 10:
  print(f"The score between {name1} and {name2} is: {loveScore} \nAssesment: \nYou go together like coke and mentos. \nCrash and burn airlines called they want thier luck back")
elif (loveScore > 10) and (loveScore <= 30):
  print(f"The score between {name1} and {name2} is: {loveScore} \nAssesment: \nYou think that is love? I dont advise it... \nHey its your funeral")
elif (loveScore > 30) and (loveScore <= 60):
  print(f"The score between {name1} and {name2} is: {loveScore} \nAssesment: \nYour relationship is good on paper, but will likely have issues. \nBut hey, what do I know. I'm just RNJesus")
elif (loveScore > 60) and (loveScore <= 85):
  print(f"The score between {name1} and {name2} is: {loveScore} \nAssesment: \nYou have a strong foundation but will likely have issues later on.")
elif (loveScore > 85):
    print(f"The score between {name1} and {name2} is: {loveScore} \nAssesment: \nYour relationship is golden. You can overcome any problems. \nIf the beds a rocki'n dont come knockin.")
else:
  print("You broke it... Good Job Try again.")

print("\n\nDISCLAIMER: \nKeep in mind this program is for entertainment only! \nDon't take it seriously.\n- Cy")