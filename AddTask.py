from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


def addtasks():
    
    ids = taskInfo1.get()
    title = taskInfo2.get()
    descr = taskInfo3.get()
    hours = taskInfo4.get()
    
    inserttask = "insert into "+taskTable+" values('"+ids+"','"+title+"','"+descr+"','"+hours+"')"
    try:
        cur.execute(inserttask)
        con.commit()
        messagebox.showinfo('Success',"Task added successfully")
    except:
        messagebox.showinfo("Error","Can't add task into Database")
    
    print(ids)
    print(title)
    print(descr)
    print(hours)

    root.destroy()
    
def addTask(): 
    
    global taskInfo1,taskInfo2,taskInfo3,taskInfo4,Canvas1,con,cur,taskTable,root
    
    root = Tk()
    root.title("Add Task")
    root.minsize(width=400,height=400)
    root.geometry("600x500+443-70")
    root.iconbitmap("favicon.ico")
   
 

    con = pymysql.connect(host="localhost",user="root",password="Akansha@26",database="project")
    cur = con.cursor()

    taskTable = "tasks" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#A9A9A9")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FF4500",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Tasks", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    
    lb1 = Label(labelFrame,text="Task ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    taskInfo1 = Entry(labelFrame)
    taskInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
  
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    taskInfo2 = Entry(labelFrame)
    taskInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    
    lb3 = Label(labelFrame,text="Description : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    taskInfo3 = Entry(labelFrame)
    taskInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
   
    lb4 = Label(labelFrame,text="Time Required : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    taskInfo4 = Entry(labelFrame)
    taskInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    
    SubmitBtn = Button(root,text="ADD",bg='white', fg='black',command=addtasks)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
