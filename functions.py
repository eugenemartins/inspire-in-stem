#!usr\bin|python
######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022
###################################################################################################################
# function - a block of code which get executed together

# initializing the function/defining---def
def say_hello():
    print("Hello from JKUAT")
    x=4
    y=5
    print(x+y)
say_hello()    

def barks():
    print('Dog barks woof')
def mows():
    print("cows moow")
def neighs():
    print('horse neighs')
barks()
mows()
neighs()

#function parameters
#function to add two numbers
def add_numbers(x,y):
    sum_numbers = x+y
    print('the sum of numbers :',sum_numbers)
#calling the function
add_numbers(40,50) 
add_numbers(45,67)
add_numbers(45,789)   
add_numbers(9078,6006)
add_numbers(677,99)

#function to multiply two numbers
def products_numbers(x,y):
    products_numbers = x * y
    print('the product of numbers :',products_numbers)
products_numbers(45,8)
products_numbers(6,9)
products_numbers(9,-9)
products_numbers(2,98)
products_numbers(-9,-9)
products_numbers(6,9)

#using default parameter
def print_name(name = 'Eugene' ) : 
    print(name)
print_name('Felo')

# return from a function
def get_sum(num_1,num_2):
    sum_nums = num_1 + num_2
    return sum_nums
print(get_sum(7,12))    

#power of numbers
def powers(number,power):
    pow_nums = number ** power
    return pow_nums
print(powers(6,4))    
print(powers(9,2))

def get_fullname(f_name , s_name) :
    full_name = f_name +" "+ s_name
    return full_name.title()
print(get_fullname('Maneev' , 'Hurden'))

#Returning a dictionary from a function
def create_fullname(first_name , second_name) : 
    person = {'first': first_name , 'second': second_name}
    return person
student = create_fullname('goffrey','uryan')
print(student)    

#passing a list in a function
def greet_friends(names) : 
    for name in names : 
        msg = "Hello "+ name.title() +"!"
        print(msg)
Friends = ['weso','Gin','kith','poty']
greet_friends(Friends)