class Human:
    """
    A class to represent a human (non-students from ISG).

    ...

    Attributes
    ----------
    firstname : str
        first name of the human
    lastname : str
        family name of the human
    school : str
        school of the human
    number : str
        telephone number of the human
    email : str
        email of the human

    Methods
    -------
    None
    """

    def __init__(self, firstname='', lastname='', school='', number='', email=''):
        self.firstname = firstname
        self.lastname = lastname
        self.school = school
        self.number = number
        self.email = email


class Binome:
    """
    A class to represent a binome of two EPITA students.

    ...

    Attributes
    ----------
    human1 : Human()
        leader of the binome
    human2 : Human()
        mate of the leader
    school : str
        EPITA for both students of the binome

    Methods
    -------
    None
    """

    def __init__(self):
        self.human1 = Human()
        self.human2 = Human()
        self.human1.school = "EPITA"
        self.human2.school = "EPITA"


class Pioupiou:
    """
    A class to represent a pioupiou = student from ISG.

    ...

    Attributes
    ----------
    human : Human
        human form of the pioupiou
    school : str
        ISG for each pioupiou
    campus : str
        campus of the ISG the pioupiou works at
    team : str
        number of the team the pioupiou is in
    mission : str
        mission the pioupiou works on

    Methods
    -------
    None
    """

    def __init__(self):
        self.human = Human()
        self.human.school = "ISG"
        self.campus = ''
        self.team = ''
        self.mission = ''


class Sherpa:
    """
    A class to represent a sherpa = tutor of ISG students.

    ...

    Attributes
    ----------
    human : Human()
        human form of the sherpa
    school : str
        ISG for every sherpa
    campus : str
        ISG's campus the sherpa works at
    mission : str
        mission the sherpa works on

    Methods
    -------
    None
    """

    def __init__(self):
        self.human = Human()
        self.human.school = "ISG"
        self.campus = ''
        self.mission = ''


class Partenaire:
    """
    A class to represent a partenaire.

    ...

    Attributes
    ----------
    firstname : str
        first name of the partenaire
    lastname : str
        family name of the partenaire
    job : str
        job of the partenaire
    number : str
        telephone number of the partenaire
    email : str
        email of the partenaire

    Methods
    -------
    None
    """

    def __init__(self):
        self.firstname = ''
        self.lastname = ''
        self.job = ''
        self.email = ''
        self.number = ''


class Project:
    """
    A class to represent a project

    ...

    Attributes
    ----------
    project_name : str
        name of the project
    binome : Binome()
        EPITA's binome leading the project
    partenaire : Partenaire()
        partenaire the project is for
    sherpas : list
        list of the sherpas working on the project
    students: list
        list of the students working on the project

    Methods
    -------
    None
    """

    def __init__(self):
        self.project_name = ''
        self.binome = Binome()
        self.partenaire = Partenaire()
        self.sherpas = []
        self.students = []
