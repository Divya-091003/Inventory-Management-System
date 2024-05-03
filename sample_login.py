from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login for IMS | Developed by Archana and Divya")
        self.root.geometry("1350x700+0+0")
        self.phone_image = ImageTk.PhotoImage(file="images/login1.jpeg")
        self.lbl_Phone_Image = Label(self.root, image=self.phone_image).place(x=100, y=100, width=700)

        # login frame
        login_frame = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        login_frame.place(x=725, y=90, width=350, height=360)

        title = Label(login_frame, text="Login", bg="white", font=("Elephant", 30, "bold")).place(x=0, y=30, relwidth=1)
        
        lbl_user = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171").place(x=30, y=100)
        self.employee_id=StringVar()
        self.password=StringVar()
        txt_employee_id = Entry(login_frame,textvariable=self.employee_id, font=("times new roman", 15), bg="#ECECEC")
        txt_employee_id.place(x=30, y=140, width=250)

        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=30, y=180)
        txt_pass = Entry(login_frame, font=("times new roman", 15),show="*",textvariable=self.password,bg="#ECECEC")
        txt_pass.place(x=30, y=220, width=250)

        self.user_type = StringVar()
        self.user_type.set("Employee")  # Default selection
        lbl_type = Label(login_frame, text="Login As:", font=("Andalus", 15), bg="white", fg="#767171").place(x=30, y=260)
        Radiobutton(login_frame, text="Employee", variable=self.user_type, value="Employee", bg="white").place(x=150, y=260)
        Radiobutton(login_frame, text="Admin", variable=self.user_type, value="Admin", bg="white").place(x=240, y=260)

        btn_login=Button(login_frame,text="Log in",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        ##frame2
        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=725, y=470, width=350, height=60)

        lbl_reg=Label(register_frame,text="Welcome to AD IMS",font=("times new roman",11,"bold"),bg="white").place(x=100,y=15)
        
    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror('Error',"All fields are required",parent=self.root)
            else:  
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error',"Invalid Username/Password",parent=self.root)
                else:
                    if user[0]=="Employee" and self.user_type.get() == "Employee":
                        self.root.destroy()
                        os.system("python billing.py")    
                    elif user[0]=="Admin" and self.user_type.get() == "Admin":
                        self.root.destroy()
                        os.system("python d.py")
                    else:
                        messagebox.showerror('Error',"Invalid User Type",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error dur to: {str(ex)}",parent=self.root)
            
root = Tk()
obj = Login_System(root)
root.mainloop()
