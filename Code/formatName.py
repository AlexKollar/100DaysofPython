#fuctions with out

def formatName(fname, lname):
    # Below is a docstring it allows you to document your methods. 
    # Use it love it. Its mega useful and also functions as a 
    # multi line comment.
    """Take a first name and last name and format it
    to return the title case of the name"""
    if fname == "" or lname == "":
        return "No name given. Please provide valid input."
    formattedFName = fname.title()
    formattedLName = lname.title()
    return f"{formattedFName} {formattedLName}"

print(formatName(input("What is your first name: "), input("What is your last name: ")))

# Did you know that you 
# can do multi line comments 
# mega easy by using ctrl + /
# after highlighting what 
# you want to comment! 
# Fucking nifty! 
# PS: Works on Linux as well. 