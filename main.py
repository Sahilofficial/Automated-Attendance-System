
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
from time import strftime
import datetime as dt
from numpy.lib.shape_base import split
import mysql.connector
from Student_mangament_system import Students
from Attendance import Attendance


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("900x600")
        self.master.title("Automated Attendance System")
        self.master.iconbitmap(r"F:\Attendance_sys\v2\icon.ico")
    # main frame
        frame = Frame(self.master, bd=2, bg="dark slate gray")
        frame.place(x=0, y=0, width=900, height=600)

        imgframe = Frame(frame, bd=2, bg="dark slate gray")
        imgframe.place(x=0, y=0, width=150, height=100)
        img_label = Label(imgframe)
        img = Image.open(r"F:\Attendance_sys\v3\img.png")
        img = img.resize((60, 60))
        img_label.image = ImageTk.PhotoImage(img)
        img_label['image'] = img_label.image
        img_label.grid(padx=38, pady=20)


        heading = Label(frame, text="Automated Attendance System", font=("Helvetica", 35, "bold", "underline", "italic"), bg="light cyan", fg="dark slate gray" )
        heading.grid(row=0, column=1, padx=125, pady=23, columnspan=4)

        sms_btn = Button(frame, text = "Students Management System", relief=RIDGE, width=30, height=3,
                         font=("Helvetica", 10, "bold", "underline"), bg="light cyan", fg="dark slate gray", command=self.student)
        sms_btn.grid(row=2,column=1, padx=50, pady=50)

        att_btn = Button(frame, text="Attendance", relief=RIDGE, width=30, height=3,command=self.attendance,
                         font=("Helvetica", 10, "bold", "underline"), bg="light cyan", fg="dark slate gray")
        att_btn.grid(row=2, column=3, padx=50, pady=50)

        face_recog_btn = Button(frame, text="Mark Attendance", relief=RIDGE, width=30, height=3, command=self.face_recog_attendance,
                           font=("Helvetica", 10, "bold", "underline"), bg="light cyan", fg="dark slate gray")
        face_recog_btn.grid(row=3, column=1, padx=50, pady=50)

        photo_btn = Button(frame, text="Images", relief=RIDGE, width=30, height=3,
                           font=("Helvetica", 10, "bold", "underline"), bg="light cyan", fg="dark slate gray", command=self.photo)
        photo_btn.grid(row=3, column=3, padx=50, pady=50)

        train_btn = Button(frame, text="Train Images", relief=RIDGE, width=30, height=3, command=self.train,
                           font=("Helvetica", 10, "bold", "underline"), bg="light cyan", fg="dark slate gray")
        train_btn.grid(row=4, column=1, padx=50, pady=50)

        train_btn = Button(frame, text="Exit", relief=RIDGE, width=30, height=3, command=quit,
                           font=("Helvetica", 10, "bold", "underline"), bg="light cyan", fg="dark slate gray")
        train_btn.grid(row=4, column=3, padx=50, pady=50)


    def student(self):
        self.win = Toplevel(self.master)
        self.st = Students(self.win)

    def photo(self):
        os.startfile(r"F:\Attendance_sys\v3\data")

    def train(self):
        data_dir = ("F:\\Attendance_sys\\v3\\data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert("L")
            img_arr = np.array(img, 'uint8')
            split_path = os.path.split(image)[1].split('.')
            i = int(split_path[1])
            faces.append(img_arr)
            ids.append(i)
            cv2.imshow("TRAINING",img_arr)
            cv2.waitKey(1)==13
        
        ids = np.array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("trainig_classifiers.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Complete")


    
    def mark_attendance(self, u_id_data, name_data, roll_no_data, course_data):
        with open(r'F:\Attendance_sys\v3\attendance.csv', 'r+', newline="\n") as f:
            data_list = f.readlines()
            name_list = []
            for lines in data_list:
                entry = lines.split(',')
                name_list.append(entry[0])
                
            
            if ((name_data not in name_list) and (roll_no_data not in name_list) and (course_data not in name_list) and (u_id_data not in name_list)):
                now = dt.datetime.now()
                d1 = now.strftime('%d-%m-%Y')
                dstring = now.strftime('%H:%M:%S')
                f.writelines(f"\n{u_id_data}, {name_data}, {roll_no_data}, {course_data}, {dstring}, {d1}, Present")





    def face_recog_attendance(self):
        def draw_boundaries(img, classifier, scalefactor, minNeighbors, color, text, clf):

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scalefactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(gray_img, (x, y), (x + w, y + h), (50, 255, 2), 3)
                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                accuracy = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Sahil#12",
                                               database="attendancesystem")
                c = conn.cursor()

                c.execute("SELECT Student_Names FROM `student_details` WHERE University_Id = " + str(id))
                name_data = c.fetchone()
                name_data = "+".join(name_data)

                c.execute("SELECT Roll_No FROM `student_details` WHERE University_Id = " + str(id))
                roll_no_data = c.fetchone()
                roll_no_data = "+".join(roll_no_data)

                c.execute("SELECT Course FROM `student_details` WHERE University_Id = " + str(id))
                course_data = c.fetchone()
                course_data = "+".join(course_data)

                c.execute("SELECT University_Id FROM `student_details` WHERE University_Id = " + str(id))
                u_id_data = c.fetchone()
                u_id_data = "+".join(u_id_data)

                if accuracy > 90:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 255, 10), 3)
                    cv2.putText(img, f"University ID : {u_id_data}", (x, y - 80), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (255, 175, 35), 2)
                    cv2.putText(img, f"Name : {name_data}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (255, 175, 35), 2)
                    cv2.putText(img, f"Roll No. : {roll_no_data}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (255, 175, 35), 2)
                    cv2.putText(img, f"Course : {course_data}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (255, 175, 35), 2)
                    self.mark_attendance(u_id_data, name_data, roll_no_data, course_data)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (10, 10, 255), 3)
                    cv2.putText(img, "UNKNOWN", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (150, 50, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, face_cascade):
            coordinates = draw_boundaries(img, face_cascade, 1.1, 10, (190, 130, 5), "Face", clf)
            return img

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"F:\Attendance_sys\v3\trainig_classifiers.xml")
        cap = cv2.VideoCapture(r"F:\Attendance_sys\v3\test\ld.mp4")
        while True:
            ret, frame = cap.read()
            print("ret status : ", ret)
            img = recognize(frame, clf, face_cascade)
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
        cap.release()
        cv2.destroyAllWindows()

    def attendance(self):
        self.win = Toplevel(self.master)
        self.st = Attendance(self.win)



















if __name__ == "__main__":
    
    window=Tk()
    main_win = MainWindow(window)
    window.mainloop()

