class Employee : #Creating a class
    def __init__(Self,_name,_salary):#__init__ () function
        Self.name = _name#creating object
        Self.salary = _salary
    def ref (Self) :
        print("Employee's name is " + Self.name + "and earns " +Self.salary + "kenyan shillings" )
employee1 = Employee("Eriod Hula" , str(450000)) 
employee1.ref()

class Person : 
    def __init__(self,_name,_age):
        self.name = _name
        self.age = str(_age)
    def sayHi(self): 
        print('Hello , i am ' + self.name + ' and I am ' + str(self.age))
person1 = Person("Bob" , str(16))
person1.sayHi()
person2 = Person('felo',str(56))
person2.sayHi()

class Vehicle :
    def __init__(vehicle,_top_speed,_mileage) :
        vehicle.max_speed = _top_speed
        vehicle.mileage = _mileage 
    def ref(vehicle):
        print("vehicle max speed is ; " +str(vehicle)+ '\n and has a mileage of: '+str(15000))    
Toyota=Vehicle("380mph" , 15555500)
Mercedes=Vehicle('420mph',759686588)
Vehicle.ref(Vehicle)
print('\n')