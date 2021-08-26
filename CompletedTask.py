from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from ViewCompTask import *

def comptasks():
    
    ids = comptaskInfo1.get()
    title = comptaskInfo2.get()
    hours = comptaskInfo4.get()
    
    inserttask = "insert into "+taskTable+" values('"+ids+"','"+title+"','"+hours+"')"
    try:
        cur.execute(inserttask)
        con.commit()
        messagebox.showinfo('Success',"Task added successfully")
    except:
        messagebox.showinfo("Error","Can't add task into Database")
    
    print(ids)
    print(title)
    print(hours)

    root.destroy()
    
def compTask(): 
    
    global comptaskInfo1,comptaskInfo2,comptaskInfo3,comptaskInfo4,compCanvas1,con,cur,taskTable,root
    
    root = Tk()
    root.title("Completed Task")
    root.minsize(width=400,height=400)
    root.geometry("600x500+443-70")
    root.iconbitmap("favicon.ico")

   
   
   

    con = pymysql.connect(host="localhost",user="root",password="Akansha@26",database="project")
    cur = con.cursor()

    taskTable = "comptasks" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#A9A9A9")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#4169E1",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Completed Tasks", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)
        
   
    lb1 = Label(labelFrame,text="Task ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.32, relheight=0.08)
        
    comptaskInfo1 = Entry(labelFrame)
    comptaskInfo1.place(relx=0.3,rely=0.32, relwidth=0.62, relheight=0.08)
        
   
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.45, relheight=0.08)
        
    comptaskInfo2 = Entry(labelFrame)
    comptaskInfo2.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)
        
  
    lb3 = Label(labelFrame,text="Time Spent : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.58, relheight=0.08)
        
    comptaskInfo4 = Entry(labelFrame)
    comptaskInfo4.place(relx=0.3,rely=0.58, relwidth=0.62, relheight=0.08)
        
    
    SubmitBtn = Button(root,text="ADD",bg='white', fg='black',command=comptasks)
    SubmitBtn.place(relx=0.21,rely=0.88, relwidth=0.18,relheight=0.08)

    viewBtn = Button(root,text="View Tasks",bg='white', fg='black', command=ViewComp)
    viewBtn.place(relx=0.41,rely=0.88, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.61,rely=0.88, relwidth=0.18,relheight=0.08)

    
    
    root.mainloop()
