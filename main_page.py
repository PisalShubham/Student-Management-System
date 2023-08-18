"""
@author: Shubham Pisal
@goal: To build a main page window.
"""

import sys
import tkinter
import os
from PIL import Image, ImageTk
from teacher_login import TeacherLogin
from student_login import StudentLogin


class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="../img/university.jpg")
        self.bg_image = tkinter.Label(self.root, image=self.bg, bd=0)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        college_btn = tkinter.Button(self.root, text="College", font=("goudy old style",23,"bold"),bd=4, relief=tkinter.RIDGE, command=self.clickon_college, bg="#d77337",fg="black",cursor="hand2")
        college_btn.place(x=50, y=20, width=130, height=40)
        student_btn = tkinter.Button(self.root, text="Student", font=("goudy old style",23,"bold"),bd=4, relief=tkinter.RIDGE, command=self.clickon_student, bg="#d77337",fg="black",cursor="hand2")
        student_btn.place(x=220, y=20, width=130, height=40)

    def clickon_college(self):
        self.root.destroy()
        os.system("python teacher_login.py")

    def clickon_student(self):
        self.root.destroy()
        os.system("python student_login.py")

def main():
    if __name__ == "__main__":
        root_window = tkinter.Tk()
        obj = MainPage(root_window)
        root_window.mainloop()

    sys.exit(0)
main()