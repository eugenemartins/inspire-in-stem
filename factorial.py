#!usr\bin|python
######################################################################################
#name : Eugene Martins Maloba
# factorials
#date : 30/5/2022
###################################################################################################

number=int(input("Enter the number : "))
factorial = 1 
if number < 0 :
    print("factorial of negative number does not exist")
elif number == 0 : 
    print ("factorial of 0 = 1")  
else : 
    for i in range(1,number+1):
        factorial=factorial*i
print("factorial of number :",factorial)         
          