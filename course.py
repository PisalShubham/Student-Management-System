"""
@author: Shubham Pisal
@goal: To build a course page window for teachers login.
"""

import sys
import tkinter
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class CourseClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+60+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = tkinter.Label(self.root, text="Manage Course Details",font=("goudy old style",20,"bold"),bg="lightgrey", fg="black")
        title.place(x=10, y=15, width=1180, height=36)

        # defining variables
        self.var_course = tkinter.StringVar()
        self.var_branch = tkinter.StringVar()
        self.var_duration = tkinter.StringVar()
        self.var_fees = tkinter.StringVar()

        #labels
        lbl_course_name = tkinter.Label(self.root, text="Course Name", font=("goudy old style",15,'bold'),bg='white')
        lbl_course_name.place(x=10, y=60)
        lbl_branch_name = tkinter.Label(self.root, text="Branch Name", font=("goudy old style",15,'bold'),bg='white')
        lbl_branch_name.place(x=10, y=100)
        lbl_duration = tkinter.Label(self.root, text="Duration", font=("goudy old style",15,'bold'),bg='white')
        lbl_duration.place(x=10, y=140)
        lbl_fees = tkinter.Label(self.root, text="Total Fees", font=("goudy old style",15,'bold'),bg='white')
        lbl_fees.place(x=10, y=180)

        #textboxes
        self.txt_course_name = tkinter.Entry(self.root)
        self.txt_course_name.configure(textvariable=self.var_course, font=("goudy old style",12),bg='lightyellow')
        self.txt_course_name.place(x=200, y=60)
        self.txt_branch_name = tkinter.Entry(self.root)
        self.txt_branch_name.configure(textvariable=self.var_branch, font=("goudy old style",12),bg='lightyellow')
        self.txt_branch_name.place(x=200, y=100)
        txt_duration = tkinter.Entry(self.root)
        txt_duration.configure(textvariable=self.var_duration, font=("goudy old style",12),bg='lightyellow')
        txt_duration.place(x=200, y=140)
        txt_fees = tkinter.Entry(self.root)
        txt_fees.configure(textvariable=self.var_fees, font=("goudy old style",12),bg='lightyellow')
        txt_fees.place(x=200, y=180)

        #buttons
        self.add_btn = tkinter.Button(self.root, text="Save", font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2", command=self.add)
        self.add_btn.place(x=150, y=400, width=110, height=40)
        self.update_btn = tkinter.Button(self.root, text="Update", font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.update_details)
        self.update_btn.place(x=270, y=400, width=110, height=40)
        self.delete_btn = tkinter.Button(self.root, text="Delete", font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.delete_course)
        self.delete_btn.place(x=390, y=400, width=110, height=40)
        self.clear_btn = tkinter.Button(self.root, text="Clear", font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2", command=self.clear_details)
        self.clear_btn.place(x=510, y=400, width=110, height=40)

    # search by course name console
        self.var_search = tkinter.StringVar()
        lbl_search_course = tkinter.Label(self.root,text="Course Name",font=("goudy old style",15,'bold'),bg='white')
        lbl_search_course.place(x=720, y=60)
        txt_search_course = tkinter.Entry(self.root)
        txt_search_course.configure(textvariable=self.var_search, font=("goudy old style",12),bg='lightyellow')
        txt_search_course.place(x=870, y=60, width=180)
        self.search_btn = tkinter.Button(self.root, text="Search", font=("times new roman",12,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search_course)
        self.search_btn.place(x=1070, y=60, width=120, height=28)

        self.c_frame = tkinter.Frame(self.root, bd=2, relief=tkinter.RIDGE)
        self.c_frame.place(x=720, y=100, width=470, height=340)
        
        #construct table and scroll bar
        scrolly = tkinter.Scrollbar(self.c_frame,orient=tkinter.VERTICAL)
        scrollx = tkinter.Scrollbar(self.c_frame,orient=tkinter.HORIZONTAL)
        self.course_table = ttk.Treeview(self.c_frame, columns=("cid","course_name","branch_name","duration","fees"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=tkinter.BOTTOM,fill=tkinter.X)
        scrolly.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)

        # construct table columns
        self.course_table.heading("cid", text="Course ID")
        self.course_table.heading("course_name", text="Course Name")
        self.course_table.heading("branch_name", text="Branch Name")
        self.course_table.heading("duration", text="Duration")
        self.course_table.heading("fees", text="Fees")
        self.course_table["show"]='headings'
        self.course_table.column("cid", width=70)
        self.course_table.column("course_name", width=100)
        self.course_table.column("branch_name", width=180)
        self.course_table.column("duration", width=100)
        self.course_table.column("fees", width=100)

        self.course_table.pack(fill=tkinter.BOTH,expand=1)

    #shows data when click on table
        self.course_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def get_data(self, ev):
        self.txt_course_name
        r = self.course_table.focus()
        content = self.course_table.item(r)
        row = content["values"]
        #print(row)
        self.var_course.set(row[1])
        self.var_branch.set(row[2])
        self.var_duration.set(row[3])
        self.var_fees.set(row[4])

    # Save(add_btn) button function
    def add(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_course.get()=="" or self.var_branch.get()=="" or self.var_duration.get()=="" or self.var_fees.get()=="":
                messagebox.showerror("Warning","Please fill all the required information",parent=self.root)
            
            else:
                cur.execute("select * from course where course_name=?", (self.var_course.get(),))
                row = cur.fetchone()
              
                if row != None:
                    messagebox.showerror("Warning","Course name already present",parent=self.root)
                else:
                    cur.execute("insert into course (course_name, branch_name, duration, fees) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_branch.get(),
                        self.var_duration.get(),
                        self.var_fees.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    # Update button function
    def update_details(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_course.get()=="" or self.var_branch.get()=="" or self.var_duration.get()=="" or self.var_fees.get()=="":
                messagebox.showerror("Warning","Please fill all the required information",parent=self.root)
            
            else:
                cur.execute("select * from course where course_name=?", (self.var_course.get(),))
                row = cur.fetchone()
              
                if row == None:
                    messagebox.showerror("Warning","Select course from list",parent=self.root)
                else:
                    cur.execute("update course set branch_name=?, duration=?, fees=? where course_name=?",(
                        self.var_branch.get(),
                        self.var_duration.get(),
                        self.var_fees.get(),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course update Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute("select * from course")
            rows = cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',tkinter.END, values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search_course(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute(f"select * from course where course_name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',tkinter.END, values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    # clear button function
    def clear_details(self):
        self.show()
        self.var_course.set("")
        self.var_branch.set("")
        self.var_duration.set("")
        self.var_fees.set("")
        self.var_search.set("")
        self.txt_course_name.config(state=tkinter.NORMAL)

    # delete button function

    def delete_course(self):

        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_course.get()=="":
                messagebox.showerror("Warning","Course name should be required",parent=self.root)
            
            else:
                cur.execute("select * from course where course_name=?", (self.var_course.get(),))
                row = cur.fetchone()
              
                if row == None:
                    messagebox.showerror("Warning","Please select course from list first",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from course where course_name=?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted successfully", parent=self.root)
                        self.clear_details()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

def main():
    if __name__ == "__main__":
        root_window = tkinter.Tk()
        obj = CourseClass(root_window)
        root_window.mainloop()

        sys.exit(0)
main()