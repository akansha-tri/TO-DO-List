from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
from main import *


db = mysql.connector.connect(host="localhost",user="root",password="Akansha@26",database="project")
mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x120+670-300")
    Label(err,text="All fields are required..",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("250x120+680-300")
    succ.iconbitmap("favicn.ico")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=10, height=1, command=succ_destroy).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    if username_info == "":
        error()
    elif password_info == "":
        error()
    else:
        sql = "insert into login values(%s,%s)"
        t = (username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        success()


def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration")
    root1.geometry("400x300+570-200")
    root1.iconbitmap("favicn.ico")
    global username
    global password
    Label(root1,text="Register your account",bg="grey",fg="black",font="bold",width=300).pack()
    username = StringVar()
    password = StringVar()
    Label(root1,text="").pack()
    Label(root1,text="Username :").pack()
    Entry(root1,textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="Password :").pack()
    Entry(root1, textvariable=password,show="*").pack()
    Label(root1, text="").pack()
    Button(root1,text="Register",bg="red",width=8,command=register_user).pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In")
    root2.geometry("400x300+570-200")
    root2.iconbitmap("favicn.ico")
    global username_varify
    global password_varify
    Label(root2, text="Enter Your Credentials", bg="grey", fg="black", font="bold",width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="red",width=8, height=1, command=login_varify).pack()
    Label(root2, text="")

def fail_destroy():
    fail.destroy()

def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("200x120+670-300")
    logg.iconbitmap("favicn.ico")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Enter", bg="grey", width=8, height=1, command=main).pack()
    root2.withdraw()


def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x120+670-300")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()


def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from login where user = %s and password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()
    root.withdraw()


def main_screen():
    global root
    root = Tk()
    root.title("Login/Register")
    root.geometry("400x300+570-200")
    root.iconbitmap("favicn.ico")
    Label(root,text="Welcome to Personal Planner",font="bold",bg="grey",fg="black",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="LogIn",width="8",height="1",bg="dark blue",fg="white",font="bold",command=login).pack(pady=30)
    #Label(root,text="").pack()
    Button(root, text="Registration",height="1",width="15",bg="dark blue",fg="white",font="bold",command=registration).pack()
    Label(root,text="").pack()
    Label(root,text="").pack()

main_screen()
root.mainloop()
