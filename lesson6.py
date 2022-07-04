#!usr\bin|python
######################################################################################
#name : Eugene Martins Maloba

#date : 24/5/2022

#lists
#########################################################################################
#Learning about lists
plate_number=['H3456','S345','Y23456']
motorcycle=['honda','suzuki','yamaha']
#Accessing list items using index
print(motorcycle)
print(motorcycle[0])
print(motorcycle[-2])

motorcycle[1]="Bugatti"#changing element in a list
print("I love"+str (motorcycle[0]))

#Adding element in a list
motorcycle.append("Bugatti yonaha")#adding item into a list
print(motorcycle)
motorcycle[1]="Haojin"
print(motorcycle[1])
#Task---print the motorcycle and their plate

print(str(motorcycle[0])+str(plate_number[0]))
print(str(motorcycle[1])+str(plate_number[1]))
print(str(motorcycle[2])+str(plate_number[2]))
#Deleting an item from a list---del
del motorcycle[2]
print(motorcycle)
popped_motorcycle=motorcycle.pop()
print(popped_motorcycle)
print(motorcycle)
#task-- #my name is Mojo Jojo and I own a motorcycle plate number
print("my name is Mojo Jojo and I own a " +str(motorcycle[0]) +str(plate_number[0]))
# removing an item from a list
motorcycle.remove("honda")
print(motorcycle)
# loops
school=['joy','hope','mercy','happy']
pupil=['patience','peace','amani','love']
# Hard way
print(f"I am {pupil[0]} and I school at {school[0]}")
print(f"I am {pupil[1]} and I school at {school[1]}")
print(f"I am {pupil[2]} and I school at {school[2]}")
print(f"I am {pupil[3]} and I school at {school[3]}")

for pupil in pupil:
 print(f"Hello, I am pupil at {pupil}")