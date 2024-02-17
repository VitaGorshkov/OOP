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
        for course in self.grades.keys():
            return(sum(self.grades[course])/len(self.grades[course]))
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

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
    def avg_grade(self):
            for course in self.grades_lecturers.keys():
                return(sum(self.grades_lecturers[course])/len(self.grades_lecturers[course]))
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()}'

    def __lt__(self, other):
            return self.avg_grade()  < other.avg_grade()

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

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Git', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 5)

cool_student.rate_lecturer(cool_lecturer, 'Python', 10)
cool_student.rate_lecturer(cool_lecturer, 'Git', 10)
cool_student.rate_lecturer(cool_lecturer, 'Python', 5)
 
cool_reviewer.rate_hw(best_student, 'Python', 20)
cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Python',10)

cool_reviewer.rate_hw(cool_student, 'Python', 15)
cool_reviewer.rate_hw(cool_student, 'Git', 5)
cool_reviewer.rate_hw(cool_student, 'Python',5)




print(cool_reviewer)

print(cool_lecturer)

print(best_student)







