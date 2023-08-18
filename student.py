"""
@author: Shubham Pisal
@goal: To build a course page window for teachers login.
"""

import sys
import tkinter
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class StudentClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+60+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = tkinter.Label(self.root, text="Manage Student Details",font=("goudy old style",20,"bold"),bg="lightgrey", fg="black")
        title.place(x=10, y=15, width=1180, height=36)

        # defining variables
        self.var_roll_no = tkinter.StringVar()
        #self.var_prn = tkinter.StringVar()
        self.var_name = tkinter.StringVar()
        self.var_email = tkinter.StringVar()
        self.var_gender = tkinter.StringVar()
        self.var_m_name = tkinter.StringVar()
        self.var_dob = tkinter.StringVar()
        self.var_contact = tkinter.StringVar()
        self.var_course = tkinter.StringVar()
        self.var_branch = tkinter.StringVar()
        self.var_a_date = tkinter.StringVar()
        self.var_state = tkinter.StringVar()
        self.var_city = tkinter.StringVar()
        self.var_pin = tkinter.StringVar()

        #labels
        # LHS column
        lbl_roll_no = tkinter.Label(self.root, text="Roll No.", font=("goudy old style",15,'bold'),bg='white')
        lbl_roll_no.place(x=5, y=60)
        lbl_name = tkinter.Label(self.root, text="Full Name", font=("goudy old style",15,'bold'),bg='white')
        lbl_name.place(x=5, y=100)
        lbl_Email = tkinter.Label(self.root, text="Email", font=("goudy old style",15,'bold'),bg='white')
        lbl_Email.place(x=5, y=140)
        lbl_m_name = tkinter.Label(self.root, text="Mother Name", font=("goudy old style",15,'bold'),bg='white')
        lbl_m_name.place(x=5, y=180)
        lbl_gender = tkinter.Label(self.root, text="Gender", font=("goudy old style",15,'bold'),bg='white')
        lbl_gender.place(x=5, y=220)

        lbl_address = tkinter.Label(self.root, text="Address", font=("goudy old style",15,'bold'),bg='white')
        lbl_address.place(x=5, y=300)

        # LHS textboxes
        self.txt_roll_no = tkinter.Entry(self.root)
        self.txt_roll_no.configure(textvariable=self.var_roll_no, font=("goudy old style",12),bg='lightyellow')
        self.txt_roll_no.place(x=170, y=60)
        self.txt_name = tkinter.Entry(self.root)
        self.txt_name.configure(textvariable=self.var_name, font=("goudy old style",12),bg='lightyellow')
        self.txt_name.place(x=170, y=100,)
        txt_email = tkinter.Entry(self.root)
        txt_email.configure(textvariable=self.var_email, font=("goudy old style",12),bg='lightyellow')
        txt_email.place(x=170, y=140)
        self.txt_m_name = tkinter.Entry(self.root)
        self.txt_m_name.configure(textvariable=self.var_m_name, font=("goudy old style",12),bg='lightyellow')
        self.txt_m_name.place(x=170, y=180)
        self.txt_gender = ttk.Combobox(self.root)
        self.txt_gender.configure(textvariable=self.var_gender,values=("Select","Male","Female","Other"), font=("goudy old style",12),state='readonly', justify=tkinter.CENTER)
        self.txt_gender.place(x=170, y=220, width=165)
        self.txt_gender.current(0)

        self.txt_address = tkinter.Text(self.root)
        self.txt_address.configure(font=("goudy old style",12),bg='lightyellow')
        self.txt_address.place(x=170, y=300, width=530, height=80)

         # RHS column
        lbl_dob = tkinter.Label(self.root, text="D.O.B(dd/mm/yyyy)", font=("goudy old style",15,'bold'),bg='white')
        lbl_dob.place(x=360, y=60)
        lbl_contact = tkinter.Label(self.root, text="Contact No.", font=("goudy old style",15,'bold'),bg='white')
        lbl_contact.place(x=360, y=100)
        lbl_course = tkinter.Label(self.root, text="Course", font=("goudy old style",15,'bold'),bg='white')
        lbl_course.place(x=360, y=140)
        lbl_branch = tkinter.Label(self.root, text="Branch", font=("goudy old style",15,'bold'),bg='white')
        lbl_branch.place(x=360, y=180)
        lbl_admission = tkinter.Label(self.root, text="Admission Date", font=("goudy old style",15,'bold'),bg='white')
        lbl_admission.place(x=360, y=220)
        
        # RHS textboxes
        self.course_list = []
        self.fetch_course()
        self.branch_list = []
        self.fetch_branch()

        self.dob = tkinter.Entry(self.root)
        self.dob.configure(textvariable=self.var_dob, font=("goudy old style",12),bg='lightyellow')
        self.dob.place(x=550, y=60, width=150)
        self.contact = tkinter.Entry(self.root)
        self.contact.configure(textvariable=self.var_contact, font=("goudy old style",12),bg='lightyellow')
        self.contact.place(x=550, y=100, width=150)
        self.txt_course = ttk.Combobox(self.root)
        self.txt_course.configure(textvariable=self.var_course,values=self.course_list, font=("goudy old style",12),state='readonly', justify=tkinter.CENTER)
        self.txt_course.place(x=550, y=140, width=150)
        self.txt_course.set("Select")
        self.txt_branch = ttk.Combobox(self.root)
        self.txt_branch.configure(textvariable=self.var_branch,values=self.branch_list, font=("goudy old style",12),state='readonly', justify=tkinter.CENTER)
        self.txt_branch.place(x=550, y=180, width=150)
        self.txt_branch.set("Select")
        txt_admission = tkinter.Entry(self.root)
        txt_admission.configure(textvariable=self.var_a_date, font=("goudy old style",12),bg='lightyellow')
        txt_admission.place(x=550, y=220, width=150)

        # center labels and textboxes

        lbl_state = tkinter.Label(self.root, text="State", font=("goudy old style",15,'bold'),bg='white')
        lbl_state.place(x=5, y=260)
        self.txt_state = tkinter.Entry(self.root)
        self.txt_state.configure(textvariable=self.var_state, font=("goudy old style",12),bg='lightyellow')
        self.txt_state.place(x=100, y=260, width=150)

        lbl_city = tkinter.Label(self.root, text="City", font=("goudy old style",15,'bold'),bg='white')
        lbl_city.place(x=265, y=260)
        self.txt_city = tkinter.Entry(self.root)
        self.txt_city.configure(textvariable=self.var_city, font=("goudy old style",12),bg='lightyellow')
        self.txt_city.place(x=320, y=260, width=140)

        lbl_pin = tkinter.Label(self.root, text="Pin Code", font=("goudy old style",15,'bold'),bg='white')
        lbl_pin.place(x=470, y=260)
        self.txt_pin = tkinter.Entry(self.root)
        self.txt_pin.configure(textvariable=self.var_pin, font=("goudy old style",12),bg='lightyellow')
        self.txt_pin.place(x=560, y=260, width=140)

        #buttons
        self.add_btn = tkinter.Button(self.root, text="Save", font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2", command=self.add)
        self.add_btn.place(x=150, y=420, width=110, height=40)
        self.update_btn = tkinter.Button(self.root, text="Update", font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.update_details)
        self.update_btn.place(x=270, y=420, width=110, height=40)
        self.delete_btn = tkinter.Button(self.root, text="Delete", font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.delete_course)
        self.delete_btn.place(x=390, y=420, width=110, height=40)
        self.clear_btn = tkinter.Button(self.root, text="Clear", font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2", command=self.clear_details)
        self.clear_btn.place(x=510, y=420, width=110, height=40)

    # search by Roll number panel
        self.var_search = tkinter.StringVar()
        lbl_search_prn = tkinter.Label(self.root,text="Roll Number",font=("goudy old style",15,'bold'),bg='white')
        lbl_search_prn.place(x=720, y=60)
        txt_search_prn = tkinter.Entry(self.root)
        txt_search_prn.configure(textvariable=self.var_search, font=("goudy old style",12),bg='lightyellow')
        txt_search_prn.place(x=870, y=60, width=180)
        self.search_btn = tkinter.Button(self.root, text="Search", font=("times new roman",12,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search_student)
        self.search_btn.place(x=1070, y=60, width=120, height=28)

        self.c_frame = tkinter.Frame(self.root, bd=2, relief=tkinter.RIDGE)
        self.c_frame.place(x=720, y=100, width=470, height=340)
        
        #construct table and scroll bar
        scrolly = tkinter.Scrollbar(self.c_frame,orient=tkinter.VERTICAL)
        scrollx = tkinter.Scrollbar(self.c_frame,orient=tkinter.HORIZONTAL)
        self.student_details_table = ttk.Treeview(self.c_frame, columns=("roll","name","email","gender", "m_name","dob","contact","course","branch","a_date","state","city","pin","addr"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=tkinter.BOTTOM,fill=tkinter.X)
        scrolly.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        scrollx.config(command=self.student_details_table.xview)
        scrolly.config(command=self.student_details_table.yview)

        # construct table columns
        #self.student_details_table.heading("prn", text="PRN No.")
        self.student_details_table.heading("roll", text="Roll No.")
        self.student_details_table.heading("name", text="Name")
        self.student_details_table.heading("email", text="Email")
        self.student_details_table.heading("gender", text="Gender")
        self.student_details_table.heading("m_name", text="Mother's Name")
        self.student_details_table.heading("dob", text="Date of Birth")
        self.student_details_table.heading("contact", text="Contact No.")   
        self.student_details_table.heading("course", text="Course")
        self.student_details_table.heading("branch", text="Branch")
        self.student_details_table.heading("a_date", text="Admission Date")
        self.student_details_table.heading("state", text="State")
        self.student_details_table.heading("city", text="City")
        self.student_details_table.heading("pin", text="Pin Code")
        self.student_details_table.heading("addr", text="Address")
        self.student_details_table["show"]='headings'

        #self.student_details_table.column("prn", width=100)
        self.student_details_table.column("roll", width=100)
        self.student_details_table.column("name", width=160)
        self.student_details_table.column("email", width=100)
        self.student_details_table.column("gender", width=70)
        self.student_details_table.column("m_name", width=100)
        self.student_details_table.column("dob", width=100)
        self.student_details_table.column("contact", width=100)
        self.student_details_table.column("course", width=100)
        self.student_details_table.column("branch", width=150)
        self.student_details_table.column("a_date", width=110)
        self.student_details_table.column("state", width=100)
        self.student_details_table.column("city", width=100)
        self.student_details_table.column("pin", width=100)
        self.student_details_table.column("addr", width=200)

        self.student_details_table.pack(fill=tkinter.BOTH,expand=1)

    #shows data when click on table
        self.student_details_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def get_data(self, ev):
        self.txt_roll_no.config(state='readonly')
        self.txt_roll_no
        r = self.student_details_table.focus()
        content = self.student_details_table.item(r)
        row = content["values"]
        
        self.var_roll_no.set(row[0]),
        #self.var_prn.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_m_name.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_contact.set(row[6]),
        self.var_course.set(row[8]),
        self.var_branch.set(row[9]),
        self.var_a_date.set(row[7]),
        self.var_state.set(row[10]),
        self.var_city.set(row[11]),
        self.var_pin.set(row[12]),
        self.txt_address.delete("1.0", tkinter.END)
        self.txt_address.insert(tkinter.END,row[13])
        

    # Save(add_btn) button function
    def add(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()
        if self.var_roll_no.get()=="":
            print("Error")



        try:
            if self.var_roll_no.get()=="" or self.var_name.get() == "" or self.var_email.get() == "" or self.var_m_name.get() == "" or self.var_dob.get() == "" or self.var_contact.get() == "" or self.var_gender.get() == "Select":
                messagebox.showerror("Warning","Please fill all the required information",parent=self.root)

            elif self.var_a_date.get() == "" or self.var_state.get() == "" or self.var_city.get() == "" or self.var_pin.get() == "" or self.txt_address.get("1.0") == "" or self.var_contact.get() == "Select" or self.var_branch.get() == "Select":
                messagebox.showerror("Warning","Please fill all the required information",parent=self.root)

            else:
                cur.execute("select * from student_db where roll=?", (self.var_roll_no.get(),))
                row = cur.fetchone()
              
                if row != None:
                    messagebox.showerror("Warning","Roll number already present", parent=self.root)
                else:
                    cur.execute("insert into student_db(roll, name, email, gender, m_name, dob, contact, course, branch, a_date, state, city, pin, addr) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll_no.get(),
                        #self.var_prn.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_m_name.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_course.get(),
                        self.var_branch.get(),
                        self.var_a_date.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", tkinter.END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    # Update button function
    def update_details(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_roll_no.get()=="" or self.var_name.get() == "" or self.var_email.get() == "" or self.var_m_name.get() == "" or self.var_dob.get() == "" or self.var_contact.get() == "" or self.var_gender.get() == "Select":
                messagebox.showerror("Warning","Please fill all the required information",parent=self.root)

            elif self.var_a_date.get() == "" or self.var_state.get() == "" or self.var_city.get() == "" or self.var_pin.get() == "" or self.txt_address.get("1.0") == "" or self.var_contact.get() == "Select" or self.var_branch.get() == "Select":
                messagebox.showerror("Warning","Please fill all the required information",parent=self.root)
            
            else:
                cur.execute("select * from student_db where roll=?", (self.var_roll_no.get(),))
                row = cur.fetchone()
              
                if row == None:
                    messagebox.showerror("Warning","Select student_db from list",parent=self.root)
                else:
                    cur.execute("update student_db set name=?, email=?, gender=?, m_name=?, dob=?, contact=?, course=?, branch=?, a_date=?, state=?, city=?, pin=?, addr=? where roll=?",(
                        
                        #self.var_prn.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_m_name.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_course.get(),
                        self.var_branch.get(),
                        self.var_a_date.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", tkinter.END),
                        self.var_roll_no.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student update Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute("select * from student_db")
            rows = cur.fetchall()
            self.student_details_table.delete(*self.student_details_table.get_children())
            for row in rows:
                self.student_details_table.insert('',tkinter.END, values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def fetch_course(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute("select course_name from course")
            rows = cur.fetchall()

            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def fetch_branch(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute("select branch_name from course")
            rows = cur.fetchall()

            if len(rows) > 0:
                for row in rows:
                    self.branch_list.append(row[0])
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def search_student(self):
        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            cur.execute(f"select * from student_db where roll=?", (self.var_search.get(),))
            row = cur.fetchone()
            if row != None:
                self.student_details_table.delete(*self.student_details_table.get_children())
                self.student_details_table.insert('',tkinter.END, values=row)

            else:
                messagebox.showerror("Warning!","No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    # clear button function
    def clear_details(self):
        self.show()
        self.var_roll_no.set(""),
        #self.var_prn.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_m_name.set(""),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_course.set("Select"),
        self.var_branch.set("Select"),
        self.var_a_date.set(""),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0", tkinter.END)
        self.txt_roll_no.config(state=tkinter.NORMAL)
        self.var_search.set("")

    # delete button function

    def delete_course(self):

        con = sqlite3.connect(database="collage.db")
        cur = con.cursor()

        try:
            if self.var_roll_no.get()=="":
                messagebox.showerror("Warning","Roll number should be required",parent=self.root)
            
            else:
                cur.execute("select * from student_db where roll=?", (self.var_roll_no.get(),))
                row = cur.fetchone()
              
                if row == None:
                    messagebox.showerror("Warning","Please select student from list first",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from student_db where roll=?", (self.var_roll_no.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted successfully", parent=self.root)
                        self.clear_details()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

def main():
    if __name__ == "__main__":
        root_window = tkinter.Tk()
        obj = StudentClass(root_window)
        root_window.mainloop()

        sys.exit(0)
main()