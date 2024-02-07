class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def avg_grade(self):
        return(sum(map(sum, self.grades.values()))/len(self.grades))
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
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
        return(sum(map(sum, self.grades_lecturers.values()))/len(self.grades_lecturers))
    
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()}'

    

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


cool_student = Student('Nome', 'Guddy', 'Gaga')

cool_lecturer = Lecturer('Sooome', 'Buddyoo')
cool_lecturer.courses_attached += ['Python']

 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 5)
cool_reviewer.rate_hw(best_student, 'Python', 2)

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Git', 10)
best_student.rate_lecturer(cool_lecturer, 'Java', 10)



print(cool_reviewer)

print(cool_lecturer)

print(best_student)






