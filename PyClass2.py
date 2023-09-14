# Make a Python script that read the day, the month and the birthdate of someone and show a message with the formated date.

year = int(input("Year of birth: \n"))
month = int(input("Month of birth: \n"))
day = int(input("Day of birth: \n"))

print("The person born in: {}/{}/{}".format(day, month, year))

print("The person born in the day {} of the month {} and the in the year of {}.".format(day, month, year))