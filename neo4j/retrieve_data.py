import csv


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


class Sherpa:
    def __init__(self):
        self.firstname = ''
        self.lastname = ''
        self.school = "ISG"
        self.email = ''
        self.campus = ''


class Project:
    def __init__(self):
        self.project_name = ''
        self.binome = Binome()
        self.sherpas = [Sherpa()]


# read a csv file and return a list of lines
def read_csv(file):
    content = []
    with open(file, newline='', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            content.append(row)
        # for line in content:
        #   print(line)
        return content


def create_project_list(content):
    project_list = []
    for i in range(1, len(content)):
        curr_proj = Project()
        for j in range(len(content[0])):
            category = content[0][j]
            if category == "Projet":
                curr_proj.project_name = content[i][j]
            elif category == "Leader":
                curr_proj.binome.human1.firstname = content[i][j].split(" ")[0]
                curr_proj.binome.human1.lastname = content[i][j].split(" ")[1]
            elif category == "Binôme":
                curr_proj.binome.human2.firstname = content[i][j].split(" ")[0]
                curr_proj.binome.human2.lastname = content[i][j].split(" ")[1]
            elif category == "Contact Leader":
                curr_proj.binome.human1.email = content[i][j]
            elif category == "Contact Binôme":
                curr_proj.binome.human2.email = content[i][j]
            elif category == "Téléphone Leader":
                curr_proj.binome.human1.number = content[i][j]
            elif category == "Téléphone Binôme":
                curr_proj.binome.human2.number = content[i][j]
        project_list.append(curr_proj)
    return project_list


# quick print to see if the nodes are empty or not
def print_project_list(p_list):
    for project in p_list:
        print(project.project_name, project.binome.human1.firstname, project.binome.human1.lastname,
              project.binome.human1.school)
