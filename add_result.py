"""
@author: Shubham Pisal
@goal: To build a add student result page.
"""

import sys
import tkinter
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class ResultClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x530+80+120")
        self.root.config(bg="white")
        self.root.focus_force()

        title = tkinter.Label(self.root, text="Add Student Result",font=("goudy old style",20,"bold"),bg="lightgrey", fg="black")
        title.place(x=10, y=15, width=577, height=50)

        # defining variables
        self.var_roll_no = tkinter.StringVar()
        self.var_name = tkinter.StringVar()
        self.var_course = tkinter.StringVar()
        self.var_branch = tkinter.StringVar()
        self.var_m_name = tkinter.StringVar()
        self.var_marks = tkinter.StringVar()
        self.var_full_marks = tkinter.StringVar()

        # labels
        lbl_student = tkinter.Label(self.root, text="Roll Numbar", font=("goudy old style",15,'bold'),bg='white')
        lbl_student.place(x=40, y=100)
        lbl_name = tkinter.Label(self.root, text="Name", font=("goudy old style",15,'bold'),bg='white')
        lbl_name.place(x=40, y=150)
        lbl_course = tkinter.Label(self.root, text="Course", font=("goudy old style",15,'bold'),bg='white')
        lbl_course.place(x=40, y=200)
        lbl_branch = tkinter.Label(self.root, text="Branch", font=("goudy old style",15,'bold'),bg='white')
        lbl_branch.place(x=40, y=250)
        lbl_m_name = tkinter.Label(self.root, text="Mother Name", font=("goudy old style",15,'bold'),bg='white')
        lbl_m_name.place(x=40, y=300)
        lbl_marks = tkinter.Label(self.root, text="Marks Obtained", font=("goudy old style",15,'bold'),bg='white')
        lbl_marks.place(x=40, y=350)
        lbl_total_marks = tkinter.Label(self.root, text="Full Marks", font=("goudy old style",15,'bold'),bg='white')
        lbl_total_marks.place(x=40, y=400)

        # Entries

        self.txt_student = tkinter.Entry(self.root)
        self.txt_student.configure(textvariable=self.var_roll_no, font=("goudy old style",12),bg='white')
        self.txt_student.place(x=280, y=100, width=160)

        self.search_btn = tkinter.Button(self.root, text="Search", font=("times new roman",12,"bold"),bg="green",activebackground="white", fg="white",cursor="hand2", command=self.search_student)
        self.search_btn.place(x=480, y=100, width=100, height=30)

        # entries

        self.txt_name = tkinter.Entry(self.root)
        self.txt_name.configure(textvariable=self.var_name, font=("goudy old style",12),bg='white', state='readonly')
        self.txt_name.place(x=280, y=150, width=300)
        self.txt_course = tkinter.Entry(self.root)
        self.txt_course.configure(textvariable=self.var_course, font=("goudy old style",12),bg='white', state='readonly')
        self.txt_course.place(x=280, y=200, width=300)
        self.txt_branch = tkinter.Entry(self.root)
        self.txt_branch.configure(textvariable=self.var_branch, font=("goudy old style",12),bg='white', state='readonly')
        self.txt_branch.place(x=280, y=250, width=300)
        self.txt_m_name = tkinter.Entry(self.root)
        self.txt_m_name.configure(textvariable=self.var_m_name, font=("goudy old style",12),bg='white', state='readonly')
        self.txt_m_name.place(x=280, y=300, width=300)
        self.txt_marks = tkinter.Entry(self.root)
        self.txt_marks.configure(textvariable=self.var_marks, font=("goudy old style",12),bg='white')
        self.txt_marks.place(x=280, y=350, width=300)
        self.txt_full_marks = tkinter.Entry(self.root)
        self.txt_full_marks.configure(textvariable=self.var_full_marks, font=("goudy old style",12),bg='white')
        self.txt_full_marks.place(x=280, y=400, width=300)

        # buttons
        self.add_btn = tkinter.Button(self.root, text="Submit", font=("times new roman",12,"bold"),bg="lightgray",fg="black", activebackground="lightgray",cursor="hand2", command=self.add)
        self.add_btn.place(x=300, y=470, width=120, height=40)
        self.clear_btn = tkinter.Button(self.root, text="Clear", font=("times new roman",12,"bold"),bg="lightgray",fg="black", activebackground="lightgray",cursor="hand2", command=self.clear)
        self.clear_btn.place(x=430, y=470, width=120, height=40)

    # search button function
    def search_student(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute(f"select name,course,branch,m_name from student_db where roll=?", (self.var_roll_no.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
                self.var_branch.set(row[2])
                self.var_m_name.set(row[3])

            else:
                messagebox.showerror("Warning!","No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    # Submit (add) button function
    def add(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_name.get()=="":
                messagebox.showerror("Warning","Please first search student record by roll number",parent=self.root)
            
            else:
                cur.execute("select * from result_db where roll=? and course=? and branch=?", (self.var_roll_no.get(), self.var_course.get(), self.var_branch.get()))
                row = cur.fetchone()
              
                if row != None:
                    messagebox.showerror("Warning","Result already added",parent=self.root)
                else:
                    per = (int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    per = round(per, 2)
                    cur.execute("insert into result_db (roll, name, course, branch,m_name, marks_ob, full_marks, per) values(?,?,?,?,?,?,?,?)",(
                        self.var_roll_no.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_branch.get(),
                        self.var_m_name.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}", parent=self.root)

    def clear(self):
        self.var_roll_no.set(""),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_branch.set(""),
        self.var_m_name.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set("")

def main():
    if __name__ == "__main__":
        root_window = tkinter.Tk()
        obj = ResultClass(root_window)
        root_window.mainloop()

        sys.exit(0)
main()