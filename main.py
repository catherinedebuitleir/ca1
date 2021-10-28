# create course class
class Course:
    courseName = "Postgraduate in fundamentals of Data Science(Conversion)"
    courseNumber = "TU257"
    student_list = ["c1345223", "c1345223", "c1345223"]
    max_list = 4

    def set_course_info(self, cname, cnumber, slist, mlist):
        self.courseName = cname
        self.courseNumber = cnumber
        self.student_list = slist
        self.max_list = mlist


# create student class
class Student:
    firstName = ""
    lastName = ""
    dob = ""
    address = ""
    email = ""
    mobile = ""
    Student_Number = ""
    status = ""

    def set_student_info(self, fname, lname, dob, address, email, mobile, studentnumber, status):
        self.firstName = fname
        self.lastName = lname
        self.dob = dob
        self.address = address
        self.email = email
        self.mobile = mobile
        self.Student_Number = studentnumber
        self.status = status

    # use method for printing out the list
    def show_student_list(self):
        print(f'{self.firstName},{self.lastName},{self.dob},{self.address},{self.email},{self.mobile},{self.Student_Number},{self.status}')

        # student_array = [self.firstName, self.lastName, self.dob, self.address, self.email, self.mobile,
    #                  self.Student_Number, self.status]
    # print(student_array)


# objects created
student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()
student6 = Student()
student7 = Student()
student8 = Student()
student9 = Student()
student10 = Student()
student11 = Student()
student12 = Student()
student13 = Student()
student14 = Student()
student15 = Student()
student16 = Student()
student17 = Student()
student18 = Student()
student19 = Student()
student20 = Student()

student1.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student2.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student3.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student4.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student5.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student6.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student7.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student8.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student9.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student10.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student11.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student12.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student13.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student14.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student15.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student16.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student17.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student18.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student19.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student20.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")

course_info = Course()

studentlist_len = len(course_info.student_list)

print(f"{studentlist_len} students currently registered")
while len(course_info.student_list) < course_info.max_list:
    fname = input("whats your name?")
    lname = input("whats your lastname?")
    dob = input("whats your dob?")
    address = input("whats your address")
    email = input("whats your email?")
    mobile = input("whats your mobile?")
    studentnumber = input("whats your studentnumber?")
    status = input("whats your status?")
    student1.set_student_info(fname, lname, dob, address, email, mobile, studentnumber, status)
    course_info.student_list.append(fname)
    course_info.max_list = course_info.max_list - 1

    student1.show_student_list()
    student2.show_student_list()
    student3.show_student_list()
    student4.show_student_list()
    student5.show_student_list()
    student6.show_student_list()
    student7.show_student_list()
    student8.show_student_list()
    student9.show_student_list()
    student10.show_student_list()
    student11.show_student_list()
    student12.show_student_list()
    student13.show_student_list()
    student14.show_student_list()
    student15.show_student_list()
    student16.show_student_list()
    student17.show_student_list()
    student18.show_student_list()
    student19.show_student_list()
    student20.show_student_list()

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
