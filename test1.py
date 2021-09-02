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





    def face_recog(self):
        def draw_boundaries(img, classifier, scalefactor, minNeighbors, color, text, clf):

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scalefactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(gray_img, (x, y), (x + w, y + h), (50, 255, 2), 3)
                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                accuracy = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Root#12",
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
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            print("ret status : ", ret)
            img = recognize(frame, clf, face_cascade)
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
        cap.release()
        cv2.destroyAllWindows()
