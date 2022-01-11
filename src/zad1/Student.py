from itertools import count


class Student:
    def __init__(self, name, surname, studentId):
        if type(name) != str or len(name) == 0:
            raise ValueError("Imię ucznia musi być typu string!")
        elif type(surname) != str or len(surname) == 0:
            raise ValueError("Nazwisko ucznia musi być typu string!")
        self.id = studentId
        self.name = name
        self.surname = surname


class StudentList:
    def __init__(self, students=""):
        self.students = []
        self.__auto_id = count(1, 1)
        if students:
            for student in students:
                self.students.append(student)

    def addStudent(self, name, surname):
        studentId = next(self.__auto_id)
        student = Student(name, surname, studentId)
        self.students.append(student)
        return student

    def getAllStudents(self):
        result = []
        for student in self.students:
            result.append(f"{student.name} {student.surname}")
        return result

    def getStudentById(self, num):
        if type(num) != int:
            raise ValueError("Numer musi być liczbą całkowitą!")
        elif num <= 0:
            raise ValueError("Numer musi być liczbą dodatnią!")
        for student in self.students:
            if student.id == num:
                return student
        raise Exception("Uczeń o podanym numerze nie istnieje!")

    def deleteStudentById(self, num):
        if type(num) != int or num <= 0:
            raise ValueError("Numer musi być dodatnią liczbą całkowitą!")
        elif len(self.students) < num:
            raise ValueError("Uczeń o podanym numerze nie istnieje!")
        student = self.getStudentById(num)
        self.students.remove(student)
        del student
