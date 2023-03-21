from tkinter import *
from turtle import bgcolor, bgpic 

root = Tk()
root.title("Practice")
root.configure(width=1000, height=700)
root.configure(bg='red')

    
greet=Label(root, font = ('arial', 20, 'bold'),text="Special Gift to Nar!!!", bg='red').grid(row=1,columnspan=3)
btn1 = Button(root,text="Show Gift",bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3)

window2 = Tk()
window2.title("Warning!!!")

msg1=StringVar()

greet2= Label(root, font = ('arial', 20, 'bold'),text="Type: I love you", bg='red')
greet2.grid(row=1,columnspan=3)
msgbtn = Entry(root,textvariable=msg1,width=5,font =('arial', 20, 'bold'))
msgbtn.grid(row=2,column=1)
btn2 = Button(root,text="set alarm",bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3)

mainloop()