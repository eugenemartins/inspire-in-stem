#!/usr/bin/python

###########################################

#loops: for loop

# Name : Eugene Maloba

# Date : 23 / 5 /2022

#############################################


print("Number\t    square")
print("========================================")




for number in range(0,9):
    print(number)   
    print("\t")
    print(number**2)


# Pyramid of stars

print("pyramid of stars (*):")
for i in range(5):
    for s in range(-6, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()


# Diamond of stars
h = int(input("please enter diamond's height:"))


for i in range(h):
    print(" "*(h-i), "*"*(i*2+1))
for i in range(h-2, -1, -1):
    print(" "*(h-i), "*"*(i*2+1))
