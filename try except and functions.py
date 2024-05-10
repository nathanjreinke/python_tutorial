# try and except

try:
    if name>3:
        print("hello")
except:
    print ("an error was detected")

#functions

def hello_world():
    print ("Hello World")

hello_world()

def greeting(name):
    print ("Hi "+ name + "!")

greeting('Nathan')

def sum(num1, num2):
    ans = num1 + num2
    print (ans)

sum (1,5)

def add(num1,num2):
    return num1+num2

num_sum = add(30,27)
print (num_sum)

def mul (num1,num2):
    return num1*num2

print (mul (add(1,2),(add(3,4))))