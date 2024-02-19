students = []
courses = []
marks = []

def input_number_of_students():
    num_students = int(input("Enter the number of students in the class: "))
    students.clear()

    for _ in range(num_students):
        print("Enter information for Student:")
        student_id = input("Student ID: ")
        student_name = input("Student Name: ")
        dob = input("Date of Birth: ")

        students.append({"id": student_id, "name": student_name, "dob": dob})

    print("Student information entered successfully!")


def input_student_information():
    student_id = input("Enter the student ID: ")
    student_name = input("Enter the student Name: ")
    dob = input("Enter the student Date of Birth: ")

    students.append({"id": student_id, "name": student_name, "dob": dob})

    print("Student information entered successfully!")


def input_number_of_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses.clear()

    for _ in range(num_courses):
        print("Enter information for Course:")
        course_id = input("Course ID: ")
        course_name = input("Course Name: ")

        courses.append({"id": course_id, "name": course_name})

    print("Course information entered successfully!")


def input_course_information():
    course_id = input("Enter the course ID: ")
    course_name = input("Enter the course Name: ")

    courses.append({"id": course_id, "name": course_name})

    print("Course information entered successfully!")


def input_marks():
    list_courses()
    if not courses:
        print("No courses available. Please input course information first.")
        return

    course_id = input("Select a course by entering the course ID: ")
    selected_course = get_course_by_id(course_id)
    if not selected_course:
        print("Invalid course ID. Please try again.")
        return

    list_students()
    if not students:
        print("No students available. Please input student information first.")
        return

    print(f"Enter marks for students in the course: {selected_course['name']}")

    for student in students:
        student_id = student["id"]
        marks_value = float(input(f"Enter marks for student {student_id}: "))

        marks.append({"student_id": student_id, "course_id": course_id, "marks": marks_value})

    print("Marks entered successfully!")


def list_courses():
    print("Courses:")
    for course in courses:
        print(f"Course ID: {course['id']}")
        print(f"Course Name: {course['name']}")
        print()


def list_students():
    print("Students:")
    for student in students:
        print(f"Student ID: {student['id']}")
        print(f"Student Name: {student['name']}")
        print(f"Date of Birth: {student['dob']}")
        print()


def show_student_marks():
    list_courses()
    if not courses:
        print("No courses available. Please input course information first.")
        return

    course_id = input("Select a course by entering the course ID: ")
    selected_course = get_course_by_id(course_id)
    if not selected_course:
        print("Invalid course ID. Please try again.")
        return

    print(f"Marks for students in the course: {selected_course['name']}")
    found = False

    for mark in marks:
        if mark["course_id"] == course_id:
            found = True
            student = get_student_by_id(mark["student_id"])
            if student:
                print(f"Student ID: {student['id']}")
                print(f"Student Name: {student['name']}")
                print(f"Marks: {mark['marks']}")
                print()

    if not found:
        print("No marks found for the selected course.")


def get_course_by_id(course_id):
    for course in courses:
        if course["id"] == course_id:
            return course
    return None


def get_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def main():
    print("Welcome to Student Course Management System!")

    while True:
        print("\nMenu:")
        print("1. Input number of students in a class")
        print("2. Input student information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Select a course and input marks for students")
        print("6. List courses")
        print("7. List students")
        print("8. Show student marks for a given course")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            input_number_of_students()
        elif choice =="2":
            input_student_information()
        elif choice == "3":
            input_number_of_courses()
        elif choice == "4":
            input_course_information()
        elif choice == "5":
            input_marks()
        elif choice == "6":
            list_courses()
        elif choice == "7":
            list_students()
        elif choice == "8":
            show_student_marks()
        elif choice == "0":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
