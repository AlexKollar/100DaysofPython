#Generate a map grid using emojis
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

#Nest the grid into a map
map = [row1, row2, row3]
#Print the map

print(f"{row1}\n{row2}\n{row3}")
#Ask where you want to place the x
position = input("Where do you want to put the treasure: ")

#Gather Position Data and convert to integer
horizontal = int(position[0])
vertical = int(position[1])

#Black Magic
selectedRow = map[vertical - 1]
selectedRow[horizontal -1] = "❌"
#selectedRow[horizontal -1] = "X" #For the CLI
#Print the output and the new map with the treasure marked on it.
print(f"{row1}\n{row2}\n{row3}")