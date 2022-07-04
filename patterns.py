#!usr\bin|python
######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022
#########################################################################################
#half pyramid of stars

rows = int(input("Enter the number of rows : "))
for i in range(rows) : 
    for j in range(i+1) : 
        print("* ", end =" ")
    print("\n")

#half pyramid of numbers

rows=int(input("Enter no of rows : "))

for i in range(rows) : 
    for j in range(i+1) : 
        print(j+1, end=" ")
    print(" \n ")    