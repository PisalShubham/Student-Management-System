"""
@author: Shubham Pisal
@goal: To build a login page for student
"""

import sys
import tkinter 
import sqlite3
import os
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from student_dashboard import StudentDashboard
from regester import Regestration

class StudentLogin:
    def __init__(self, root):
        # background
        self.root = root
        self.root.title("Student Management Sysytem")
        self.root.geometry("1300x700+0+0")
        self.root.focus_force()

        self.bg = ImageTk.PhotoImage(file="../img/university.jpg")
        self.bg_image = tkinter.Label(self.root, image=self.bg, bd=0)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)
        # login frame
        login_frame = tkinter.Frame(self.root, bg="white", bd=0)
        login_frame.place(x=330, y=150, width=600, height=440)

        title = tkinter.Label(login_frame, text="Login Here", font=("Impact", 35,"bold"),bg="white", fg="#d77337")
        title.place(x=180, y=30)

        lbl_user = tkinter.Label(login_frame, text="Username", font=("goudy old style", 20,"bold"),bg="white", fg="black")
        lbl_user.place(x=90, y=140)
        self.var_username = tkinter.StringVar()
        self.txt_user = tkinter.Entry(login_frame, textvariable=self.var_username, font=("times new roman", 15),bg="lightgray", bd=0)
        self.txt_user.place(x=100, y=180, width=350, height=35)

        lbl_pass = tkinter.Label(login_frame, text="Password", font=("goudy old style", 20,"bold"),bg="white", fg="black")
        lbl_pass.place(x=90, y=230)
        self.var_pass = tkinter.StringVar()
        self.txt_pass = tkinter.Entry(login_frame, show='*', textvariable=self.var_pass, font=("times new roman", 15),bg="lightgray", bd=0)
        self.txt_pass.place(x=100, y=270, width=350, height=35)

        forgot_btn = tkinter.Button(login_frame,  text="Forgot Password?", font=("times new roman", 12), command=self.forgot, bg="white", fg="black",bd=0, activebackground="white")
        forgot_btn.place(x=330, y=310)
        register_btn = tkinter.Button(login_frame,  text="New Registeratation", font=("times new roman", 12), command=self.clicked_register, bg="white", fg="black",bd=0, activebackground="white")
        register_btn.place(x=100, y=310)

        # Back button 
        self.back_btn_img = ImageTk.PhotoImage(file="../img/back_logo.jpg")
        back_btn = tkinter.Button(login_frame, image=self.back_btn_img, bd=0, bg="white", fg="white", activebackground="white", command=self.back)
        back_btn.place(x=5, y=5)

        login_btn = tkinter.Button(self.root,  text="Login", font=("times new roman", 20), command=self.login , bg="#d77337", fg="white", cursor="hand2")
        login_btn.place(x=530, y=560, width=180, height=40)

    
    def login(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_username.get == "" or self.var_pass.get() == "":
                messagebox.showerror("Warning","Please fill all the details")

            else:
                cur.execute(f"select * from student_login_db where email=? and pass=?", (self.var_username.get(), self.var_pass.get()))
                row = cur.fetchone()
                if row != None:
                    self.clicked_login()
                    self.clear()

                else:
                    messagebox.showerror("Warning!","Incorrect Username or Password!\nPlease register first", parent=self.root)

            
            con.close()
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def forgot(self):
        messagebox.showerror("Forgot Password!","Please contact to the college admin for username pasword", parent=self.root)
        self.clear()

    def clear(self):
        self.var_username.set("")
        self.var_pass.set("")

    def clicked_login(self):
        self.root.destroy()
        os.system("python student_dashboard.py")

    def clicked_register(self):
        self.new_win = tkinter.Toplevel(self.root)
        self.new_obj = Regestration(self.new_win)
        self.clear()

    def back(self):
        self.root.destroy()
        os.system("python main_page.py")


def main():

    if __name__ == "__main__":
        root_window = tkinter.Tk()
        student_obj = StudentLogin(root_window)
        root_window.mainloop()

        sys.exit(0)
main()