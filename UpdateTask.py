from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
#from main import *


taskTable = "tasks"  


def updateTask():

    ids = taskInfo1.get()
    title = taskInfo2.get()
    hours = taskInfo4.get()

    if (ids=="" or title=="" or hours==""):
        messagebox.showinfo('Error',"All fields required")
    else:
        con = pymysql.connect(host="localhost",user="root",password="Akansha@26",database="project")
        cursor = con.cursor()
        cursor.execute("update tasks set title='"+title+"', hours='"+hours+"' where ids='"+ids+"'")
        cursor.execute("commit");

        taskInfo1.delete(0,'end')
        taskInfo2.delete(0,'end')
        taskInfo4.delete(0,'end')
        messagebox.showinfo('Success',"Task Updated successfully")
        con.close();
    root.destroy()

def update(): 
    
    global taskInfo1,taskInfo2,taskInfo3,taskInfo4,Canvas1,con,cur,taskTable,root
    
    root = Tk()
    root.title("Update Task")
    root.minsize(width=400,height=400)
    root.geometry("600x500+443-70")
    root.iconbitmap("favicon.ico")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#A9A9A9")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#800000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Update Task", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        

    lb1 = Label(labelFrame,text="Task ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.15)
        
    taskInfo1 = Entry(labelFrame)
    taskInfo1.place(relx=0.3,rely=0.15, relwidth=0.62)
    
    lb2 = Label(labelFrame,text="Task Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25)
        
    taskInfo2 = Entry(labelFrame)
    taskInfo2.place(relx=0.3,rely=0.25, relwidth=0.62)

    lb3 = Label(labelFrame,text="Updated Task : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.55)
        
    taskInfo2 = Entry(labelFrame)
    taskInfo2.place(relx=0.3,rely=0.55, relwidth=0.62)

    lb4 = Label(labelFrame,text="Previous Hours : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.35)
        
    taskInfo4 = Entry(labelFrame)
    taskInfo4.place(relx=0.3,rely=0.35, relwidth=0.62)

    lb5 = Label(labelFrame,text="Updated Hours : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.65)
        
    taskInfo4 = Entry(labelFrame)
    taskInfo4.place(relx=0.3,rely=0.65, relwidth=0.62)
    

    SubmitBtn = Button(root,text="Update",bg='white', fg='black',command=updateTask)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
