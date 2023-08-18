"""
@author: Shubham Pisal
@goal: To build a homepage window for student login.
"""

import sys
import tkinter
import os
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from report_for_student import StudentReport

class StudentDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="../img/book.jpg")
        self.bg_image = tkinter.Label(self.root, image=self.bg, bd=0)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        #logo
        self.logo_dash = ImageTk.PhotoImage(file="../img/logo.jpg")

        title = tkinter.Label(self.root, text="Student Management System",padx=10,compound="right", image=self.logo_dash, font=("goudy old style",20,"bold"),bg="lightgrey", fg="Black")
        title.place(x=0, y=0, relwidth=1, height=50)


        student_result_btn = tkinter.Button(self.root, text="View Student Result", font=("goudy old style",20,"bold"), command=self.view_result, bg="#a81414",fg="white",cursor="hand2")
        student_result_btn.place(x=30, y=200, width=250, height=50)
        logout_btn = tkinter.Button(self.root, text="Logout", font=("goudy old style",20,"bold"), command=self.logout, bg="#a81414",fg="white",cursor="hand2")
        logout_btn.place(x=30, y=300, width=190, height=50)
        exit_btn = tkinter.Button(self.root, text="Exit", font=("goudy old style",20,"bold"), command=self.exit, bg="#a81414",fg="white",cursor="hand2")
        exit_btn.place(x=30, y=400, width=190, height=50)

        footer = tkinter.Label(self.root, text="SMS-Student Management System\nContact Us: SMSTechnical@gmail.com", font=("goudy old style",12,"bold"),bg="#262626", fg="white")
        footer.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    def view_result(self):
        self.new_win = tkinter.Toplevel(self.root)
        self.new_obj = StudentReport(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm","Do you really want to logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python student_login.py")

    def exit(self):
        op = messagebox.askyesno("Confirm","Do you really want to exit?", parent=self.root)
        if op == True:
            self.root.destroy()


def main():

    if __name__ == "__main__":
        root_window = tkinter.Tk()
        obj = StudentDashboard(root_window)
        root_window.mainloop()

        sys.exit(0)
main()