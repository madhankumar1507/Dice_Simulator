import random
from tkinter import * 
from PIL import ImageTk,Image
root=Tk()
root.geometry('700x450')
l1=Label(root,text='',font=('times',200))
l1=Label(root,text="Dice SImulator",fg="yellow",bg="black",font="Helvetica 16 bold ")
l1.pack()


def roll():
    rand=random.randint(1,6)
    print(rand)
    if rand==1:
       
       load = Image.open("dice1.png")
       render = ImageTk.PhotoImage(load)
       img = Label(image=render)
       img.image = render
       img.place(x=230, y=100)
    elif rand==2:
        
        load = Image.open("dice22.png")
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=230, y=100)
    
    elif rand==4:
        
        load = Image.open("dice44.png")
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=230, y=100)
    elif rand==5:
        
        load = Image.open("dice55.png")
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=230, y=100)
    elif rand==6:
        
        load = Image.open("dice66.png")
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=230, y=100)
    elif rand==3:
    
        load = Image.open("dice33.png")
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=230, y=100)
    
    
    
roll_btn = PhotoImage(file='roll.png')
img_label = Label(image=roll_btn)    
b1=Button(root,image=roll_btn,command=roll,borderwidth=0,width=100,height=50)
b1.pack(pady=20)
b1.place(x=300,y=400)



root.mainloop()