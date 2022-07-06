#!\usr\bin\python

##################################################################################

#Eugene Maloba
#date : 7/6/2022
# gui_examples using tkinter

from cProfile import label
from tkinter import *
from turtle import width

window = Tk( )

window.title("welcome to my  APP")
window.configure(bg= "grey")
window.geometry("400x400")#
# window.mainloop( )
f_name = Label(window,text ="First name" , font = ("AriaL",20))
s_name = Label(window,text ="Second name" , font = ("AriaL",20))
f_name.grid(column = 60, row = 100)
s_name.grid(column = 60, row = 120)
# window.mainloop()
def open_popup():
    # top = Toplevel(window)
    # top.geometry('300x300')
    # top.title('Pop Up Window')
    # Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)
    # top.configure(bg = "black")
 
    # msg= Label(top,text ="welcome to pop up",bg = 'blue',fg = 'green' ,command = open_popup().pack())
    
# window.mainloop( )

    btn = Button(window,text = ('click me'),bg = "blue", font = ('oswarld',12))
    btn.grid(column = 100,row = 180)
# window.mainloop()

f_name_box = Entry(window, width =20)
s_name_box = Entry(window ,width = 20)
f_name_box.grid(column = 100 , row = 100)
s_name_box.grid(column = 100, row = 120)

# def open_popup():
#     top = Toplevel(window)
#     top.geometry('300x300')
#     top.title('Pop Up Window')
#     top.configure(bg = "black")
 
#     msg= Label(top,text ="welcome to pop up",bg = 'blue',fg = 'green' ,command = open_popup().pack())
    
window.mainloop()
