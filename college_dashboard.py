"""
@author: Shubham Pisal
@goal: To build a home page window for teachers login.
"""

import sys
import tkinter
import os
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from course import CourseClass
from student import StudentClass
from add_result import ResultClass
from report import ReportClass
from support import SupportClass


class CollegeDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="white")

        #logo
        self.logo_dash = ImageTk.PhotoImage(file="../img/logo.jpg")
        #self.logo_dash = self.logo_dash.resize((20,10), Image.ANTIALIAS)

        

        #title
        title = tkinter.Label(self.root, text="Student Management System",padx=10,compound="right", image=self.logo_dash, font=("goudy old style",20,"bold"),bg="lightgrey", fg="black")
        title.place(x=0, y=0, relwidth=1, height=50)

        #menu bar frame
        main_frame = tkinter.LabelFrame(self.root, text="Menu", font=("times new roman", 25),bg="white")
        main_frame.place(x=50,y=100,width=500,height=400)

        #menu buttons
        course_btn = tkinter.Button(main_frame, text="Course", font=("goudy old style",20,"bold"),command=self.add_course, bg="#a81414",fg="white",cursor="hand2")
        course_btn.place(x=30, y=30, width=180, height=50)
        student_btn = tkinter.Button(main_frame, text="Student", font=("goudy old style",20,"bold"),command=self.add_student, bg="#a81414",fg="white",cursor="hand2")
        student_btn.place(x=260, y=30, width=170, height=50)
        result_btn = tkinter.Button(main_frame, text="Result", font=("goudy old style",20,"bold"),command=self.add_student_result,bg="#a81414",fg="white",cursor="hand2")
        result_btn.place(x=30, y=150, width=170, height=50)
        student_result_btn = tkinter.Button(main_frame, text="View Result", font=("goudy old style",20,"bold"),bg="#a81414",fg="white",cursor="hand2", command=self.view_result)
        student_result_btn.place(x=260, y=150, width=180, height=50)
        logout_btn = tkinter.Button(main_frame, text="Logout", font=("goudy old style",20,"bold"), command=self.logout, bg="#a81414",fg="white",cursor="hand2")
        logout_btn.place(x=30, y=270, width=170, height=50)
        exit_btn = tkinter.Button(main_frame, text="Exit", font=("goudy old style",20,"bold"), command=self.exit, bg="#a81414",fg="white",cursor="hand2")
        exit_btn.place(x=260, y=270, width=170, height=50)

        support_btn = tkinter.Button(self.root,  text="Teacher Support", font=("times new roman", 15),command=self.view_support, bg="white", bd=0, fg="black", activebackground="white", cursor="hand2")
        support_btn.place(x=0, y=600, width=200, height=40)

        #total tabs
        self.total_student = tkinter.Label(self.root, text="Total Students\n[0]",font=("goudy old style",18),bd=10,relief=tkinter.RIDGE,bg="#e43b06",fg="white")
        self.total_student.place(x=820, y=550,width=200,height=80)
        self.total_course = tkinter.Label(self.root, text="Total Courses\n[0]",font=("goudy old style",18),bd=10,relief=tkinter.RIDGE,bg="#e43b06",fg="white")
        self.total_course.place(x=1050, y=550,width=200,height=80)

        #self.bg = ImageTk.PhotoImage(file="../img/50472.jpg")
        #self.bg_image = tkinter.Label(self.root, image=self.bg, bd=0)
        #self.bg_image.place(x=500, y=50, relwidth=1, relheight=1)


        footer = tkinter.Label(self.root, text="SMS-Student Management System\nContact Us: SMSTechnical@gmail.com", font=("goudy old style",12,"bold"),bg="#262626", fg="white")
        footer.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.update_count()


    def update_count(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.total_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student_db")
            cr = cur.fetchall()
            self.total_student.config(text=f"Total Students\n[{str(len(cr))}]")

            self.total_course.after(200,self.update_count)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add_course(self):
        self.new_win = tkinter.Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = tkinter.Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_student_result(self):
        self.new_win = tkinter.Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def view_result(self):
        self.new_win = tkinter.Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)

    def view_support(self):
        self.new_win = tkinter.Toplevel(self.root)
        self.new_obj = SupportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm","Do you really want to logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python teacher_login.py")

    def exit(self):
        op = messagebox.askyesno("Confirm","Do you really want to exit?", parent=self.root)
        if op == True:
            self.root.destroy()

def main():
    if __name__ == "__main__":
        root_window = tkinter.Tk()
        obj = CollegeDashboard(root_window)
        root_window.mainloop()

        sys.exit(0)
main()