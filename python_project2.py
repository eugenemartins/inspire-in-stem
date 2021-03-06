
# How to come up with a digital clock
# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('uppreugbuf')

# This function displays time on the label
def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('Times new roman', 50, 'bold'),
			background = 'purple',
			foreground = 'white')

# Placing clock at the bottom
# of the tkinter window
lbl.pack(anchor = 'se')
time()

mainloop()
