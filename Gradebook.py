from model.enrollment import Enrollment
from model.course import Course
from model.student import Student
from model.transcript import Transcript

from data.school_db import SchoolDB
from data.school_initializer import SchoolInitializer

class Gradebook:

    def __init__(self, school_db):

        self.school_db = school_db#.school_initializer
#                       school_initializer arg ^ (?)
        self.enrollments = school_db.enrollments
        self.students = school_db.school_initializer.students
##        self.courses = school_db.school_initializer.courses
##        self.professors = school_db.school_initializer.professors
#       assign from schhol initializer to class atributes ^
      

    def main(self):

        option = ''

        while option != 'e':
            print()
            option = self.__main_main()

            if option == '1':

                enroll_id = int(input("Enter Enroll ID: "))

                if enroll_id in self.enrollments:
                    enroll = self.enrollments.get(enroll_id)

                    grade = input("Enter grade: ")
                    enroll.grade = grade
                else:
                    print("Sorry, Enroll ID does not exist")

            elif option == '2':

                student_id = int(input("Enter Stduent ID: "))

                if student_id in self.students:
                    student = self.students.get(student_id)
                    transcript.print_transcript(student)

                else:
                    print("Sorry, Student ID does not exist")

            elif option == '3':

                for enrollment in self.enrollments.values():
                    enrollment.print_record()#print records
                    
            elif option == '4':

                self.school_db.save_data()

            print()
##        keep_going = 'y'
##        keep_going = input("press 'y'")
##        while keep_going == 'y':
##        
##            enroll_id = int(input("Enter enrollment ID: "))
##            grade = input("Enter grade: ")
##
##            e = self.enrollments.get(enroll_id)
##
##            e.grade = grade
##            
##            keep_going = input("To keep going press 'y'")
##            
##        for key, enroll in self.enrollments.items():
##                print(key, enroll.grade, enroll.student.first_name, enroll.course.title)

    def __main_main(self):

        print("Academic Main Menu")
        print()
        print("1) Update Grade")
        print("2) Print Student GPA")
        print("3) Print All Enrollments")
        print("4) Save Data")
        print()
        return input("Enter 1, 2, 3, 4 or e to exit: ")
        


db = SchoolDB(SchoolInitializer())
Gradebook = Gradebook(db)
Gradebook.main()
