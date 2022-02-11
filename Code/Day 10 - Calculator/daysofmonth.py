def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def daysInMonth(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    monthDays= [31,30,29,28,27,26,25,24,23,22,21,20,
                19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    if isLeap(year) and month == 2:
        return 29
    return monthDays[month - 1]
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = daysInMonth(year, month)
print(days)    
    