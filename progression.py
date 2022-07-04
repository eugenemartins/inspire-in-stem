#!usr\bin|python

######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022


#first n terms of AP
# a= 'first_number'
# d= 'steps(common_difference)'
# n= 'no_of_terms'

a=int(input("Enter the number : "))
d=int(input("Enter the number : "))
n=int(input("Enter the number : "))

for i in range(1,n+1):
    n_term = a + (i-1)*d
    print(n_term)
sum_n=(n_term/2)*(2*a + (n-1)*d)
print(sum_n)


#Geometric progression
#find number of terms
a='first term'
r='common ratio'
n='no. of terms'

a=int(input("Enter the first term : "))
r=int(input("Enter the common ratio : "))
n=int(input("Enter the no. of terms : "))

for i in range(1,n+1):
    n_term=a*(r**(n-1))
print(n_term)