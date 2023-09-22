# Car rent:

# Write a program that ask the total Km traveled by a rented car and the total of rent days

# Calculate the price to pay, knowning the car cost R$ 60 per day and R$ 0.15 per Km traveled

days = int(input("How many days the car was rented: \n"))
km = float(input("How many km the car traveled: \n"))

day_cost = (days * 60)
km_cost = (km * 0.15)

print("You traveled {}Km per {} days, so the price to pay is R${:.2f}.".format(km, days, (km_cost + day_cost)))
