# Make a program that read the wage of a employee and show his new wage, with 15% of increase

wage = float(input("Insert your wage: \nR$"))
increase = wage * 15/100
print("The wage of employee, that is R${:.2f}, will up to R${:.2f} with the increase of 15%.".format(wage, wage + increase))