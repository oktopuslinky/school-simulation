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

class MenuController():
    def __init__(self):
        self.teacher_list = list()
        self.student_list = list()
        self.course_list = list()

    def run(self):
        pass

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
        pass
    
    def redirect_user(self):
        pass

    def quit(self):
        pass