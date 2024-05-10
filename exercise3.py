def calculate_factorial(num):
    total=1
    for i in range (1,num+1):
        total=total*i
    return total

print (calculate_factorial(5))