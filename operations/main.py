#!usr\bin|python

######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022

import operations
print(operations.sum_numbers(4,6))
print(operations.divide_numbers(9,6))
print(operations.multi_numbers(6,7))
print(operations.sub_numbers(20,9))


# import student

# student = student('Joan','cycling',2004)
# print(student.greet_student())


from teachers import Teachers

new_teacher = Teachers('Mr.tito',123445,'history',600000)
print(new_teacher.get_tsc_no())