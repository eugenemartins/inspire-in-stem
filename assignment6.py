#!usr\bin|python
######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022
###########################################################################################
#reverse number in python

#using while loop
n = int(input("Enter the number you wish to reverse : "))
rev = 0
while (n > 0) : 
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
print("The reverse number is : {}" .format(rev ))

#using string slicing
num = int(input("Enter the number : "))
print(str(num)[: : -1])