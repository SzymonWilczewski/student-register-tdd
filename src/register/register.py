class Register:
    def __init__(self):
        pass


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
