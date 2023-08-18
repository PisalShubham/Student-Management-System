"""
@author: Shubham Pisal
@goal: To build a support page for teachers 
        which contains the regestration data of students.
"""

import sys
import tkinter
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class SupportClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x530+80+120")
        self.root.config(bg="white")
        self.root.focus_force()

        #defining variables

        self.var_fname = tkinter.StringVar()
        self.var_lname = tkinter.StringVar()
        self.var_roll = tkinter.StringVar()
        self.var_contact = tkinter.StringVar()
        self.var_email = tkinter.StringVar()


        self.var_search = tkinter.StringVar()
        lbl_search_prn = tkinter.Label(self.root,text="Roll Number",font=("goudy old style",15,'bold'),bg='white')
        lbl_search_prn.place(x=0, y=3)
        txt_search_prn = tkinter.Entry(self.root)
        txt_search_prn.configure(textvariable=self.var_search, font=("goudy old style",12),bg='lightyellow')
        txt_search_prn.place(x=130, y=7, width=180)
        self.search_btn = tkinter.Button(self.root, text="Search", font=("times new roman",12,"bold"),command=self.search, bg="#03a9f4",fg="white",cursor="hand2")
        self.search_btn.place(x=330, y=7, width=100, height=28)
        self.clear_btn = tkinter.Button(self.root, text="Clear", font=("times new roman",12,"bold"),command=self.clear, bg="#03a9f4",fg="white",cursor="hand2")
        self.clear_btn.place(x=450, y=7, width=100, height=28)

        self.c_frame = tkinter.Frame(self.root, bd=2, relief=tkinter.RIDGE)
        self.c_frame.place(x=0, y=50, width=600, height=477)
        
        #construct table and scroll bar
        scrolly = tkinter.Scrollbar(self.c_frame,orient=tkinter.VERTICAL)
        scrollx = tkinter.Scrollbar(self.c_frame,orient=tkinter.HORIZONTAL)
        self.student_details_table = ttk.Treeview(self.c_frame, columns=("fname","lname","roll","contact","email","pass"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=tkinter.BOTTOM,fill=tkinter.X)
        scrolly.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        scrollx.config(command=self.student_details_table.xview)
        scrolly.config(command=self.student_details_table.yview)

        # construct table columns
        #self.student_details_table.heading("prn", text="PRN No.")
        
        self.student_details_table.heading("fname", text=" First Name")
        self.student_details_table.heading("lname", text="Last Name")
        self.student_details_table.heading("roll", text="Roll No.")        
        self.student_details_table.heading("contact", text="Contact No.") 
        self.student_details_table.heading("email", text="Username") 
        self.student_details_table.heading("pass", text="Password") 

        self.student_details_table["show"]='headings'

        #self.student_details_table.column("prn", width=100)
        self.student_details_table.column("fname", width=100)
        self.student_details_table.column("lname", width=100)
        self.student_details_table.column("roll", width=100)        
        self.student_details_table.column("contact", width=100) 
        self.student_details_table.column("email", width=100)
        self.student_details_table.column("pass", width=100)
        
        self.student_details_table.pack(fill=tkinter.BOTH,expand=1)

        self.show()



    def show(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute("select * from student_login_db")
            rows = cur.fetchall()
            self.student_details_table.delete(*self.student_details_table.get_children())
            for row in rows:
                self.student_details_table.insert('',tkinter.END, values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute(f"select * from student_login_db where roll=?", (self.var_search.get(),))
            row = cur.fetchone()
            if row != None:
                self.student_details_table.delete(*self.student_details_table.get_children())
                self.student_details_table.insert('',tkinter.END, values=row)

            else:
                messagebox.showerror("Warning!","No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_search.set("")
        self.show()

def main():
    if __name__ == "__main__":
        root_window = tkinter.Tk()
        obj = SupportClass(root_window)
        root_window.mainloop()

        sys.exit(0)
main()
