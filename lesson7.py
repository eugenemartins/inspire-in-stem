#!/usr/bin/python
###################################################################
# Dictionaries

# Name : Eugene Maloba

# Date : 24 / 5 /2022
########################################################################
# Initializing dictionaries
student={"Name":"Maloba","Age":24,"Gender":"male"}
print(student["Name"])
print(student["Age"])
print(student["Gender"])
#Adding key value pair to a dictionary
student["id_no"]="6487085752"
student["hobby"]="travelling"
student["club"]="cityzen"
student["food"]="ugali"
print(student)
#Empty dictionary
student={}
student["school"]="kericho"
student["home_city"]="Nairobi"
student["hobby"]="travelling"
student["club"]="cityzen"
student["food"]="ugali"
print(student)
#Modifying values
student["Name"]="Young"
student["school"]="Litein"
print(student)
#Removing key value pairs
del student["food"]
print(student)