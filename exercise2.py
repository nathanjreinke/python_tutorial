# 1. Create a list of names and print the second item.
print ("Question 1")
names = ["Nathan", "Joshua", "Christina"]
print (names[1])
print ("")

#2. Create a list of sports and then replace the second item with another sport.
print ("Question 2")
sports = ["soccer", "football", "rugby"]
print (sports)
sports[1] = "hockey"
print (sports)
print ("")

#3. Create a list containing numbers and delete the fifth number from the array.
print("Question 3")
nums = [1,2,3,4,5,6,7]
del nums[4]
print (nums)
print ("")

#4. Create two lists of numbers and merge them.
print("Question 4")
num2 = [1,3,5,7]
num3 = [2,4,6,8]
num4 = num2+num3
print (num4)
print ("")

#5. Create a list of numbers and find the length, minimum, and maximum.
print ("Question 5")
num6 = [1,164,32,48,16,84,65,49,65,16,468,43,1,65,468,46,489,4,654]
print(max(num6), min(num6), len(num6))
print ("")

#6. Create a dictionary of students and scores and print out a student’s score.
print ("Question 6")
students = {'bob':12, "rachel":13, "emily":15}
print ("Emily's score is", students['emily'])
print ("")

#7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
print ("Question 7")
students2 = {'bob':12, "rachel":13, "emily":15}
del students2['rachel']
print (students2)
print ("")

#8. Create a dictionary of names and ages and then print out all the keys and values
print ("Question 8")
print (students.keys())
print (students.values())
print ("")

#9. Create a tuple of your favorite movies
print ("Question 9")
movies = ("star wars", "star trek", "stargate")
print (movies)
print ("")

#10. Create a tuple and print all the items from the first to third index.
print ("Question 10")
nums = (1,35,46,6,498,654,68,45,1)
print (nums[0:3])