"""
@author: Shubham Pisal
@goal: To build a report page.
"""

import sys
import tkinter 
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class ReportClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1240x480+30+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = tkinter.Label(self.root, text="View Student Result",font=("goudy old style",20,"bold"),bg="lightgrey", fg="black")
        title.place(x=10, y=15, width=1218, height=36)

        # label
        lbl_search_roll = tkinter.Label(self.root, text="Roll Number", font=("goudy old style",18,'bold'),bg='white')
        lbl_search_roll.place(x=400, y=95)
        lbl_search_m_name = tkinter.Label(self.root, text="Mother Name", font=("goudy old style",18,'bold'),bg='white')
        lbl_search_m_name.place(x=400, y=145)
        
        # entrybox
        self.var_search_roll = tkinter.StringVar()
        self.var_search_m_name = tkinter.StringVar()
        self.var_id = ""

        txt_search_roll = tkinter.Entry(self.root)
        txt_search_roll.configure(textvariable=self.var_search_roll, font=("goudy old style",15),bg='lightyellow')
        txt_search_roll.place(x=570, y=100, width=150)
        txt_search_m_name = tkinter.Entry(self.root)
        txt_search_m_name.configure(textvariable=self.var_search_m_name, font=("goudy old style",15),bg='lightyellow')
        txt_search_m_name.place(x=570, y=150, width=150)

        #buttons
        self.search_btn = tkinter.Button(self.root, text="Search", font=("times new roman",12,"bold"),bg="#03a9f4",activebackground="white", fg="white",cursor="hand2", command=self.search_result)
        self.search_btn.place(x=740, y=125, width=100, height=30)
        self.clear_btn = tkinter.Button(self.root, text="Clear", font=("times new roman",12,"bold"),bg="#03a9f4",activebackground="white", fg="white",cursor="hand2", command=self.clear)
        self.clear_btn.place(x=850, y=125, width=100, height=30)
        self.delete_btn = tkinter.Button(self.root, text="Delete", font=("times new roman",12,"bold"),bg="red",activebackground="red", fg="white",cursor="hand2", command=self.delete_result)
        self.delete_btn.place(x=550, y=350, width=150, height=35)

        # labels for report table
        lbl_roll = tkinter.Label(self.root, text="Roll No.", font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        lbl_roll.place(x=30, y=230, width=150, height=50)
        lbl_name = tkinter.Label(self.root, text="Name", font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        lbl_name.place(x=180, y=230, width=150, height=50)
        lbl_course = tkinter.Label(self.root, text="Course", font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        lbl_course.place(x=330, y=230, width=150, height=50)
        lbl_branch = tkinter.Label(self.root, text="Branch", font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        lbl_branch.place(x=480, y=230, width=150, height=50)
        lbl_m_name = tkinter.Label(self.root, text="Mother Name", font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        lbl_m_name.place(x=630, y=230, width=150, height=50)
        lbl_marks = tkinter.Label(self.root, text="Marks Obtained", font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        lbl_marks.place(x=780, y=230, width=150, height=50)
        lbl_full_marks = tkinter.Label(self.root, text="Total Marks", font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        lbl_full_marks.place(x=930, y=230, width=150, height=50)
        lbl_per = tkinter.Label(self.root, text="Percentage", font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        lbl_per.place(x=1080, y=230, width=150, height=50)

        self.roll = tkinter.Label(self.root, font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        self.roll.place(x=30, y=280, width=150, height=50)
        self.name = tkinter.Label(self.root, font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        self.name.place(x=180, y=280, width=150, height=50)
        self.course = tkinter.Label(self.root, font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        self.course.place(x=330, y=280, width=150, height=50)
        self.branch = tkinter.Label(self.root, font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        self.branch.place(x=480, y=280, width=150, height=50)
        self.m_name = tkinter.Label(self.root, font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        self.m_name.place(x=630, y=280, width=150, height=50)
        self.marks = tkinter.Label(self.root, font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        self.marks.place(x=780, y=280, width=150, height=50)
        self.full_marks = tkinter.Label(self.root, font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        self.full_marks.place(x=930, y=280, width=150, height=50)
        self.per = tkinter.Label(self.root, font=("goudy old style",15,'bold'),bg='white', bd=2, relief=tkinter.GROOVE)
        self.per.place(x=1080, y=280, width=150, height=50)

    # search button function
    def search_result(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_search_roll.get() == "" or self.var_search_m_name.get() == "":
                messagebox.showerror("Warning","Roll Number and Mother Name should be required", parent=self.root)

            else:
                cur.execute(f"select * from result_db where roll=? and m_name=?", (self.var_search_roll.get(), self.var_search_m_name.get(),))
                row = cur.fetchone()
                if row != None:
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.branch.config(text=row[4])
                    self.m_name.config(text=row[5])
                    self.marks.config(text=row[6])
                    self.full_marks.config(text=row[7])
                    self.per.config(text=row[8])

                else:
                    messagebox.showerror("Warning!","No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.branch.config(text="")
        self.m_name.config(text="")
        self.marks.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")
        self.var_search_roll.set("")
        self.var_search_m_name.set("")

    def delete_result(self):

        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_id == "":
                messagebox.showerror("Warning","Please search student result first",parent=self.root)
            
            else:
                cur.execute("select * from result_db where rid=?", (self.var_id,))
                row = cur.fetchone()
              
                if row == None:
                    messagebox.showerror("Warning","Invalid Student Result",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from result_db where rid=?", (self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



def main():
    if __name__ == "__main__":
        root_window = tkinter.Tk()
        obj = ReportClass(root_window)
        root_window.mainloop()

        sys.exit(0)
main()