#!usr\bin|python
######################################################################################
#name : Eugene Martins Maloba

#date : 30/5/2022
#########################################################################################
#if ------ elif
acc_bal=int(input("Enter your acc balance:"))
if (int(acc_bal) > 100000 and int(acc_bal) < 200000):
    acc_bal=acc_bal-25000
    print("we have deducted Ksh 25000 from your account\nacc_bal")
elif(int(acc_bal) > 500000 and int(acc_bal) < 1000000):
    acc_bal=acc_bal-(0.3*acc_bal)
    print("we have deducted Ksh (0.3 of acc_bal)from your account")
elif(int(acc_bal) > 1000000):
   acc_bal=acc_bal-150000
   print("we have deducted Ksh 150000 from your account")  
   #if-------else
age=int(input("what is your age ? "))
acc_bal=0
if (age > 25) and (age < 30):
    acc_bal= acc_bal+100000
    print("Hurrah.You have received 100000")
else:
    print("sorry")    


