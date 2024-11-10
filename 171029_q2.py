class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}
    
    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")
    
    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print(f"{self.name} has no grades yet.")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(f"Added student '{student.name}' (ID: {student.student_id}) to the course '{self.course_name}'.")
    
    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found.")
    
    def display_all_students_and_grades(self):
        if self.students:
            print(f"Students and grades for the course '{self.course_name}':")
            for student in self.students:
                print(f"\nStudent: {student.name} (ID: {student.student_id})")
                student.display_grades()
        else:
            print(f"No students enrolled in the course '{self.course_name}'.")

# Interactive code to manage students and assign grades
def course_management():
    instructor = Instructor("Dr. Smith", "Python Programming")
    
    while True:
        print("\nCourse Management System:")
        print("1. Add Student")
        print("2. Assign Grade")
        print("3. Display All Students and Grades")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)
        
        elif choice == "2":
            student_id = input("Enter student's ID to assign grade: ")
            assignment_name = input("Enter assignment name: ")
            try:
                grade = float(input("Enter grade: "))
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid input for grade. Please enter a numeric value.")
        
        elif choice == "3":
            instructor.display_all_students_and_grades()
        
        elif choice == "4":
            print("Exiting the course management system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the course management system
course_management()
