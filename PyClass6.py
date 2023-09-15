# Make a program that read the width and height of a wall in meters, calculate its area and the amount of needed ink to paint it, knowing wich each liter of ink paint an area of 2m² 

width = float(input("Insert the width: \n"))
height = float(input("Insert the height: \n"))
area = width * height

print("Your wall have tha dimensity of {} x {} and your area is {:.2f}m².".format(width, height, area))

# each liter (L) of ink paint an area of 2m².

needed_ink = area / 2
print("To paint this wall, you need {:.2f}L of ink.".format(needed_ink))
