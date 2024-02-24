import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class Mark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

students = []
courses = []
marks = []

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    student = Student(student_id, name, dob)
    students.append(student)

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    course = Course(course_id, name)
    courses.append(course)

def select_course():
    print("Available courses:")
    for index, course in enumerate(courses):
        print(f"{index + 1}. {course.name}")
    choice = int(input("Select a course (enter the number): "))
    course = courses[choice - 1]
    return course

def input_student_marks(course):
    for student in students:
        mark = int(input(f"Enter mark for student {student.name} in course {course.name}: "))
        mark_obj = Mark(student.student_id, course.course_id, mark)
        marks.append(mark_obj)

def list_courses():
    print("Courses:")
    for course in courses:
        print(f"Course ID: {course.course_id}, Name: {course.name}")

def list_students():
    print("Students:")
    for student in students:
        print(f"Student ID: {student.student_id}, Name: {student.name}")

def show_student_marks(course):
    print(f"Student marks for course {course.name}:")
    for mark in marks:
        if mark.course_id == course.course_id:
            student = next((student for student in students if student.student_id == mark.student_id), None)
            print(f"Student ID: {student.student_id}, Name: {student.name}, Mark: {mark.mark}")

def calculate_average_gpa(students):
    marks = np.array([mark.mark for mark in student.marks])
    credits = np.array([3 for _ in student.marks])
    weighted_sum = np.sum(marks * credits)
    total_credits = np.sum(credits)
    average_gpa = weighted_sum/total_credits
    return average_gpa

def sort_students_by_gpa():
    students.sort(key=lambda student: calculate_average_gpa(student), reverse=True)

# Main program
num_students = input_number_of_students()
for _ in range(num_students):
    input_student_information()

num_courses = input_number_of_courses()
for _ in range(num_courses):
    input_course_information()

selected_course = select_course()
input_student_marks(selected_course)

list_courses()
list_students()

show_student_marks(selected_course)

# Calculate and display average GPA for a given student
student_id = input("Enter student ID to calculate average GGPA: ")
selected_student = next((student for student in students if student.student_id == student_id), None)
if selected_student:
    average_gpa = calculate_average_gpa(selected_student)
    print(f"Avergae GPA for student {selected_student.name}: {average_gpa}")

# Sort students by GPA descending
sort_students_by_gpa()
print("Students sorted by GPA (descending):")
for student in students:
    print(f"Student ID: {student,student.id}, Name: {student.name}, GPA: {calculate_average_gpa(student)}")




