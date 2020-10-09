import sys

class Item:
    def __init__(self, name=None):
        self.name = name
'''
** DATA STRUCTURE **

courses=[
    {
        Course: "courseName", 
        Students: [students], 
        Teachers: [teachers]
    }, 
    ETC
]

students[
    {
        Name: "name",
        Courses: {
            Course1: Teacher1,
            course2: teacher2,
            etc
        }
    },
    ETC
]

teachers[
    {
        Name: "name",
        Courses: {
            course1: [students]
            course2: [students]
        }
    }
]
'''
class Course(Item):
    def __init__(self, name):
        super().__init__(name)
        self.teachers = []
        self.students = []

        self.identity = {"Course": self.name, "Teachers": self.teachers, "Students": self.students}

class Student(Item):
    def __init__(self, name):
        super().__init__(name)
        self.teachers = []

        self.identity = {"Name": self.name, "Courses": {}}

class Teacher(Item):
    def __init__(self, name):
        super().__init__(name)
        self.students = []

        self.identity = {"Name": self.name, "Courses": {}}

class TakeInput():
    def __init__(self, input_type, input_disp_text):
        self.input_type = input_type
        self.input_disp_text = input_disp_text
        self.the_user_input = None
        self.take_input()

    def take_input(self):
        input_valid = False
        if self.input_type == "int":
            while input_valid is False:
                try:
                    user_input = int(input(self.input_disp_text + ": "))
                    if user_input is not None:
                        input_valid = True
                except:
                    print("Please try again.")
            
            self.the_user_input = user_input
            return

        if self.input_type == "verify":
            possible_values = ["Y", "N", "y", "n"]
            input_valid = False
            while input_valid is False:
                try:
                    user_input = str(input(self.input_disp_text + " (Y/N): "))
                    if user_input is not None and user_input in possible_values:
                        break
                except:
                    print("Please try again.")
            
            self.the_user_input = user_input
            return
        
        if self.input_type == "str":
            input_valid = False
            while input_valid is False:
                try:
                    user_input = str(input(self.input_disp_text + ": "))
                    if user_input is not None:
                        input_valid = True
                except:
                    print("Please try again.")

            self.the_user_input = user_input
            return

