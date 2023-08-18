"""
@author: Shubham Pisal
@goal: Create a database for collage use
"""

import sqlite3

def create_db():
    con = sqlite3.connect(database="collage.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, course_name text, branch_name text, duration text, fees INTEGER)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student_db(roll INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, m_name text, dob text, contact text, course text, branch text, a_date text, state text, city text, pin text, addr text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result_db(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text, name text, course text, branch text, m_name text, marks_ob INTEGER, full_marks INTEGER, per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student_login_db(fname text, lname text, roll text, contact INTEGER, email text, pass)")
    con.commit()


    con.close()

create_db()