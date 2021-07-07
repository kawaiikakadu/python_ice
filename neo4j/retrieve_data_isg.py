import openpyxl
from Python_class import *
from retrieve_data import *


def test_project(projects, project):
    for p in projects:
        if p.project_name == project:
            return True
    return False


def get_project_index(projects, project):
    for p in projects:
        if p.project_name == project:
            return projects.index(p)


def check_sherpa(project, sherpa):
    for s in project.sherpas:
        if s.human.lastname == sherpa.split(" ")[0] and s.human.firstname == sherpa.split(" ")[1]:
            return True
    return False


def parse_lille(projects):
    wb = openpyxl.load_workbook("ressources/effectif_campus.xlsx")
    sheet_lille = wb["ISG_Lille"]

    row = sheet_lille.max_row
    col = sheet_lille.max_column

    for i in range(2, row + 1):
        current_project = ''
        index = 0
        sherpa1 = Sherpa()
        sherpa2 = Sherpa()
        student = Pioupiou()
        for j in range(3, col - 2):
            if (j == 3):
                student.human.lastname = sheet_lille.cell(i, j).value
            if (j == 4):
                student.human.firstname = sheet_lille.cell(i, j).value
            if (j == 5):
                student.human.email = sheet_lille.cell(i, j).value
            if (j == 6):
                student.team = sheet_lille.cell(i, j).value
            if (j == 7):
                if not test_project(projects, sheet_lille.cell(i, j).value):
                    project = Project()
                    project.project_name = sheet_lille.cell(i, j).value
                    projects.append(project)
                index = get_project_index(projects, sheet_lille.cell(i, j).value)
                student.campus = "LILLE"
                projects[index].students.append(student)
                if (sheet_lille.cell(i, j).value != current_project):
                    current_project = sheet_lille.cell(i, j).value
            if (j == 8):
                sherpa1.human.lastname = sheet_lille.cell(i, j).value.split(" ")[0]
                sherpa1.human.firstname = sheet_lille.cell(i, j).value.split(" ")[1]
                if not check_sherpa(projects[index], sheet_lille.cell(i, j).value):
                    sherpa1.campus = "LILLE"
                    projects[index].sherpas.append(sherpa1)
            if (j == 9):
                sherpa2.human.lastname = sheet_lille.cell(i, j).value.split(" ")[0]
                sherpa2.human.firstname = sheet_lille.cell(i, j).value.split(" ")[1]
                if not check_sherpa(projects[index], sheet_lille.cell(i, j).value):
                    sherpa2.campus = "LILLE"
                    projects[index].sherpas.append(sherpa2)
            if (j == 10):
                student.mission = sheet_lille.cell(i, j).value
                sherpa1.mission = sheet_lille.cell(i , j).value
                sherpa2.mission = sheet_lille.cell(i , j).value
    return projects

def print_projects(projects):
    for project in projects:
        print(project.project_name)
        for sherpa in project.sherpas:
            print(sherpa.human.firstname)
        for student in project.students:
            print(student.human.firstname)

if __name__ == '__main__':
    file = "ressources/Liste leads.csv"
    # projects list
    p_list = create_project_list(read_csv(file))
    print_projects(parse_lille(p_list))
