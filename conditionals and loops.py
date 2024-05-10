# Conditional statements

if 2>3:
    print ("hello")
else:
    print ("condition was not true")

#relational operators
# > < >= <= ++ !=

# else if statements

age = 100

if age <= 15:
    print ("You are less than 16")
elif age == 16:
    print ("You are 16")
elif age > 16:
    print ("You are older than 16")

if age <13:
    print ("you are a child")
elif age>=13 and age <=18:
    print ("you are a teenager")
else:
    print ("you are an adult")

# for loops
list1 = ["apples","bananas","cherries"]
tup1 = (2,6,10)

for item in tup1:
    print(item)

for i in range(0,10):
    print(i)

for i in range (0,11,2):
    print (i)

for i in range (0,5):
    for j in range (0,3):
        print (i*j)

# while loops
# control statement - break, continue, and pass
c=0
while c <5:
    c=c+1
    if c ==3:
        continue
    print(c)
print ("done")
