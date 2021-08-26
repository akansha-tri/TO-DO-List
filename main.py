import tkinter
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddTask import *
from DeleteTask import *
from ViewTask import *
from UpdateTask import *
from DataAnalysis import *
from CompletedTask import *




con = pymysql.connect(host="localhost",user="root",password="Akansha@26",database="project")
cur = con.cursor()

def main():

    root = Toplevel()
    root.title("Dashboard")
    root.minsize(width=400,height=400)
    root.geometry("1370x800")
    root.iconbitmap("favicon.ico")

    load = Image.open("todo.png")
    render = ImageTk.PhotoImage(load)
    img = Label(root,image = render)
    img.place(x=0,y=0)

    headingFrame1 = Frame(root,bg="#87CEEB",bd=5)
    headingFrame1.place(relx=0.18,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \n Your Personal Manager", bg='black', fg='white', font=('yesteryear',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #photo=PhotoImage(file=r"C:\Users\admin\Desktop\python-rait\Main Project\delete.png")
    #image=photo,compound=LEFT

    btn1 = Button(root,text="Add Your Task",bg='black',fg='white',font=('Courier',20),command=addTask)
    btn1.place(relx=0.26,rely=0.32, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Delete Task",bg='black', fg='white',font=('Courier',20),command=delete)
    btn2.place(relx=0.26,rely=0.42, relwidth=0.45,relheight=0.1)
                    
    btn3 = Button(root,text="Update Task",bg='black', fg='white',font=('Courier',20),command=update)
    btn3.place(relx=0.26,rely=0.52, relwidth=0.45,relheight=0.1)
                    
    btn4 = Button(root,text="View Task List",bg='black', fg='white',font=('Courier',20),command=View)
    btn4.place(relx=0.26,rely=0.62, relwidth=0.45,relheight=0.1)

    btn6 = Button(root,text="Completed Task",bg='black', fg='white',font=('Courier',20),command=compTask)
    btn6.place(relx=0.26,rely=0.72, relwidth=0.45,relheight=0.1)
                  
    btn5 = Button(root,text="LOGOUT",bg='grey',borderwidth=12, fg='black',font=('Courier',20,"bold"),command=root.destroy)
    #btn5.place(relx=0.36,rely=0.85, relwidth=0.30,relheight=0.1)
    btn5.place(x=593,y=685,relheight=0.1,relwidth=0.2)


    root.mainloop()

