# Make a program that read something from keyboard
# and show in the screen it primitive type
# and all possible information about it

entry = input("Write something: \n")
print("Primitive type: {}.".format(type(entry)))

print("Is numeric? {}".format(entry.isnumeric()))
print("Is alphanumeric? {}".format(entry.isalpha()))
print("Is a decimal? {}".format(entry.isdecimal()))
print("Is lowercase? {}".format(entry.islower()))
print("Is only blankspace? {}".format(entry.isspace()))
print("Is uppercase? {}".format(entry.isupper()))