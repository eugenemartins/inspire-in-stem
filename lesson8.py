#!/usr/bin/python
####################################
#For loops with lists

#Name:Eugene Martins

#date:5/24/2022
########################################
squares=[]
for number in range(0,10) : 
    square=number**2
    squares.append(square)
print(squares) 

cubes=[]
for number in range(10,20):
    cube=number**3
    cubes.append(cube)
print(cubes)    

#sum of numbers between 1-100
sums=0
for number in range(1,100):
    sum=sums+number
print(sum)    

 #condition
age=24
if age >= 18:
     print("you are allowed to drive") 
else:
     print("you are too young")    



