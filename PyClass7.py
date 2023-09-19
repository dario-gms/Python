# Make a program that read the price of a product and show your new price, with 5% off

price = float(input("Insert the price of a product: \nR$"))
discount = price * 5 /100
print("During the store's sale, this product of R${:.2f} has a 5% discount, \nso it will only cost R${:.2f}.".format(price, price - discount))