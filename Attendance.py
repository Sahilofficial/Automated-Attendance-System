#!/usr/bin/env python
# coding:utf-8
"""
Name : Attendance.py
Author : Sahil Kumar
Email : sahilofficial74@gmail.com
Time    : 7/11/2021 7:44 PM

"""


from tkinter import *
from tkinter import ttk, filedialog, messagebox
from time import strftime
import datetime as dt
import mysql.connector
import cv2
import os
import csv



my_data=[]
class Attendance:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1370x750")
        self.master.configure(background="dark slate gray")
        self.master.title("Attendance Management System")
        self.master.iconbitmap(r"F:\Attendance_sys\v2\icon.ico")

        # Text Variables
        self.u_Id_var = StringVar()
        self.name_var = StringVar()
        self.roll_no_var = StringVar()
        self.course_var = StringVar()
        self.time_var = StringVar()
        self.date_var = StringVar()
        self.att_status_var = StringVar()


        # main frame
        frame = Frame(self.master, bd=2, bg="dark slate gray")
        frame.place(x=0, y=0, width=1370, height=750)

    # Heading "Student Management System"
        heading = Label(frame, text="Attendance Management System", font=("Helvetica", 34, "bold", "underline"), fg="aquamarine2", bg = "dark slate gray" )
        heading.grid(row=0, column=2, padx=370, pady=10, sticky=NW)

    # make two frames in main frame
        left_frame = LabelFrame(frame, text="Student Attendance Details",font=("Times Roman", 15, "bold", "italic", "underline"), relief=RIDGE, bg="dark slate gray", fg="aquamarine2")
        left_frame.place(x=0, y=100, width=685, height=620)

        right_frame = LabelFrame(frame, text="Student Attendance Details", font=("Times Roman", 15, "bold", "italic", "underline"), relief=RIDGE, bg="dark slate gray", fg="aquamarine2")
        right_frame.place(x=680, y=100, width=683, height=620)

        left_frame1 = Frame(frame, relief=RIDGE, bg="dark slate gray")
        left_frame1.place(x=2, y=145, width=343, height=310)

        left_frame2 = Frame(frame, relief=RIDGE, bg="dark slate gray")
        left_frame2.place(x=338, y=145, width=342, height=310)

        u_Id_label = Label(left_frame1, text="University_Id", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        u_Id_label.grid(row=0, column=0,padx=5, pady=20, sticky=W)
        u_Id = Entry(left_frame1, width=30, relief=RIDGE, textvariable=self.u_Id_var)
        u_Id.grid(row=0, column=1, padx=5, pady=20, sticky=W)

        name_label = Label(left_frame2, text="Name", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        name_label.grid(row=0, column=0, padx=10, pady=20, sticky=W)
        name = Entry(left_frame2, width=30, relief=RIDGE, textvariable=self.name_var)
        name.grid(row=0, column=1, padx=5, pady=20, sticky=W)

        roll_no_label = Label(left_frame1, text="Roll No.", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        roll_no_label.grid(row=1, column=0, padx=10, pady=20, sticky=W)
        roll_no = Entry(left_frame1, width=30, relief=RIDGE, textvariable=self.roll_no_var)
        roll_no.grid(row=1, column=1, padx=5, pady=20, sticky=W)

        course_label = Label(left_frame2, text="Course", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        course_label.grid(row=1, column=0, padx=10, pady=20, sticky=W)
        course = Entry(left_frame2, width=30, relief=RIDGE, textvariable=self.course_var)
        course.grid(row=1, column=1, padx=5, pady=20, sticky=W)

        time_label = Label(left_frame1, text="Time", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        time_label.grid(row=2, column=0, padx=10, pady=20, sticky=W)
        time = Entry(left_frame1, width=30, relief=RIDGE, textvariable=self.time_var)
        time.grid(row=2, column=1, padx=5, pady=20, sticky=W)

        date_label = Label(left_frame2, text="Date", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        date_label.grid(row=2, column=0, padx=10, pady=20, sticky=W)
        date = Entry(left_frame2, width=30, relief=RIDGE, textvariable=self.date_var)
        date.grid(row=2, column=1, padx=5, pady=20, sticky=W)

        att_status_label = Label(left_frame1, text="Attendance Status", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        att_status_label.grid(row=3, column=0,padx=10, pady=10, sticky=W)
        att_status = ttk.Combobox(left_frame1, width=25, state="readonly", textvariable=self.att_status_var)
        att_status["values"] = ["Status", "Present", "Absent"]
        att_status.current(0)
        att_status.grid(row=3, column=1, padx=5, pady=20, sticky=W)

        left_frame3 = Frame(frame, relief=RIDGE, bg="dark slate gray")
        left_frame3.place(x=1, y=430, width=675, height=200)

        import_csv = Button(left_frame3, text="Import CSV", relief=RIDGE, command=self.imp_csv, width=30, font=("Helvetica", 8, "bold"), bg="light cyan", fg="dark slate gray")
        import_csv.grid(row=0,column=0, padx=5, pady=3)

        export_csv = Button(left_frame3, text="Export CSV", relief=RIDGE, command=self.exp_csv, font=("Helvetica", 8, "bold"), width=30, bg="light cyan", fg="dark slate gray")
        export_csv.grid(row=0,column=1, padx=5, pady=3)

        update = Button(left_frame3, text="Update", relief=RIDGE, font=("Helvetica", 8, "bold"), width=30, bg="light cyan", fg="dark slate gray")
        update.grid(row=0,column=2, padx=5, pady=3)

        reset = Button(left_frame3, text="Reset", relief=RIDGE, font=("Helvetica", 8, "bold"), command=self.resets, width=30, bg="light cyan", fg="dark slate gray")
        reset.grid(row=1,column=0, padx=5, pady=10)

        cancel = Button(left_frame3, text="Cancel", relief=RIDGE, font=("Helvetica", 8, "bold"), command=quit, width=30, bg="light cyan", fg="dark slate gray")
        cancel.grid(row=1,column=1, padx=5, pady=10)
        
        # Right frame
        right_frame1 = Frame(right_frame, relief=RIDGE, bd=2, bg="dark slate gray", highlightcolor="aquamarine2")
        right_frame1.place(x=0, y=3, width=675, height=573)

        scroll_x = ttk.Scrollbar(right_frame1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_frame1, orient=VERTICAL)
        
        self.attendance_tabel = ttk.Treeview(right_frame1,xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.attendance_tabel["column"] = ("u_Id", "course", "name", "roll", "time", "date", "status")

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_tabel.xview)
        scroll_y.config(command=self.attendance_tabel.yview)

        self.attendance_tabel.heading("course", text="Course")
        self.attendance_tabel.heading("u_Id", text="University_Id")
        self.attendance_tabel.heading("name", text="Name")
        self.attendance_tabel.heading("roll", text="Roll No.")
        self.attendance_tabel.heading("time", text="Time")
        self.attendance_tabel.heading("date", text="Date")
        self.attendance_tabel.heading("status", text="Attendance Status")
        
        self.attendance_tabel["show"]='headings'

        self.attendance_tabel.column("course", width=120)
        self.attendance_tabel.column("u_Id", width=120)
        self.attendance_tabel.column("name", width=120)
        self.attendance_tabel.column("roll", width=120)
        self.attendance_tabel.column("time", width=120)
        self.attendance_tabel.column("date", width=120)
        self.attendance_tabel.column("status", width=120)

        self.attendance_tabel.pack(fill=BOTH, expand=1)
        self.attendance_tabel.bind("<ButtonRelease>", self.select_student)




    def resets(self):
        self.u_Id_var.set("")
        self.name_var.set("")
        self.roll_no_var.set("")
        self.course_var.set("")
        self.time_var.set("")
        self.date_var.set("")
        self.att_status_var.set("Status")

    def show_data(self, rows):
        self.attendance_tabel.delete(*self.attendance_tabel.get_children())
        for i in rows:
            self.attendance_tabel.insert("", END, values=i)

    def imp_csv(self):
        global my_data
        my_data.clear()
        file = filedialog.askopenfilename(initialdir=os.getcwd, title="Select file", filetypes=(("CSV files","*csv"),("All files","*.*")), parent=self.master)
        with open(file) as f:
            df = csv.reader(f, delimiter=",")
            for i in df:
                my_data.append(i)
            self.show_data(my_data)

    def exp_csv(self): # create a new file and export all data
        try:
            if len(my_data)<1:
                messagebox.showerror("Error","No data found to export", parent=self.master)
                return False
            file = filedialog.asksaveasfilename(initialdir=os.getcwd, title="Select file", filetypes=(("CSV files","*csv"),("All files","*.*")), parent=self.master)
            with open(file, mode="w", newline="") as f:
                df = csv.writer(f, delimiter=",")
                for i in my_data:
                    df.writerow(i)
                messagebox.showinfo("Info", "Data successfully export to " + os.path.basename(file))

        except Exception as e:
                messagebox.showerror("Error", f"{str(e)}", parent=self.master)

                    





    def select_student(self, event=""): # click Students details in table and all details of selected student will be filled in entries in Students Profile section 
        clk = self.attendance_tabel.focus()
        content = self.attendance_tabel.item(clk)
        data = content["values"]
        self.u_Id_var.set(data[0])
        self.name_var.set(data[1])
        self.roll_no_var.set(data[2])
        self.course_var.set(data[3])
        self.time_var.set(data[4])
        self.date_var.set(data[5])
        self.att_status_var.set(data[6])  


 


if __name__ == "__main__":
    window = Tk()
    main_win = Attendance(window)
    window.mainloop()

