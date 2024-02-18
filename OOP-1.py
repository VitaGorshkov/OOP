class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}



    def __lt__(self, other):
            return self.avg_grade()  < other.avg_grade()
    

    def avg_grade(self):
        for course in self.grades.values():
            return(sum(course)/len(course))
    

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecturers:
                lecturer.grades_lecturers[course] += [grade]
            else:
                lecturer.grades_lecturers[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grade()} \
        \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершёные курсы: {', '.join(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturers = {}
    def avg_grades(self):
            for course in self.grades_lecturers.values():
                return(sum(course)/len(course))
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grades()}'

    def __lt__(self, other):
            return self.avg_grades()  < other.avg_grades()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
    


    

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']


cool_student = Student('Nome', 'Guddy', 'Gaga')
cool_student.courses_in_progress += ['Python']
cool_student.courses_in_progress += ['Git']
cool_student.finished_courses += ['Хурум бурум']

cool_lecturer = Lecturer('Sooome', 'Buddyoo')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

best_student.rate_lecturer(cool_lecturer, 'Python', 15)
best_student.rate_lecturer(cool_lecturer, 'Git', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)

cool_student.rate_lecturer(cool_lecturer, 'Python', 15)
cool_student.rate_lecturer(cool_lecturer, 'Git', 10)
cool_student.rate_lecturer(cool_lecturer, 'Python', 59)
 
cool_reviewer.rate_hw(best_student, 'Python', 500)
cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Python',10)

cool_reviewer.rate_hw(cool_student, 'Python', 30)
cool_reviewer.rate_hw(cool_student, 'Git', 15)
cool_reviewer.rate_hw(cool_student, 'Python',300)




print(cool_reviewer)

print(cool_lecturer)

print(best_student)

print(cool_student)

study_list = [best_student, cool_student]

def avg_grages_study(study_list, course):
    grade = []
    for stady in study_list:
        for courses in stady.grades.keys():
            if course == courses:
                grade.append(stady.avg_grade())


    res = sum(grade)/len(grade)

    return res


print(avg_grages_study(study_list, 'Python'))


lectory_list = [cool_lecturer]

def avg_grages_lectory(lectory_list, course):
    grade = []
    for lector in lectory_list:
        for courses in lector.grades_lecturers.keys():
            if course == courses:
                grade.append(lector.avg_grades())


    res = sum(grade)/len(grade)

    return res

print(avg_grages_lectory(lectory_list, 'Python'))
