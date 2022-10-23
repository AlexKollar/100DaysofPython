#Our basic multi-type travel log
travelLog =[
    {
        "Country" : "France",
        "Visits" : 3,
        "Cities" : ["Paris", "Dijon", "Lille"],
    },
    {
        "Country" : "Germany",
        "Visits" : 2,
        "Cities" : ["Berlin", "Hamburg", "Stuttgart"]
    },    
]

#TODO Add code that allows you to add a country to your travel log
def addNewCountry(countryVisited, timesVisited, citiesVisited):
    newCountry = {}
    newCountry["Country"] = countryVisited
    newCountry["Visits"] = timesVisited
    newCountry["Cities"] = citiesVisited
    travelLog.append(newCountry)


#Add Russia to the travel log
addNewCountry("Russia", 2, ["Moscow", "St Petersburg"])
#Print it all out.
print(travelLog)