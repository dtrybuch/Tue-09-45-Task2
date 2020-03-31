# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
class Diary:
    def __init__(self, students):
        self.students = students
    

    def get_students_grades(self,name,surname):
        for student in self.students:
            if student.name == name and student.surname == surname:
                return student.grades


    def get_student(self, name, surname):
        for student in self.students:
            if student.name == name and student.surname == surname:
                return student


    def get_students_average(self):
        sum = 0
        len = 0
        for student in self.students:
            for grade in student.grades:
                sum = sum + grade
                len = len + 1
        if len == 0:
            return 0
        return sum/len


    def get_student_average(self, name, surname):
        student = self.get_student(name,surname)
        sum = 0
        for grade in student.grades:
            sum = sum + grade
        if len(student.grades) == 0:
            return 0
        return sum/len(student.grades)


    def add_student(self, student):
        students.append(student)


    def add_grade_for_student(self, name, surname, grade):
        student = self.get_student(name,surname)
        student.add_grade(grade)


class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []

        
    def add_grade(self, grade):
        self.grades.append(grade)

if __name__ == "__main__":
    students = []
    students.append(Student('Jan','Kowalski'))
    diary = Diary(students) 
    diary.add_grade_for_student('Jan','Kowalski',5)
    diary.add_grade_for_student('Jan','Kowalski',2)
    diary.add_grade_for_student('Jan','Kowalski',1)
    diary.add_student(Student('Jan','Wozniak'))
    diary.add_grade_for_student('Jan', 'Wozniak',5)
    print(diary.get_students_grades('Jan','Kowalski'))

    print(diary.get_students_average())

    print(diary.get_student_average('Jan','Wozniak'))