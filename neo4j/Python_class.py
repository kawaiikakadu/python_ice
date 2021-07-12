class Human:
    def __init__(self):
        self.firstname = ''
        self.lastname = ''
        self.school = ''
        self.number = ''
        self.email = ''


class Binome:
    def __init__(self):
        self.human1 = Human()
        self.human2 = Human()
        self.human1.school = "EPITA"
        self.human2.school = "EPITA"


class Pioupiou:
    def __init__(self):
        self.human = Human()
        self.human.school = "ISG"
        self.campus = ''
        self.team = ''
        self.mission = ''


class Sherpa:
    def __init__(self):
        self.human = Human()
        self.human.school = "ISG"
        self.campus = ''
        self.mission = ''


class Project:
    def __init__(self):
        self.project_name = ''
        self.binome = Binome()
        self.partenaire = Partenaire()
        self.sherpas = []
        self.students = []


class Partenaire:
    def __init__(self):
        self.firstname = ''
        self.lastname = ''
        self.job = ''
        self.email = ''
        self.number = ''
