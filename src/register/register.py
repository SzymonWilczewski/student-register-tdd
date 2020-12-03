class Register:
    def __init__(self):
        self.db = [
            Student("dc338aff-d851-4c08-a319-ed4e18640b36", "Andrzej", "Kowalski", 1,
                    [["Język polski", [1, 1.5, 3, 2.5, 5]], ["Matematyka", [5, 4.5, 5.5, 6, 4, 6]],
                     ["Angielski", [5, 5, 5.5, 6, 4, 6]]],
                    ["Uczeń jadł podczas zajęć", "Uczeń nie wykonywał poleceń nauczyciela"]),
            Student("f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", 1,
                    [["Język polski", [4, 3, 4.5, 5, 6]], ["Matematyka", [5, 4.5, 5.5, 6, 4, 6]],
                     ["Angielski", [4, 4.5, 4.5, 3, 5.5, 6]]], []),
            Student("cc6d68fe-d2b0-4ee9-b832-dcf31b9e8752", "Ireneusz", "Mazur", 2,
                    [["Język polski", [3, 2, 3.5, 1.5, 4]], ["Matematyka", [5, 4, 5, 6, 4.5, 5]],
                     ["Angielski", [3, 4, 1, 5.5, 4, 5]]], ["Uczeń nagminnie spóźnia się na lekcje"]),
            Student("8ffdf006-536b-47d4-b074-cada820f67e1", "Milena", "Górecka", 2,
                    [["Język polski", [4, 4, 4.5, 3.5, 5]], ["Matematyka", [4, 4, 5, 3, 5, 5]],
                     ["Angielski", [5, 4, 6, 6, 5.5, 6]]], []),
            Student("36a158b5-4ea3-4c5b-a82f-141fea0eae44", "Oliwia", "Kowalczyk", 3,
                    [["Język polski", [5, 3, 3.5, 4.5, 5]], ["Matematyka", [2, 3.5, 2.5, 3, 3, 4.5]],
                     ["Angielski", [4.5, 4, 5.5, 3, 4.5, 6]]], [])
        ]

    def add_student(self, id_, first_name, last_name, year):
        self.db.append(Student(id_, first_name, last_name, year))
        return [id_, first_name, last_name, year]

    def edit_student(self, id_, new_first_name=None, new_last_name=None, new_year=None):
        result = []
        for student in self.db:
            if student.id_ == id_:
                if new_first_name is not None:
                    student.first_name = new_first_name
                    result.append(new_first_name)
                if new_last_name is not None:
                    student.last_name = new_last_name
                    result.append(new_last_name)
                if new_year is not None:
                    student.year = new_year
                    result.append(new_year)
                return result

    def remove_student(self, id_):
        for student in self.db:
            if student.id_ == id_:
                self.db.remove(student)
                return id_

    def student_id(self, first_name, last_name):
        return [student.id_ for student in self.db
                if student.first_name == first_name and student.last_name == last_name]


class Student:
    def __init__(self, id_, first_name, last_name, year, subjects=None, comments=None):
        if subjects is None:
            subjects = []
        if comments is None:
            comments = []
        self.id_ = id_
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.subjects = subjects
        self.comments = comments
