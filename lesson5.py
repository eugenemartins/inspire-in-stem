#!usr\bin|python

######################################################################################
#name : Eugene Martins Maloba

#date : 21/5/2022
##########################################################################################
age=17
userName="Kevin Otii"
name="Maloba Martins"
person="I am "+ str(name) +" and my age is" + str(age)
#print(person)
#print("I am"+ str(name)+ "and my age is" + str(age))
#the format method
print("my name is {} and I am {} years old".format(name,age))
#newline \n and \t
print(f"My name is {name} \n and I am {age} yeras old")
print(userName.lstrip)
print("Monday\tTuesday\tWednesday\tThusday\tFriday\tSaturday\tSunday")
print("kisumu\nnyeri\nmombasa")
#mutliple strings
msg=""" QRST126XDG MPESA confirmed
      you have receieved ksh 600 
      from Titus
      12th May 2020"""
print(msg) 
#slice
#slice from the start
city="Nairobi"
print(city[:5])
print(city[2:])
print(city[:3])
print(city[:-1])



f_name="eugene maloba"#small letters
#.upper() convert to upper case
print(f_name.upper())
s_name = "MALOBA MARTINS"
print(s_name.lower())

#concatination-converting from one data type to another
number=6
print(str(number))
#int-> float float(x)
#float->int  int(x)
#int->string  str(x)
x=4
print(float(x))
y=6.7897
print(str(y))
print(float(y))
print(int(y))
f_name="Eugene"
s_name="Martins"
full_name=f_name+s_name
print(full_name)
#the replace() method replaces a string with another character
name="Ray Grat"
print(name.replace('t','y'))
print(name.replace('G','B'))
#the split() 
msg=""" QRST126XDG MPESA confirmed
      you have receieved ksh 600 
      from Titus
      12th May 2020"""
print(msg.split())
print(len(msg))
print(msg.strip())