class MenuController():
    def __init__(self):
        #[{name: "", courses: ["", ""], students: ["", ""]}]
        self.teacher_list = list()

        #[{name: "", courses: ["", ""], teachers: ["",""]}]
        self.student_list = list()

        #["courseName1", etc]
        self.course_list = list()
        self.done = False

        self.user_choice = 0

    def search(self, the_type=None, the_item=None, the_list=None, the_key=None):
        for an_item in the_list:
            if the_type == "list":
                if an_item == the_item:
                    return True

            elif the_type == "dict_in_list":
                if an_item[the_key] == the_item:
                    return True

    def run(self):
        print("Running")
        
        while self.done is False:
            self.disp_action_menu()
            possible_choices = [1,2,3,4,5,6,7]

            self.user_choice = TakeInput("int", "Insert Choice").the_user_input
            self.redirect_user()

    def add_course(self):
        course_name = input("What is the name of the new course?")
        course_exists = self.search("dict_in_list", course_name, self.course_list, "Course")
        if course_exists:
            print("This course already exists in the system.")
            print("You will be redirected to the main menu.")
        else:
            new_course = Course(course_name)
            self.course_list.append(new_course.identity)
            print(self.course_list)
    
    def add_person(self):
        #Create person and append to list
        print("Is this person a student or a teacher?")
        person_valid = False
        possible_values = ["s", "S", "t", "T"]
        while person_valid is False:
            person_type = TakeInput("str", 'Input "s" for student or "t" for teacher').the_user_input
            if person_type in possible_values:
                person_valid = True

        person_name = input("What is the name of the new person?: ")

        if person_type == "s" or person_type == "S":
            student_exists = self.search("dict_in_list", person_name, self.student_list, "Name")
            if student_exists:
                print("This student already exists in the system.")
            else:
                new_person = Student(person_name).identity
                print(new_person)
                self.student_list.append(new_person)
                print(self.student_list)

        elif person_type == "t" or person_type == "T":
            teacher_exists = self.search("dict_in_list", person_name, self.teacher_list, "Name")
            if teacher_exists:
                print("This student already exists in the system.")
                print("")
            else:
                new_person = Teacher(person_name).identity
                print(new_person)
                self.teacher_list.append(new_person)
                print(self.teacher_list)

    def remove_course(self):
        the_course = input("What course do you want to remove?: ")
        course_exists = self.search("dict_in_list", the_course, self.course_list, "Course")
        if course_exists:
            #remove course from course, students, and teachers lists.
            for student in self.student_list:
                student_courses = student["Courses"]
                for course in student_courses:
                    if course == the_course:
                        student_courses.pop(the_course)
                        print(self.student_list)
            
            for a_course in self.course_list:
                if a_course["Course"] == the_course:
                    self.course_list.remove(a_course)
            
            for teacher in self.teacher_list:
                teacher_courses = teacher["Courses"]
                for course in teacher_courses:
                    if course == the_course:
                        teacher_courses.pop(the_course)
                        print(self.teacher_list)
            
            print("The course has successfully been removed from the system.")

        else:
            print("You will be redirected to the main menu.")

    def remove_person(self):
        #remove person from course, student, and teacher lists
        
        person_valid = False
        possible_values = ["s", "S", "t", "T"]
        while person_valid is False:
            person_type = TakeInput("str", "Is this person a student or teacher?").the_user_input
            if person_type in possible_values:
                person_valid = True

        the_person = input("What is the name of the person?: ")
        if person_type == "s" or person_type == "S":
            #remove the student from all lists
            student_exists = self.search("dict_in_list", the_person, self.student_list, "Name")
            if student_exists:
                #remove student from all lists
                for a_course in self.course_list:
                    students_in_course = a_course["Students"]
                    for a_student in students_in_course:
                        if a_student == the_person:
                            students_in_course.remove(the_person)
                
                for student in self.student_list:
                    if student["Name"] == the_person:
                        self.student_list.remove(student)

                for teacher in self.teacher_list:
                    courses = teacher["Courses"]
                    for course_key in courses:
                        students_in_course = courses[course_key]
                        for student in students_in_course:
                            if student == the_person:
                                students_in_course.remove(student)
                print("Student", the_person, "has been removed.")
            else:
                print("This student does not exist in the system.")

        elif person_type == "t" or person_type == "T":
            #remove the teacher from all lists.
            teacher_exists = self.search("dict_in_list", the_person, self.teacher_list, "Name")
            if teacher_exists:
                for a_course in self.course_list:
                    teachers_in_course = a_course["Teachers"]
                    for a_teacher in teachers_in_course:
                        if a_teacher == the_person:
                            teachers_in_course.remove(the_person)
                
                for student in self.student_list:
                    the_course_list = student["Courses"]
                    for course_key in the_course_list:
                        if the_course_list[course_key] == the_person:
                            the_course_list.pop(course_key)
                
                for teacher in self.teacher_list:
                    if teacher["Name"] == the_person:
                        self.teacher_list.remove(teacher)
                
                print("Teacher", the_person, "has been removed.")

            else:
                print("This teacher does not exist in the system.")
        

    def assign_course(self):
        pass

    def unassign_course(self):
        pass

    def disp_info(self):
        print("Courses:")
        print(self.course_list)

        print("Teachers:")
        print(self.teacher_list)

        print("Students:")
        print(self.student_list)

    def disp_action_menu(self):
        print(
            '''
            Welcome to the school simulation!

            1) Add a course to the system
            2) Add a person (teacher or student)
            3) Remove a course from the system
            4) Remove a person (teacher or student)
            5) Assign a course
            6) Unassign a course
            7) Display the courses, teachers, and students
            8) Quit
            '''
        )
    
    def redirect_user(self):
        if self.user_choice == 1:
            self.add_course()

        elif self.user_choice == 2:
            self.add_person()

        elif self.user_choice == 3:
            self.remove_course()

        elif self.user_choice == 4:
            self.remove_person()

        elif self.user_choice == 5:
            self.assign_course()

        elif self.user_choice == 6:
            self.unassign_course()
        
        elif self.user_choice == 7:
            self.disp_info()
        
        elif self.user_choice == 8:
            self.quit()

    def quit(self):
        print("Have a nice day.")
        sys.exit()

the_menu = MenuController()
the_menu.run()

'''
TODO:
remove_course()
remove_person()
assign_course()
unassign_course()
disp_info()
'''