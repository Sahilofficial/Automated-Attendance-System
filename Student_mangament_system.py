'''
Author: Sahil Kumar
Email: sahilofficial74@gmail.com
Date: 2021-07-06 14:04:14   
Last Modified time: 2021-07-06 14:04:14
'''

from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import datetime as dt
import mysql.connector
import cv2




class Students:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1370x750")
        self.master.title("Automated Attendance System")
        self.master.iconbitmap(r"F:\Attendance_sys\v2\icon.ico")

    # all variable for Combobox, Entry and Radiobutton
    # left frame
        self.course_var = StringVar()
        self.year_var = StringVar()
        self.sub_var = StringVar()
        self.sem_var = StringVar()

        self.u_Id_var = StringVar()
        self.name_var = StringVar()
        self.roll_no_var = StringVar()
        self.gender_var = StringVar()
        self.dob_var = StringVar()
        self.mobile_no_var = StringVar()
        self.email_var = StringVar()
        self.address_var = StringVar()

        self.rdbtn_var = StringVar()


    # main frame
        frame = Frame(self.master, bd=2, bg="dark slate gray")
        frame.place(x=0, y=0, width=1370, height=750)

    # Heading "Student Management System"
        heading = Label(frame, text="Student Management System", font=("Helvetica", 34, "bold", "underline"), fg="aquamarine2", bg = "dark slate gray" )
        heading.grid(row=0, column=2, padx=370, pady=10, sticky=NW)

    # make two frames in main frame
        left_frame = LabelFrame(frame, text="Student Profile",font=("Times Roman", 15, "bold", "italic", "underline"), relief=RIDGE, bg="dark slate gray", fg="aquamarine2")
        left_frame.place(x=0, y=100, width=685, height=620)

        right_frame = LabelFrame(frame, text="Student Profile", font=("Times Roman", 15, "bold", "italic", "underline"), relief=RIDGE, bg="dark slate gray", fg="aquamarine2")
        right_frame.place(x=680, y=100, width=683, height=620)

