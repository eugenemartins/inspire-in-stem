#!usr\bin|python

######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022
#############################################################################################################################################
#A dictionary is a collection  of a key value pair:key;pair
#syntax:dictionary={"key":"value"}
list_names=['john','mary']#use type method to find data type
colors={'color':'red'}
vehicle={'type':'toyota','plate_number':'hfh8098'}
print(type(list_names))
# accessing values in a dictionary
print(vehicle['type'])#you can access an element in a dictionary using the'key'
print(vehicle['type'],vehicle['plate_number'])
person={'Name':'kim','age':'24','Gender':'Male','Residence':'Juja','Address':'00200'}
person['phoneNo']='0985758298729'
print(type(person))
print(type(person['Name'].title()))
print(person)
print(person['Gender'])
# print(person['password'])#it will give an error

#looping over dictionaries-"for_in and while loops

for key,value in person.items():
    print(f"{key}:{value}")

colors=['red','green','blue','orange']
i = 1
while i <len(colors):
    if(colors[0]=='red'):
         print(colors[0].upper())
         i +=1

i = 1
while i <len(colors):
     if(colors[1]=='green'):
         print(colors[1].upper())
         i +=1

i = 1
while i <len(colors):
    if(colors[2]=='blue'):
        print(colors[2].upper())
        i +=1

i = 1
while i <len(colors):
    if(colors[3]=='orange'):
        print(colors[3].upper())
        i +=1

#using get to access the value in a dictionary
# print(person.get('location','the\'item\'is non-existence'))
# print(person.get('Residence'))


mary_fav_food = ['beef','chicken','vegetable']
jane_fav_food = ['rice','ugali','potato']
#Dictionary containing the above
fav_food = {
    'mary':['beef','chicken','vegetable'], 
    'jane':['rice','ugali','potato']
     }
# print(fav_food) 

for key,value in fav_food.items() : 
    print(f"'{key}':'{value}'") 
        
    

