#!usr\bin|python

######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022
##########################################################################################
#sum of all even numbers between 0-50
sum=0
for number in range (0,50):
    if(number %2 == 0):
        sum=sum+number
print(sum)

#product of all odd numbers between 0-10
prod=1
for number in range(0,20):
    if(number %2 == 1):#odd number
        prod=prod*number
print(prod)

#calculate the factorial of 6! and 9!
#5!
fact = 1
for number in range(0,6):
    if(number %2 == 1):
        fact=number*(number-1)*(number-2)*(number-3)*(number-4)
print(fact)
#9!
fact = 1
for number in range(0,10) : 
    if(number %2 == 1) : 
        fact=number*(number-1)*(number-2)*(number-3)*(number-4)*(number-5)*(number-6)*(number-7)*(number-8)
print(fact)

#6
fact = 0
for number in range(7) : 
    if(number %2 == 0) :
        fact=number*(number-1)*(number-2)*(number-3)*(number-4)*(number-5)
print(fact)
