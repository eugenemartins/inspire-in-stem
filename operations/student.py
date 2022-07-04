#!usr\bin|python

######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022

from http import server


class student :
    def __init__(self ,name,hobby ,year_of_birth) : 
        self.name = name
        self.hobby = hobby
        self.year_of_birth = year_of_birth

    def greet_student(student) : 
        print("Hello from "  + name.title())
