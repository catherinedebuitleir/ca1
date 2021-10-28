# create course class to storehe student list which will get the length of the list so we can stop the loop.
class Course:
    courseName = "Postgraduate in fundamentals of Data Science(Conversion)"
    courseNumber = "TU257"
    student_list = []
    max_list = 30

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
        print(
            f'{self.firstName},{self.lastName},{self.dob},{self.address},{self.email},{self.mobile},{self.Student_Number},{self.status}')

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
student21 = Student()
student22 = Student()
student23 = Student()
student24 = Student()
student25 = Student()
student26 = Student()
student27 = Student()
student28 = Student()
student29 = Student()
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
student21.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student22.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student23.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student24.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student25.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student26.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student27.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student28.set_student_info("John", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
student29.set_student_info("Britney", "Smith", "25/05/1990", "Dublin", "f@email.com", "03212222", "c2411333", "RE")
course_info = Course()

print(course_info.student_list)
course_tuple = (student1.Student_Number, student2.Student_Number, student3.Student_Number, student4.Student_Number,student5.Student_Number, student6.Student_Number, student7.Student_Number,student8.Student_Number, student9.Student_Number, student10.Student_Number, student11.Student_Number, student12.Student_Number,student13.Student_Number, student14.Student_Number, student15.Student_Number, student16.Student_Number,student17.Student_Number, student18.Student_Number, student19.Student_Number, student20.Student_Number, student21.Student_Number, student22.Student_Number, student23.Student_Number, student24.Student_Number, student25.Student_Number, student26.Student_Number, student27.Student_Number,student28.Student_Number,student29.Student_Number)
course_info.student_list.extend(course_tuple)
print(course_info.student_list)
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
