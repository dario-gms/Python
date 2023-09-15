# Make a program that read the amount of money a person have in the wallet and show how many dollars can be bought

# consider R$ 4.87 = US% 1
wallet = float(input("How much money you have? \nR$"))
dolar = float(4.87)
conversion = wallet / dolar
print("With R${} you can buy US$ {:.2f}.".format(wallet, conversion))