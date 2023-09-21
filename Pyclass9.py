# temperature converter: write a program that converts an inserted tempoerature in ºC to ºF

celsius = float(input("Insert the temperature in Celsius: \n"))
farenheit = ((1.8 * celsius) + 32)
print("{}ºC matchs to {:.1f}ºF. ".format(celsius, farenheit))