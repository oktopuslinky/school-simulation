import sys



class Item:
    def __init__(self, name=None):
        self.name = name

class Course(Item):
    def __init__(self, name=None, teachers=None, students=None):
        super().__init__(name)
        self.teachers = teachers
        self.students = students

        self.identity = {"Name": self.name, "Teachers": self.teachers, "Students": self.students}

class Teacher(Item):
    def __init__(self, name=None, students=None):
        super().__init__(name)
        self.students = students

        self.identity = {"Name": self.name, "Students": self.students}

class Student(Item):
    def __init__(self, name=None, teachers=None):
        super().__init__(name)
        self.teachers = teachers

        self.identity = {"Name": self.name, "Teachers": self.teachers}

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

            elif the_type == "dict":
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
        course_exists = self.search("list", course_name, self.course_list)
        if course_exists:
            print("This course already exists in the system.")
            print("You will be redirected to the main menu.")
        else:
            self.course_list.append(course_name)
            print(self.course_list)
    
    def add_person(self):
        #Create person and append to list
        print("Is this person a student or a teacher?")
        person_type = TakeInput("str", 'Input "student" or "teacher"').the_user_input
        person_name = input("What is the name of the new person?: ")

        if person_type == "student" or person_type == "Student":
            student_exists = self.search("dict", person_name, self.student_list, "Name")
            if student_exists:
                print("This student already exists in the system.")
            else:
                new_person = Student(person_name, []).identity
                print(new_person)
                self.student_list.append(new_person)
                print(self.student_list)

        elif person_type == "teacher" or person_type == "Teacher":
            teacher_exists = self.search("dict", person_name, self.teacher_list, "Name")
            if teacher_exists:
                print("This student already exists in the system.")
                print("")
            else:
                new_person = Teacher(person_name, []).identity
                print(new_person)
                self.teacher_list.append(new_person)
                print(self.teacher_list)

    def remove_course(self):
        the_course = input("What course do you want to remove?: ")
        course_exists = self.search("list", the_course, self.course_list)
        if course_exists:
            #remove course from course, students, and teachers lists.
            pass
        
        else:
            print("You will be redirected to the main menu.")

    def remove_person(self):
        pass

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