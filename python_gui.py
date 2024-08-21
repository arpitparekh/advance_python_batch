# advance python
# python GUI
# tkinter library
# desktop application
# web application
# mobile application
# desktop application

# library # module
# is a collection of predefine class and methods

from tkinter import *
from tkinter.messagebox import *

# everything in tkinter is a widget
root = Tk()
root.title("My First GUI")
root.geometry("500x500")
root.resizable(False,False)
root.configure(background='lightblue')

# label

label = Label(root,text="This is a new Label Title",bg="purple",fg="white",padx=10,pady=10,font=("Times New Roman",24))
# label = Label(root,text="This is Label 1",bg="purple",fg="white",padx=10,pady=10,font=("Times New Roman",24))
label.pack()


label1 = Label(root,text="This is Label 2",bg="pink",fg="black",padx=10,pady=10,font=("Arial",24))
label1.pack()

def buttonClick():
    showinfo(title="You Clicked on a button",message="You clicked on a button")

button = Button(root,text="Click Me",command=buttonClick)
button.pack()

canvas = Canvas(root,height=200,width=200,bg="black")
canvas.create_rectangle((0,0,100,100),fill="red")
canvas.create_rectangle((100,0,200,100),fill="blue")
canvas.create_arc((50,50,150,150),fill="pink")
canvas.pack()

root.mainloop()