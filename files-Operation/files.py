# f = open("demofile.txt")
# print(f.read()) #read the file
# print(f.read(120))# read part of the file-input characters
# print(f.readline())
# print(f.readline())
# print(f.readline())  #read a line i.e first 5 lines
# f.close()  #close a file
#overwriting an existing file
# f = open("demofile.txt","w")
# f.write("I schooled at Litein High")
# f.write("\nI love listening to music")
# f.write("\nI am Eugene Martins Maloba")
# f.write("\nLearning python is fun")
# f.write("\nDo or die")
# f.write("\nThe gift of life from God")
# f.write("\nInterested in learning Data Science")
# f.write("\nMathematics is my best subject")
# f.close()
# open and read the file
# f = open("demofile.txt",'r')
# print(f.read())
# f = open("demofile.txt",'w')
# f.write("wow!I love python ")
# f.close()
# f = open("demofile.txt",'r')
# print(f.read())

# f=open("demofile.txt",'r')
# print(f.read())

#appending a file
# f =open("demofile.txt",'a')
# f.write("\nI am a BOY")
# f= open("demofile.txt",'r')
# print(f.read())

# create a file
# f =open("my file.txt",'x')
# f =open("ken1.txt",'a')
# f =open("ken.txt",'w')

#delete a file
# import os
# os.remove("my file.txt")
# if os.path.exists("ken1.txt"):#check if file is removed
    # os.remove("ken1.txt")
# else:
    # print("file do not exist")
    
#delete a folder
import os
os.rmdir("folder")   
