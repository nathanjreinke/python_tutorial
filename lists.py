# Introduction to lists

shopping_list = ['apples',"bananas","oranges","cheese"]

print (shopping_list[0:2])

# add items to list
shopping_list.append('blueberries)')
print (shopping_list)

# update items
shopping_list[0] = "cherries"
print(shopping_list)

del shopping_list[1]
print (shopping_list)

# length of list
print(len(shopping_list))

shopping_list_2 = ['bread','jam']
print (shopping_list + shopping_list_2)

#max and min
num=[1,25,64984,612121,94,6165]
print(max(num))
print(min(num))

# Dictionaries
students = {'bob':12, "rachel":13, "emily":15}
print(students['rachel'])
students['rachel']=14
del students ['emily']
print (len(students))

# Tuples
# Tuples cannot be modified

fruits = ('oranges','apples','bananas')
print(fruits[0])