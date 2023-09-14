# Make a Python script that read 2 numbers and show the sum result

num1 = int(input("Insert the first number: \n"))
num2 = int(input("insert the second number: \n"))

print("The sum is:",num1+num2)
print("The sum is: %d!" % (num1 + num2))
print("The sum is: {}!".format(num1+num2))

# Other ways

n1 = int(input("Insert a number: \n"))
n2 = int(input("insert another number: \n"))
sum = n1 + n2

print(sum)