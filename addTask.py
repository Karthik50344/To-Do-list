from tkinter import *
from tkinter import messagebox
import mysql.connector

def add_db():
    
    global id
    global task

    tid=id.get()
    ttask=task.get()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'karthik',database='todo')
    cursor = db.cursor()

    sqlquery= "insert into todolist values('" + tid +"','"+ttask+"','NO');"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Task added Successfully")
    except:
        messagebox.showinfo("Error","Cannot access Database")
    

def add():

    global id
    global task
    
    window=Tk()
    window.title("To-Do List")

    greet = Label(window, font = ('arial', 20), text = "Add a Task !")
    greet.grid(row = 0,columnspan = 3)

    #----------id-------------------
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Task id: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15), text = "   ")
    L.grid(row = 2, column = 2)

    id=Entry(window,width=5,font =('arial', 15))
    id.grid(row=2,column=3)

    #------------------task---------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter task: ")
    L.grid(row = 3, column = 1)

    L = Label(window, font = ('arial', 15), text = "   ")
    L.grid(row = 3, column = 2)

    task=Entry(window,width=5,font =('arial', 15))
    task.grid(row=3,column=3)

    submitbtn=Button(window,text="Submit",command=add_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=5,columnspan=3)
    mainloop()
        
    pass
