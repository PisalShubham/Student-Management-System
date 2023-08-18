"""
@author: Shubham Pisal
@goal: To build a regestration page for new students.
"""

import sys
import tkinter
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class Regestration:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x300+80+120")
        self.root.config(bg="white")
        self.root.focus_force()

        title = tkinter.Label(self.root, text="Generate Password",font=("goudy old style",20,"bold"),bg="orange", fg="#262626")
        title.place(x=10, y=15, width=577, height=50)

        # defining variables
        self.var_name = tkinter.StringVar()
        self.var_lname = tkinter.StringVar()
        self.var_roll = tkinter.StringVar()
        self.var_contact = tkinter.StringVar()
        self.var_email = tkinter.StringVar()
        self.password = tkinter.StringVar()

        # Labels
        lbl_name = tkinter.Label(self.root, text="First Name", font=("goudy old style",15,'bold'),bg='white')
        lbl_name.place(x=20, y=80)
        lbl_lname = tkinter.Label(self.root, text="Last Name", font=("goudy old style",15,'bold'),bg='white')
        lbl_lname.place(x=300, y=80)
        lbl_roll = tkinter.Label(self.root, text="Roll Number", font=("goudy old style",15,'bold'),bg='white')
        lbl_roll.place(x=20, y=130)
        lbl_contact = tkinter.Label(self.root, text="Contact Number", font=("goudy old style",15,'bold'),bg='white')
        lbl_contact.place(x=300, y=130)
        lbl_email = tkinter.Label(self.root, text="Email ID", font=("goudy old style",15,'bold'),bg='white')
        lbl_email.place(x=170, y=180)

        # Entries
        self.txt_name = tkinter.Entry(self.root)
        self.txt_name.configure(textvariable=self.var_name, font=("goudy old style",12),bg='white')
        self.txt_name.place(x=150, y=80, width=130)
        self.txt_lname = tkinter.Entry(self.root)
        self.txt_lname.configure(textvariable=self.var_lname, font=("goudy old style",12),bg='white')
        self.txt_lname.place(x=450, y=80, width=130)
        self.txt_roll = tkinter.Entry(self.root)
        self.txt_roll.configure(textvariable=self.var_roll, font=("goudy old style",12),bg='white')
        self.txt_roll.place(x=150, y=130, width=130)
        self.txt_contact = tkinter.Entry(self.root)
        self.txt_contact.configure(textvariable=self.var_contact, font=("goudy old style",12),bg='white')
        self.txt_contact.place(x=450, y=130, width=130)
        self.txt_email = tkinter.Entry(self.root)
        self.txt_email.configure(textvariable=self.var_email, font=("goudy old style",12),bg='white')
        self.txt_email.place(x=270, y=180, width=150)

        register_btn = tkinter.Button(self.root,  text="Register", font=("times new roman", 15), bg="green", fg="white", cursor="hand2", command=self.register)
        register_btn.place(x=200, y=250, width=150, height=30)

    def register(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_name.get() == "" or self.var_lname.get() == "" or self.var_roll.get() == "" or self.var_contact.get() == "" or self.var_email.get=="":
                messagebox.showerror("Warning","Please fill all the details")

            else:
                cur.execute(f"select roll,contact,email from student_db where roll=? and contact=? and email=?", (self.var_roll.get(), self.var_contact.get(), self.var_email.get(),))
                row = cur.fetchone()
                if row == None:
                    self.var_roll.get()
                    self.var_contact.get()
                    messagebox.showerror("Warning!","No record found!\nPlease contact to college", parent=self.root)
                else:

                    cur.execute("select * from student_login_db where roll=?", (self.var_roll.get(),))
                    row = cur.fetchone()
                
                    if row != None:
                        messagebox.showerror("Warning","Student already regester",parent=self.root)
                    else:
                        self.password = str(self.var_name.get())+"@"+str(self.var_roll.get())
                        cur.execute("insert into student_login_db (fname, lname, roll, contact, email, pass) values(?,?,?,?,?, ?)",(
                            self.var_name.get(),
                            self.var_lname.get(),
                            self.var_roll.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.password
                        ))
                        
                        print(str(self.password))

                        #cur.execute("insert into student_db(pass) values(?)",(
                        #self.password.get(),
                        #))
                        con.commit()
                        messagebox.showinfo("Registrarion Successful","Username - "+str(self.var_email.get())+"\nPassword - "+str(self.var_name.get())+"@"+str(self.var_roll.get()))
                        self.clear_details()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def clear_details(self):

        self.var_name.set("")
        self.var_lname.set("")
        self.var_roll.set("")
        self.var_contact.set("")
        self.var_email.set("")


def main():
    if __name__ == "__main__":
        root_window = tkinter.Tk()
        obj = Regestration(root_window)
        root_window.mainloop()

        sys.exit(0)
main()