#!usr\bin|python
######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022
#####################################################################################3#
# Test if a number is even
num = int(input("Enter the number : "))

for num in range(0,30) : 
    if (num %5 == 0 ) : 
        print(num , "is divisible by 5")
else: (num %7 == 0)
print(num,"is divisible by 7")     

for num in range(0,30) : 
    if (num %5 == 0) :  
        print(num," is divisible by 5")
    elif(num %7 == 0) : 
        print(num, " is divisible by 7")

if(num %7 == 0) and (num %5 == 0) : 
    print(f"the number {num} is divisible by 5 or 7")
else:
    print(f"the number {num} is not divisible by 5 or 7")    

Name=input("Enter your name so we can cutomize the greeting : ")
Name=input("Enter your name :")

print("Hello " + str(Name))

# num = 20
# num += num
# print(num)

name = ("Enter your name so we can customize the greeting")
name += "\n  Enter your name : "
print("Hello " +input(name))
