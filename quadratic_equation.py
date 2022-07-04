#!usr\bin|python

######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022
##############################################################################################
import math

# a = int(input("Enter the coefficient of first term (a) :"))
# b = int(input("Enter the coefficient of second term (b) :"))
# c = int(input("Enter the constant (c) :"))

# def find_roots(a,b,c) : 
#     y1 = ((-b + math.sqrt((b**2) - 4 * a * c ))/(2*a))

#     y2 = ((-b - math.sqrt((b**2) - 4 * a * c ))/(2*a))
#     print("The root of the quadratic equation are:", y1 , y2)
# find_roots(a,b,c)

a = int(input("Enter the coefficient of first term (a) :"))
b = int(input("Enter the coefficient of second term (b) :"))
c = int(input("Enter the constant (c) :"))
w = math.sqrt((b**2)-(4*a*c))

def find_roots(a,b,c) : 
    y_1 = ((-b + w)/(2*a))
    y_2 = ((-b - w)/(2*a))
    print("The root of the quadratic equation are:", y_1 , y_2)
# find_roots(a,b,c)