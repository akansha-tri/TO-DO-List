
from tkinter import *
from PIL import ImageTk,Image
from login import *






root = Tk()
root.title("Dashboard")
root.minsize(width=400,height=400)
root.geometry("1370x800")
root.iconbitmap("favicon.ico")

load = Image.open("todo.png")
render = ImageTk.PhotoImage(load)
img = Label(root,image = render)
img.place(x=0,y=0)

headingFrame = Frame(root,bg="#87CEEB",bd=5)
headingFrame.place(relx=0.18,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Your Personal Manager", bg='black', fg='white', font=('yesteryear',25))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #photo=PhotoImage(file=r"C:\Users\admin\Desktop\python-rait\Main Project\delete.png")
    #image=photo,compound=LEFT

btn1 = Button(root,text="get started",bg='black',fg='white',font=('Courier',20),command=main_screen)
btn1.place(relx=0.26,rely=0.42, relwidth=0.45,relheight=0.1)



root.mainloop()


