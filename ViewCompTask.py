from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql



con = pymysql.connect(host="localhost",user="root",password="Akansha@26",database="project")
cur = con.cursor()


taskTable = "comptasks" 
    
def ViewComp(): 
    
    root = Tk()
    root.title("View Tasks")
    root.minsize(width=400,height=400)
    root.geometry("600x500+443-70")
    root.iconbitmap("favicon.ico")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#808080")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Completed Tasks", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.26,relwidth=0.8,relheight=0.60)
    y = 0.2
    
    Label(labelFrame, text="%-40s%-60s%-65s"%('ID','Title','Time Required'),bg='black',fg='white').place(relx=0.07,rely=0.06)
    Label(labelFrame, text="-------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.14)
    getTasks = "select * from "+taskTable
    
    try:
        cur.execute(getTasks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-40s%-60s%-65s"%(i[0],i[1],i[2]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.06
    except:
        messagebox.showinfo("Failed to fetch data from database")

    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

