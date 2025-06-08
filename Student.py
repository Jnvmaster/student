from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1930x1005+0+0")
        self.root.title("Face Recognition System")

        # Variables for entry fields
        self.var_dep = StringVar(value="Select Department")
        self.var_course = StringVar(value="Select Course")
        self.var_semester = StringVar(value="Select Semester")
        self.var_year = StringVar(value="Select Year")
        self.var_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_class_division = StringVar()
        self.var_roll_no = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_gender = StringVar()
        self.var_mentor = StringVar()
        self.var_photo_sample = StringVar(value="no")  # For radiobutton

        # Images and layout (unchanged)
        img = Image.open(r"C:\Users\Admin\Downloads\pes.jpg")
        img = img.resize((643, 150), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=0, y=0, width=643, height=150)

        img1 = Image.open(r"C:\Users\Admin\Downloads\logo.jfif")
        img1 = img1.resize((643, 150), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl1 = Label(self.root, image=self.photoimg1)
        lbl1.place(x=643, y=0, width=633, height=150)

        img2 = Image.open(r"C:\Users\Admin\Downloads\pes.jpg")
        img2 = img2.resize((644, 150), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl2 = Label(self.root, image=self.photoimg2)
        lbl2.place(x=1280, y=0, width=644, height=150)

        img3 = Image.open(r"C:\Users\Admin\Downloads\face.jpg")
        img3 = img3.resize((1930, 1005), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg3 = Label(self.root, image=self.photoimg3)
        bg3.place(x=0, y=150, width=1930, height=1005)

        title_lbl = Label(bg3, text="STUDENT MANAGEMENT SECTION", font=("Times New Roman", 35, "bold"),
                          bg="black", fg="darkgreen", bd=5)
        title_lbl.place(x=0, y=0, width=1930, height=45)

        main_frame = Frame(bg3, bd=2)
        main_frame.place(x=15, y=60, width=1880, height=900)

        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("Times New Roman", 12, "bold"), bg="white")
        left_frame.place(x=10, y=10, width=910, height=760)

        img_left = Image.open(r"C:\Users\Admin\Downloads\pes.jpg")
        img_left = img_left.resize((900, 150), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        lbl = Label(left_frame, image=self.photoimg_left)
        lbl.place(x=5, y=0, width=900, height=150)

        course_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Current Course",
                                  font=("Times New Roman", 15, "bold"), bg="white")
        course_frame.place(x=10, y=155, width=910, height=210)

        dep_lbl = Label(course_frame, text="Department:", font=("Times New Roman", 15, "bold"), bd=5, bg="white")
        dep_lbl.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(course_frame, textvariable=self.var_dep, font=("Times New Roman", 15, "bold"),
                                   width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "ECE", "VLSI", "MECHANICAL", "CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        course_lbl = Label(course_frame, text="Course:", font=("Times New Roman", 15, "bold"), bd=5, bg="white")
        course_lbl.grid(row=0, column=2, padx=10)

        cou_combo = ttk.Combobox(course_frame, textvariable=self.var_course, font=("Times New Roman", 15, "bold"),
                                   width=17, state="readonly")
        cou_combo["values"] = ("Select Course", "FY", "SY", "TY", "BE")
        cou_combo.current(0)
        cou_combo.grid(row=0, column=3, padx=2, pady=10)

        sem_lbl = Label(course_frame, text="Semester:", font=("Times New Roman", 15, "bold"), bd=5, bg="white")
        sem_lbl.grid(row=1, column=0, padx=20, pady=50)

        sem_combo = ttk.Combobox(course_frame, textvariable=self.var_semester, font=("Times New Roman", 15, "bold"),
                                   width=17, state="readonly")
        sem_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=1, padx=2, pady=10)

        year_lbl = Label(course_frame, text="Year:", font=("Times New Roman", 15, "bold"), bd=5, bg="white")
        year_lbl.grid(row=1, column=2, padx=20, pady=50)

        year_combo = ttk.Combobox(course_frame, textvariable=self.var_year, font=("Times New Roman", 15, "bold"),
                                    width=17, state="readonly")
        year_combo["values"] = ("Select Year", "2022-23", "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=2, pady=10)

        student_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Information",
                                     font=("Times New Roman", 15, "bold"), bg="white")
        student_frame.place(x=10, y=360, width=910, height=470)

        labels = ["Student ID:", "Student Name:", "Class Division:", "Roll No:", "DOB:", "Email:",
                  "Phone No:", "Address:", "Gender:", "Mentor Name:"]
        variables = [self.var_student_id, self.var_student_name, self.var_class_division, self.var_roll_no,
                     self.var_dob, self.var_email, self.var_phone, self.var_address, self.var_gender,
                     self.var_mentor]

        positions = [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 0), (4, 2)]

        for i, (text, var, pos) in enumerate(zip(labels, variables, positions)):
            lbl = Label(student_frame, text=text, font=("Times New Roman", 15, "bold"), bd=5, bg="white")
            lbl.grid(row=pos[0], column=pos[1], padx=20, pady=10)
            entry = ttk.Entry(student_frame, textvariable=var, width=20, font=("Times New Roman", 15, "bold"))
            entry.grid(row=pos[0], column=pos[1] + 1, padx=5, pady=10)

        radionbtn1 = ttk.Radiobutton(student_frame, text="Take photo sample", variable=self.var_photo_sample, value="yes")
        radionbtn1.grid(row=5, column=0, pady=10)

        radionbtn2 = ttk.Radiobutton(student_frame, text="No photo sample", variable=self.var_photo_sample, value="no")
        radionbtn2.grid(row=5, column=1, pady=10)

        button_frame = Frame(student_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=310, width=890, height=45)

        save_btn = Button(button_frame, text="Save", width=17, font=("Times New Roman", 15, "bold"),
                          bd=5, bg="grey", command=self.save_data)
        save_btn.grid(row=0, column=0)

        update_btn = Button(button_frame, text="Update", width=17, font=("Times New Roman", 15, "bold"),
                            bd=5, bg="grey", command=self.update_data)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(button_frame, text="Delete", width=17, font=("Times New Roman", 15, "bold"),
                            bd=5, bg="grey", command=self.delete_data)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(button_frame, text="Reset", width=18, font=("Times New Roman", 15, "bold"),
                           bd=5, bg="grey", command=self.reset_data)
        reset_btn.grid(row=0, column=3)

        button_frame1 = Frame(student_frame, bd=2, relief=RIDGE, bg="white")
        button_frame1.place(x=0, y=355, width=890, height=45)

        tps_btn = Button(button_frame1, text="Take Photo Sample", width=35, font=("Times New Roman", 15, "bold"),
                         bd=5, bg="grey", command=self.take_photo_sample)
        tps_btn.grid(row=0, column=0)

        tps1_btn = Button(button_frame1, text="Update Photo Sample", width=37, font=("Times New Roman", 15, "bold"),
                          bd=5, bg="grey", command=self.update_photo_sample)
        tps1_btn.grid(row=0, column=1)

        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Search Details",
                                 font=("Times New Roman", 12, "bold"), bg="white")
        right_frame.place(x=910, y=10, width=930, height=760)

        img_right = Image.open(r"C:\Users\Admin\Downloads\pes.jpg")
        img_right = img_right.resize((900, 150), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        lbl = Label(right_frame, image=self.photoimg_right)
        lbl.place(x=5, y=0, width=900, height=150)

        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Student Details",
                                  font=("Times New Roman", 12, "bold"), bg="white")
        search_frame.place(x=10, y=180, width=910, height=80)

        search_by_lbl = Label(search_frame, text="Search by:", font=("Times New Roman", 15, "bold"),
                              bd=5, bg="white", fg="red")
        search_by_lbl.grid(row=0, column=0, padx=10)

        self.var_search_by = StringVar(value="Search_By")
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search_by, font=("Times New Roman", 15, "bold"),
                                      width=14, state="readonly")
        search_combo["values"] = ("Search_By", "Roll_No", "PRN", "Student_ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10)

        self.var_search_txt = StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search_txt, width=16,
                                 font=("Times New Roman", 15, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=10)

        search_btn = Button(search_frame, text="Search", width=14, font=("Times New Roman", 15, "bold"),
                            bd=7, bg="grey", command=self.search_data)
        search_btn.grid(row=0, column=3, padx=10)

        show_all_btn = Button(search_frame, text="Show All", width=14, font=("Times New Roman", 15, "bold"),
                              bd=7, bg="grey", command=self.show_all_data)
        show_all_btn.grid(row=0, column=4, padx=7)

        table_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=280, width=910, height=430)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          columns=("Name", "Roll_No", "Student_ID", "Class", "DOB", "Gender",
                                                   "Phone_No", "Email", "Address", "Mentor_Name"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll_No", text="Roll_No")
        self.student_table.heading("Student_ID", text="Student_ID")
        self.student_table.heading("Class", text="Class")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Phone_No", text="Phone_No")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Mentor_Name", text="Mentor_Name")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        # Bind table selection
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Connect to DB & initialize table
        self.connect_database()
        self.show_all_data()

    # Database connection
    def add_data(self):
        if self.var_dep.grt=="select department" or sef.var_student_name.get=="":

            messagebox.showerror("error","all fildes are required")
        else:
            try:
                conn = mysql.connector.connect(
                host="localhost",      # change if needed
                user="root",           # change if needed
                password="Pratik@05",           # change if needed
                 database="college"  # change if needed or create before running
            )
                my_cursor = conn.cursor()
            
                my_cursor.execute("INSERT INTO students values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                  (self.var_dep.get(),self.var_course.get(), self.var_semester.get(), self.var_year.get(),
                      self.var_student_id.get(), self.var_student_name.get(), self.var_class_division.get(),
                      self.var_roll_no.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                      self.var_address.get(), self.var_gender.get(), self.var_mentor.get(), self.var_photo_sample.get()))
           
                conn.commit()
                conn.close()
            
            
                except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database:\n{e}")

    def save_data(self):
        if self.var_student_id.get() == "" or self.var_student_name.get() == "":
            messagebox.showerror("Error", "Student ID and Name are required")
            return
        try:
            query = "INSERT INTO students (dep, course, semester, year, student_id, name, class_division, roll_no, dob, email, phone, address, gender, mentor, photo_sample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.var_dep.get(), self.var_course.get(), self.var_semester.get(), self.var_year.get(),
                      self.var_student_id.get(), self.var_student_name.get(), self.var_class_division.get(),
                      self.var_roll_no.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                      self.var_address.get(), self.var_gender.get(), self.var_mentor.get(), self.var_photo_sample.get())
            my_cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Data saved successfully")
            show_all_data()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Student ID already exists. Use update instead.")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def update_data(self):
        if self.var_student_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to update data")
            return
        try:
            query = "UPDATE students SET dep=%s, course=%s, semester=%s, year=%s, name=%s, class_division=%s, roll_no=%s, dob=%s, email=%s, phone=%s, address=%s, gender=%s, mentor=%s, photo_sample=%s WHERE student_id=%s"
            values = (self.var_dep.get(), self.var_course.get(), self.var_semester.get(), self.var_year.get(),
                      self.var_student_name.get(), self.var_class_division.get(), self.var_roll_no.get(),
                      self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                      self.var_gender.get(), self.var_mentor.get(), self.var_photo_sample.get(), self.var_student_id.get())
            my_cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Data updated successfully")
            show_all_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def delete_data(self):
        if self.var_student_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to delete data")
            return
        try:
            option = messagebox.askyesno("Confirm Delete", "Do you want to delete this record?")
            if option:
                query = "DELETE FROM students WHERE student_id=%s"
                my_cursor.execute(query, (self.var_student_id.get(),))
                conn.commit()
                messagebox.showinfo("Deleted", "Record deleted successfully")
                show_all_data()
                reset_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_semester.set("Select Semester")
        self.var_year.set("Select Year")
        self.var_student_id.set("")
        self.var_student_name.set("")
        self.var_class_division.set("")
        self.var_roll_no.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_gender.set("")
        self.var_mentor.set("")
        self.var_photo_sample.set("no")

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]
        if data:
            self.var_student_name.set(data[0])
            self.var_roll_no.set(data[1])
            self.var_student_id.set(data[2])
            self.var_class_division.set(data[3])
            self.var_dob.set(data[4])
            self.var_gender.set(data[5])
            self.var_phone.set(data[6])
            self.var_email.set(data[7])
            self.var_address.set(data[8])
            self.var_mentor.set(data[9])
            # For dept, course, semester, year and photo_sample, you can add code if needed by querying database

    def show_all_data(self):
        try:
            self.my_cursor.execute("SELECT name, roll_no, student_id, class_division, dob, gender, phone, email, address, mentor FROM students")
            rows = self.my_cursor.fetchall()
            if rows:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def search_data(self):
        if self.var_search_by.get() == "Search_By" or self.var_search_txt.get() == "":
            messagebox.showerror("Error", "Select search criteria and enter search text")
            return
        try:
            if self.var_search_by.get() == "Roll_No":
                query = "SELECT name, roll_no, student_id, class_division, dob, gender, phone, email, address, mentor FROM students WHERE roll_no LIKE %s"
                value = ("%" + self.var_search_txt.get() + "%",)
            elif self.var_search_by.get() == "PRN":
                query = "SELECT name, roll_no, student_id, class_division, dob, gender, phone, email, address, mentor FROM students WHERE student_id LIKE %s"
                value = ("%" + self.var_search_txt.get() + "%",)
            elif self.var_search_by.get() == "Student_ID":
                query = "SELECT name, roll_no, student_id, class_division, dob, gender, phone, email, address, mentor FROM students WHERE student_id LIKE %s"
                value = ("%" + self.var_search_txt.get() + "%",)
            else:
                messagebox.showerror("Error", "Invalid search criteria")
                return

            self.my_cursor.execute(query, value)
            rows = self.my_cursor.fetchall()
            if rows:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No records found")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    # ================= OpenCV Functions for Photo Capture =========================
    def take_photo_sample(self):
        if self.var_student_id.get() == "" or self.var_student_name.get() == "":
            messagebox.showerror("Error", "Student ID and Name are required to take photo samples.", parent=self.root)
            return

        student_id = self.var_student_id.get()
        # Path to the cascade file
        cascade_path = 'C:/Users/Admin/AppData/Local/Programs/Python/Python313/haarcascade_frontalface_default.xml'
        clf = cv2.CascadeClassifier(cascade_path)
        if clf.empty():
            messagebox.showerror("Error", f"Could not load cascade classifier from {cascade_path}", parent=self.root)
            return

        # Create a directory to save images if it doesn't exist
        if not os.path.exists("data"):
            os.makedirs("data")

        # Open the camera
        cap = cv2.VideoCapture(0)
        img_id = 0

        while True:
            ret, my_frame = cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to grab frame from camera.", parent=self.root)
                break
                
            gray_frame = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
            faces = clf.detectMultiScale(gray_frame, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(my_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                img_id += 1
                face_roi = gray_frame[y:y+h, x:x+w]
                face_resized = cv2.resize(face_roi, (450, 450))

                # Save the captured image
                img_path = f"data/user.{student_id}.{img_id}.jpg"
                cv2.imwrite(img_path, face_resized)
                cv2.putText(my_frame, f"Sample: {img_id}", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
            
            cv2.imshow("Taking Photo Samples...", my_frame)

            # Wait for 'q' key to be pressed to exit or if 100 samples are taken
            if cv2.waitKey(1) == 13 or img_id == 100:
                break
        
        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Photo samples generated successfully!", parent=self.root)
    
    def update_photo_sample(self):
        # This function can be an alias for take_photo_sample as the process is identical
        self.take_photo_sample()


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
