from enum import IntEnum
from statistics import mean


class Grade(IntEnum):
    F = 1
    F_PLUS = 2
    E = 3
    E_PLUS = 4
    D = 5
    D_PLUS = 6
    C = 7
    C_PLUS = 8
    B = 9
    B_PLUS = 10
    A = 11

    def __str__(self):
        if '_PLUS' in self.name:
            return self.name.replace('_PLUS', "+")
        else:
            return self.name

    def __repr__(self):
        return self.__str__()


class GradeLog:
    def __init__(self):
        self.grades = []

    def get_grade_average(self):
        grade_average = round(mean(self.grades))
        grade_average = Grade(grade_average)
        return grade_average

    def add_grade(self, grade):
        self.grades.append(grade)

    def __str__(self):
        return str(self.grades)


if __name__ == "__main__":
    grade_log = GradeLog()
    while True:
        print(grade_log)
        operacja_user = input('podaj operacej do wykoanania | add | average grades = avr | exit |\n> ')
        if operacja_user.lower() == 'add':
            ocena_add = input('ocena do dodania A,B_PLUS,B,C_PLUS,C,D_PLUS,D,E_PLUS,E,F_PLUS,F\n> ')
            if ocena_add.lower() == 'a':
                grade_log.add_grade(Grade.A)
            elif ocena_add.lower() == 'b_plus':
                grade_log.add_grade(Grade.B_PLUS)
            elif ocena_add.lower() == 'b':
                grade_log.add_grade(Grade.B)
            elif ocena_add.lower() == 'c_plus':
                grade_log.add_grade(Grade.C_PLUS)
            elif ocena_add.lower() == 'c':
                grade_log.add_grade(Grade.C)
            elif ocena_add.lower() == 'd_plus':
                grade_log.add_grade(Grade.D_PLUS)
            elif ocena_add.lower() == 'd':
                grade_log.add_grade(Grade.D)
            elif ocena_add.lower() == 'e_plus':
                grade_log.add_grade(Grade.E_PLUS)
            elif ocena_add.lower() == 'e':
                grade_log.add_grade(Grade.E)
            elif ocena_add.lower() == 'f_plus':
                grade_log.add_grade(Grade.F_PLUS)
            elif ocena_add.lower() == 'f':
                grade_log.add_grade(Grade.F)

        elif operacja_user.lower() == 'avr':
            print('average grades: ', grade_log.get_grade_average())
        elif operacja_user.lower() == 'exit':
            break