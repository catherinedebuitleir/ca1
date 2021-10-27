# student_list = []
# max_list = 30
#
#
# print(f"{max_list} students currently registered")
# while len(student_list) < max_list:
#     student_name = input("Please enter a name?:")
#     student_list.append(student_name)
#     max_list = max_list - 1
#     print(f"{max_list} students currently registered")
#
#
# if len(student_list) == max_list:
#     print(student_list)

class Student:
    firstName = ""
    LastName = ""
    Student_Number = ""
    Email = ""

    def set_student_info(self, fname, lname, number, email):
        self.firstName = fname
        self.LastName = lname
        self.Student_Number = number
        self.Email = email


student1 = Student()
tname = input("whats your name?")
tlastname = input("whats your lastname?")
tnumber = input("whats your number")
temail = input("whats your email?")
student1.set_student_info(tname, tlastname, tnumber, temail)
print(student1.firstName)

# Student_1 = Student()
# Student_1.firstName = "John"
# Student_1.LastName = "Butler"
# Student_1.Student_Number = "12233"
# Student_1.Email = "j.butler@gmail.com"
#
# Student_2 = Student()
# Student_2.firstName = "Aoife"
# Student_2.LastName = "Butler"
# Student_2.Student_Number = "12233"
# Student_2.Email = "a.butler@gmail.com"
#
# Student_3 = Student()
# Student_3.firstName = "Catherine"
# Student_3.LastName = "Butler"
# Student_3.Student_Number = "22233"
# Student_3.Email = "c.butler@gmail.com"
#
# Student_4 = Student()
# Student_4.firstName = "Sarah"
# Student_4.LastName = "Butler"
# Student_4.Student_Number = "1333"
# Student_4.Email = "cs.butler@gmail.com"
#
# print(f'{Student_3.LastName} {Student_3.firstName} is the name of my grandfather')
#
#
# class Course:
#     course_title = ""
#     course_code = ""
#     course_chair = ""
#     student_list = []
#
#
# courseObject = Course()
#
#
# def get_course_title(ask_course_title):
#     course = input(ask_course_title)
#     return course
#
#
# def get_course_code(ask_course_code):
#     course = input(ask_course_code)
#     return course
#
#
# def get_student_list(ask_student_list):
#     slit = input(ask_student_list)
#     courseObject.student_list.append(slit)
#     return slit
#
#
# def display_student_list():
#     print(courseObject.student_list)
#
#
# courseTitle = get_course_title("whats course title?")
# print(courseTitle)
#
# courseCode = get_course_code("whats course code?")
# print(courseCode)
#
# studentlist = get_student_list("whats your name?")
# print(studentlist)
#
# studentlist = get_student_list("whats your name?")
# print(studentlist)
#
# display_student_list()
