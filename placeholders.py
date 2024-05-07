# Placeholders in strings
# %s is for strings, %d is for integers

name, age = "Jake", 15
sent1 = "%s is %d years old."

print (sent1 % (name, age)) #prints sentence with placeholders replaced with variables in brackets

# format strings (or f strings)

name = "Nathan"
print (f"Hello, {name}")

x,y = 10,20
print (f"The sum of x and y is {x+y}.")

