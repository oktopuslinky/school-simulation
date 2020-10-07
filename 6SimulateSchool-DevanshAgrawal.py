import sys

class Person:
    def __init__(self):
        self.name = ""


class Teacher(Person):
    def __init__(self):
        self.students = list()
        self.schedule = list()

class Student(Person):
    def __init__(self):
        self.teachers = list()
        self.schedule = list()

class TakeInput():
    def __init__(self, input_type, input_disp_text):
        self.input_type = input_type
        self.input_disp_text = input_disp_text()
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
            while input_valid is False:
                try:
                    user_input = str(input(self.input_disp_text + " (Y/N): "))
                    if user_input is not None and user_input in possible_values:
                        break
                except:
                    print("Please try again.")
            
            self.the_user_input = user_input
            return
            
class MenuController():
    def __init__(self):
        self.teacher_list = list()
        self.student_list = list()
        self.course_list = list()
        self.done = False

    def run(self):
        print("Running")
        
        while self.done is False:
            self.disp_action_menu()
            possible_choices = [1,2,3,4,5,6]

    def add_course(self):
        pass
    
    def add_person(self):
        #for both teachers and students
        pass

    def remove_person(self):
        pass

    def assign_course(self):
        pass

    def unassign_course(self):
        pass

    def disp_courses(self):
        pass

    def disp_action_menu(self):
        print(
            '''
            Welcome to the school simulation!

            1) Add a course to the system
            2) Add a person (teacher or student)
            3) Remove a person (teacher or student)
            4) Assign a course
            5) Unassign a course
            6) Quit
            '''
        )
    
    def redirect_user(self):
        pass

    def quit(self):
        print("Have a nice day.")
        sys.exit()

the_menu = MenuController()
the_menu.run()