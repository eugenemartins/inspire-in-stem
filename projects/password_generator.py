#!usr\bin|python

######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022
##################################################################################################
import random
print('Welcome to our password generator app! ')
print("\n")
characters= input('Enter your prefered characters to make a password: ')
num_passwords = int(input('How many passwords would you like to be generated: '))
lengthPasswords = int(input('Enter the length of the password you would wish to have : '))
print('Here are your passwords: ')
for pwd in range(num_passwords):
    passwords = ' '
    for c in range(lengthPasswords):
        passwords += random.choice(characters)
    print(passwords)


