import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QLineEdit

button_y_position = 0.1  # Initial Y position for the buttons
class Addsubject(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Custom Pop-up Block')
        self.setGeometry(300, 200, 400, 200)

        # Create layouts for the dialog
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Create labels and line edits for subject name, teacher name, and number of students
        subject_label = QLabel("Subject Name:")
        self.subject_edit = QLineEdit(self)

        teacher_label = QLabel("Teacher Name:")
        self.teacher_edit = QLineEdit(self)

        students_label = QLabel("Number of Students:")
        self.students_edit = QLineEdit(self)

        # Create and add a button to the button layout
        button1 = QPushButton("Create")
        button1.clicked.connect(self.on_button1_click)

        # Add labels, line edits, and the button to the layouts
        main_layout.addWidget(subject_label)
        main_layout.addWidget(self.subject_edit)
        main_layout.addWidget(teacher_label)
        main_layout.addWidget(self.teacher_edit)
        main_layout.addWidget(students_label)
        main_layout.addWidget(self.students_edit)
        button_layout.addWidget(button1)

        # Set the layouts for the dialog
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def on_button1_click(self):
        subject_name = self.subject_edit.text()
        teacher_name = self.teacher_edit.text()
        num_students = self.students_edit.text()
        print(f"Subject Name: {subject_name}, Teacher Name: {teacher_name}, Students: {num_students}")
        self.accept()
        
    def create_class_data(self):
        subject_name = self.subject_edit.text()
        teacher_name = self.teacher_edit.text()
        num_students = self.students_edit.text()
        return subject_name , teacher_name , num_students
