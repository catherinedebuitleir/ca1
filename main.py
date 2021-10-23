student_list = []
max_list = 30

while len(student_list) < max_list:
    student_name = input("Please enter a name?:")
    student_list.append(student_name)

if len(student_list) == max_list:
    print(student_list)
