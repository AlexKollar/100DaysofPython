#fuctions with out

def formatName(fname, lname):
    if fname == "" or lname == "":
        return "No name given. Please provide valid input."
    formattedFName = fname.title()
    formattedLName = lname.title()
    return f"{formattedFName} {formattedLName}"

print(formatName(input("What is your first name: "), input("What is your last name: ")))