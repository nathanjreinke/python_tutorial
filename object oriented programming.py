#oop - clasees and objects

#class: dog
#properties: name, age, breed...
#Methods: barl, eat, sleep...

#Object 1,2,3...
#Properties: Fidd,5,german shepherd...

#person class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

p1 = Person("Bob",22)

print (p1.getName())
print (p1.getAge())

#oop - class inheritance

class Car:
    def __init__(self):
        self.wheels = 4
        self.seats = 5
    
    def drive(self):
        print("Driving a car...")

class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self.engine_power = '400 HP'
        self.seats = 2

    def drive(self):
        print ('Driving a sports car')

myCar= Car()
myCar.drive()

mySportsCar = SportsCar()
mySportsCar.drive()