# left frame
    # frame for Current Course Detail in left frame
        left_frame1 = LabelFrame(left_frame, text="Current Course Details", font=("Times Roman", 11), relief=RIDGE, bg="dark slate gray", fg="aquamarine2")
        left_frame1.place(x=0, y=10, width=685, height=140)

        course_label = Label(left_frame1, text="Course", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        course_label.grid(row=0, column=0,padx=10, pady=10, sticky=W)
        course = ttk.Combobox(left_frame1, width=27, state="readonly", textvariable=self.course_var)
        course["values"] = ["Select Course", "Tool", "Mechatronics", "Mechanical", "IT"]
        course.current(0)
        course.grid(row=0, column=1, padx=10, pady=20, sticky=W)

        year_label = Label(left_frame1, text="Year", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        year_label.grid(row=0, column=3, padx=25, pady=10, sticky=W)
        year = ttk.Combobox(left_frame1, width=27, state="readonly", textvariable=self.year_var)
        year["values"] = ["Select Year ", "1", "2", "3", "4"]
        year.current(0)
        year.grid(row=0, column=4, padx=5, pady=20, sticky=W)

        sub_label = Label(left_frame1, text="Subject", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        sub_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)
        sub = ttk.Combobox(left_frame1, width=27, state="readonly", textvariable=self.sub_var)
        sub["values"] = ["Select Subject ", "Mechanics", "Mathematics", "Robotics", "FMS", "RAC"]
        sub.current(0)
        sub.grid(row=1, column=1, padx=10, pady=20, sticky=E)

        sem_label = Label(left_frame1, text="Semester", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        sem_label.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        sem = ttk.Combobox(left_frame1, width=27, state="readonly", textvariable=self.sem_var)
        sem["values"] = ["Select Semester ", "1", "2", "3", "4", "5", "6", "7", "8"]
        sem.current(0)
        sem.grid(row=1, column=4, padx=5, pady=20, sticky=W)

    # Frame for Students Details in left frame
        left_frame2 = LabelFrame(left_frame, text="Students Details", font=("Times Roman", 11), relief=RIDGE, bg="dark slate gray", fg="aquamarine2")
        left_frame2.place(x=0, y=160, width=685, height=340)

        u_Id_label = Label(left_frame2, text="University_Id", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        u_Id_label.grid(row=0, column=0,padx=5, pady=20, sticky=W)
        u_Id = Entry(left_frame2, width=35, relief=RIDGE, textvariable=self.u_Id_var)
        u_Id.grid(row=0, column=1, padx=5, pady=20, sticky=W)

        name_label = Label(left_frame2, text="Name", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        name_label.grid(row=0, column=3, padx=10, pady=20, sticky=W)
        name = Entry(left_frame2, width=35, relief=RIDGE, textvariable=self.name_var)
        name.grid(row=0, column=4, padx=5, pady=20, sticky=W)

        roll_no_label = Label(left_frame2, text="Roll No.", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        roll_no_label.grid(row=1, column=0, padx=10, pady=20, sticky=W)
        roll_no = Entry(left_frame2, width=35, relief=RIDGE, textvariable=self.roll_no_var)
        roll_no.grid(row=1, column=1, padx=5, pady=20, sticky=W)
        
        dob_label = Label(left_frame2, text="DOB", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        dob_label.grid(row=1, column=3, padx=5, pady=20, sticky=W)
        dob = DateEntry(left_frame2, width=12, textvariable=self.dob_var, background='dark slate gray', foreground='aquamarine2', borderwidth=2)
        dob.set_date(dt.date.today())
        dob.grid(row=1, column=4, padx=5, pady=20, sticky=W)

        gender_label = Label(left_frame2, text="Gender", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        gender_label.grid(row=2, column=0, padx=10, pady=20, sticky=W)
        gender = ttk.Combobox(left_frame2, width=32, textvariable=self.gender_var, state="readonly")
        gender["values"] = ["Select Gender", "Male", "Female", "Prefer Not To Say"]
        gender.current(0)
        gender.grid(row=2, column=1, padx=5, pady=20, sticky=W)

        mobile_no_label = Label(left_frame2, text="Mobile No", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        mobile_no_label.grid(row=2, column=3, padx=10, pady=20, sticky=W)
        mobile_no = Entry(left_frame2, width=35, relief=RIDGE, textvariable=self.mobile_no_var)
        mobile_no.grid(row=2, column=4, padx=5, pady=20, sticky=W)

        email_label = Label(left_frame2, text="Email ID", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        email_label.grid(row=3, column=0, padx=10, pady=20, sticky=W)
        email = Entry(left_frame2, width=35, relief=RIDGE, textvariable=self.email_var)
        email.grid(row=3, column=1, padx=5, pady=20, sticky=W)

        address_label = Label(left_frame2, text="Address", font=("Times Roman", 10), bg="dark slate gray", fg="aquamarine2")
        address_label.grid(row=3, column=3, padx=10, pady=20, sticky=W)
        address = Entry(left_frame2, width=35, relief=RIDGE, textvariable=self.address_var)
        address.grid(row=3, column=4,columnspan=8, padx=5, pady=20, sticky=W)

        style1 = ttk.Style()
        style1.configure('style1.TRadiobutton', background="thistle")
        rdbtn1 = ttk.Radiobutton(left_frame2, text="Take Photo Sample", variable=self.rdbtn_var, value="Yes", style='style1.TRadiobutton')
        rdbtn1.grid(row=4, column=0, padx=10, pady=20, sticky=W)

        rdbtn2 = ttk.Radiobutton(left_frame2, text="No Photo Sample", variable=self.rdbtn_var, value="NO", style='style1.TRadiobutton')
        rdbtn2.grid(row=4, column=1, padx=10, pady=20, sticky=W)

    # creating frame for buttons
        left_frame3 = LabelFrame(left_frame, bd=0, relief=RIDGE, bg="dark slate gray", fg="aquamarine2")
        left_frame3.place(x=0, y=500, width=685, height=75)
        
        save = Button(left_frame3, text="Save", relief=RIDGE, width=22, font=("Helvetica", 8, "bold"), bg="light cyan", fg="dark slate gray", command=self.save_data)
        save.grid(row=0,column=0, padx=3, pady=3)

        reset = Button(left_frame3, text="Reset", relief=RIDGE, font=("Helvetica", 8, "bold"), command=self.reset_entries, width=22, bg="light cyan", fg="dark slate gray")
        reset.grid(row=0,column=1, padx=3, pady=3)

        update = Button(left_frame3, text="Update", relief=RIDGE, font=("Helvetica", 8, "bold"), command=self.update_profile, width=22, bg="light cyan", fg="dark slate gray")
        update.grid(row=0,column=2, padx=3, pady=3)

        delete = Button(left_frame3, text="Delete", relief=RIDGE, font=("Helvetica", 8, "bold"), command=self.delete_data, width=22, bg="light cyan", fg="dark slate gray")
        delete.grid(row=0,column=3, padx=3, pady=3)

        take_Photo = Button(left_frame3, text="Take Photo", relief=RIDGE, font=("Helvetica", 8, "bold"), command=self.generating_dataset, width=44, bg="light cyan", fg="dark slate gray")
        take_Photo.grid(row=1,column=0,columnspan=2, pady=3)

        update_Photo = Button(left_frame3, text="Update Photo", relief=RIDGE, font=("Helvetica", 8, "bold"), width=44, bg="light cyan", fg="dark slate gray")
        update_Photo.grid(row=1,column=2,columnspan=2, pady=3)


#right frame

    # table frame
        right_frame2 = Frame(right_frame, relief=RIDGE, bd=2, bg="dark slate gray", highlightcolor="aquamarine2")
        right_frame2.place(x=5, y=10, width=680, height=540)

        scroll_x = ttk.Scrollbar(right_frame2, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_frame2, orient=VERTICAL)

        self.student_tabel = ttk.Treeview(right_frame2,xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.student_tabel["column"] = ("course", "sub", "year", "sem", "u_Id", "name", "roll", "gender", "dob", "email", "mob", "add", "photo")

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)

        self.student_tabel.heading("course", text="Course")
        self.student_tabel.heading("sub", text="Subject")
        self.student_tabel.heading("year", text="Year")
        self.student_tabel.heading("sem", text="Semester")
        self.student_tabel.heading("u_Id", text="University_Id")
        self.student_tabel.heading("name", text="Name")
        self.student_tabel.heading("roll", text="Roll No.")
        self.student_tabel.heading("gender", text="Gender")
        self.student_tabel.heading("dob", text="DOB")
        self.student_tabel.heading("email", text="Email")
        self.student_tabel.heading("mob", text="Mobile No.")
        self.student_tabel.heading("add", text="Address")
        self.student_tabel.heading("photo", text="Photo")
        self.student_tabel["show"]='headings'

        self.student_tabel.column("course", width=100)
        self.student_tabel.column("sub", width=100)
        self.student_tabel.column("year", width=100)
        self.student_tabel.column("sem", width=100)
        self.student_tabel.column("u_Id", width=100)
        self.student_tabel.column("name", width=100)
        self.student_tabel.column("roll", width=100)
        self.student_tabel.column("gender", width=100)
        self.student_tabel.column("dob", width=100)
        self.student_tabel.column("email", width=100)
        self.student_tabel.column("mob", width=100)
        self.student_tabel.column("add", width=100)

        self.student_tabel.pack(fill=BOTH, expand=1)
        self.student_tabel.bind("<ButtonRelease>", self.select_student)
        self.show_data()

#  Fuctions

    def save_data(self):
        if self.course_var.get() == "Select Course" or self.name_var.get() == "" or self.u_Id_var.get() == "":
            messagebox.showerror("Error", "All fields are mandatory to fill", parent=self.master)
        else:
            try:
                crsVar = self.course_var
                yrsVar = self.year_var
                sbVar = self.sub_var
                smVar = self.sem_var
                uVar = self.u_Id_var
                nVar = self.name_var
                rollVar = self.roll_no_var
                genVar = self.gender_var
                dVar = self.dob_var
                mobVar = self.mobile_no_var
                eVar = self.email_var
                adVar = self.address_var
                rdVar = self.rdbtn_var
                

                print(repr(crsVar.get()), repr(sbVar.get()), repr(yrsVar.get()), repr(smVar.get()), repr(uVar.get()),
                          repr(nVar.get()), repr(rollVar.get()), repr(genVar.get()), repr(dVar.get()),
                          repr(eVar.get()), repr(mobVar.get()), repr(adVar.get()), repr(rdVar.get()))

                conn = mysql.connector.connect(host="localhost", username="root", password="Sahil#12", database="attendancesystem")
                c = conn.cursor()


                params = (crsVar.get(), sbVar.get(), yrsVar.get(), smVar.get(), uVar.get(),
                         nVar.get(), rollVar.get(), genVar.get(), dVar.get(),
                         eVar.get(), mobVar.get(), adVar.get(), rdVar.get())

                sql_insert_query = 'INSERT INTO `student_details`(Course, Subject, Years, Semester, University_Id, Student_Names, Roll_No, Gender, DOB, Email, Mobile, Address, Photo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            

                c.execute(sql_insert_query, params)

                          

                conn.commit()
                self.show_data()
                conn.close()
                messagebox.showinfo("Success", "Students details has been submitted", parent=self.master)

            except Exception as e:
                messagebox.showerror("Error", f"{str(e)}")


    def show_data(self): # function to show data in GUI table In right frame
        conn = mysql.connector.connect(host="localhost", username="root", password="Sahil#12", database="attendancesystem")
        c = conn.cursor()
        c.execute('SELECT * FROM student_details')
        data = c.fetchall()
        
        if len(data)!=0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in data:
                self.student_tabel.insert("",END, values=i)
            conn.commit()
        conn.close()

    def select_student(self, event=""): # click Students details in table and all details of selected student will be filled in entries in Students Profile section 
        clk = self.student_tabel.focus()
        content = self.student_tabel.item(clk)
        data = content["values"]
                          
        self.course_var.set(data[0])
        self.year_var.set(data[1])
        self.sub_var.set(data[2])
        self.sem_var.set(data[3])
        self.u_Id_var.set(data[4])
        self.name_var.set(data[5])
        self.roll_no_var.set(data[6])
        self.gender_var.set(data[7])
        self.dob_var.set(data[8])
        self.mobile_no_var.set(data[9])
        self.email_var.set(data[10])
        self.address_var.set(data[11])
        self.rdbtn_var.set(data[12])


    def update_profile(self):


        if self.course_var.get() == "Select Course" or self.name_var.get() == "" or self.u_Id_var.get() == "":
            messagebox.showerror("Error", "All fields are mandatory to fill", parent=self.master)
        else:
            try:
                update_msg = messagebox.askyesno("Info", "Do you want to update this student's profile", parent=self.master)
                
                if update_msg == True:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sahil#12", database="attendancesystem")
                    c = conn.cursor()
                    params = (self.course_var.get(), self.year_var.get(), self.sub_var.get(),
                                self.sem_var.get(), self.name_var.get(),self.roll_no_var.get(), self.gender_var.get(),
                                self.dob_var.get(), self.mobile_no_var.get(), self.email_var.get(),
                                 self.address_var.get(), self.rdbtn_var.get(), self.u_Id_var.get())
                                
                    sql_update_query = "UPDATE  `student_details` SET Course = %s, Subject=%s, Years=%s, Semester=%s, Student_Names=%s, Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Mobile=%s, Address=%s, Photo=%s WHERE University_Id=%s"
                    c.execute(sql_update_query,params)
                    
                       
                else:
                    return
                conn.commit()
                self.show_data()
                conn.close()
                messagebox.showinfo("Success", "Data is updated successfully", parent=self.master)

            except Exception as e:
                messagebox.showerror("Error", f"{str(e)}", parent=self.master)


    def delete_data(self):
        if self.u_Id_var.get() == "":
            messagebox.showerror("Error", "University's Id must be required", parent=self.master)

        else:
            try:
                del_msg = messagebox.askyesno("Info", "Are you sure you want to delete this students record", parent=self.master)
                if del_msg == True:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sahil#12", database="attendancesystem")
                    c = conn.cursor()
                    sql_del_query = "DELETE FROM `student_details` WHERE University_Id=%s"
                    param = (self.u_Id_var.get(),)
                    c.execute(sql_del_query, param)
                
                else:
                    return
                
                conn.commit()
                self.show_data()
                conn.close()
                messagebox.showinfo("Success", "Data is deleted successfully", parent=self.master)

            except Exception as e:
                messagebox.showerror("Error", f"{str(e)}", parent=self.master)

    def reset_entries(self):
        self.course_var.set(" Select Course")
        self.year_var.set("Select Year")
        self.sub_var.set("select Subject")
        self.sem_var.set("Select Semester")
        self.u_Id_var.set("")
        self.name_var.set("")
        self.roll_no_var.set("")
        self.gender_var.set("Select Gender")
        self.mobile_no_var.set("")
        self.email_var.set("")
        self.address_var.set("")

    def generating_dataset(self):
        if self.course_var.get() == "Select Course" or self.name_var.get() == "" or self.u_Id_var.get() == "":
            messagebox.showerror("Error", "All fields are mandatory to fill", parent=self.master)
        else:
            try:

                conn = mysql.connector.connect(host="localhost", username="root", password="Sahil#12", database="attendancesystem")
                c = conn.cursor()
                c.execute('SELECT * FROM student_details')
                result = c.fetchall()
                id = 0
                for i in result:
                    id+=1
                params = (self.course_var.get(), self.year_var.get(), self.sub_var.get(),
                      self.sem_var.get(), self.name_var.get(), self.roll_no_var.get(), self.gender_var.get(),
                      self.dob_var.get(), self.mobile_no_var.get(), self.email_var.get(),
                      self.address_var.get(), self.rdbtn_var.get(), self.u_Id_var.get()==id+1)

                sql_update_query = "UPDATE  `student_details` SET Course = %s, Subject=%s, Years=%s, Semester=%s, Student_Names=%s, Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Mobile=%s, Address=%s, Photo=%s WHERE University_Id=%s"
                c.execute(sql_update_query, params)
                conn.commit()
                self.show_data()
                self.reset_entries()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray_img, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(r"F:\Attendance_sys\v3\test\Adobe_Spark_Video.mp4")
                img_id = 0
                while True:
                    ret, frame = cap.read()
                    if face_cropped(frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        data_path = "data/student." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(data_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (230, 35, 150), 2)
                        cv2.imshow("Camera", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Info", "Successfully Generate Dataset")
            except Exception as e:
                messagebox.showerror("Error", f"{str(e)}", parent=self.master)



if __name__=="__main__":
    window=Tk()
    st = Students(window)
    window.mainloop()







