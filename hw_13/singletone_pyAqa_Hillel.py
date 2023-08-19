from hw_13.hw_13_singletone import singleton

@singleton
class PythonAqaHillel:
    def __init__(self, course_name:str, teacher:str, classes:int):
        self.course_name = course_name
        self.teacher = teacher
        self.classes = classes
        self.best = True


pyAqa_course_1 = PythonAqaHillel('QA Automation - Python', 'Oleh Vershynin', 32)
pyAqa_course_2 = PythonAqaHillel('AQA - Python', 'O. Vershynin', 32)
print(pyAqa_course_1.teacher)
print(pyAqa_course_2.teacher)
del pyAqa_course_1
del pyAqa_course_2
pyAqa_course_3 = PythonAqaHillel()
print(pyAqa_course_3.course_name)