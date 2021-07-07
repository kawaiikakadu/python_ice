import openpyxl
from Python_class import *

def parse_lille(projects):
    wb = openpyxl.load_workbook("ressources/effectif_campus.xlsx")
    sheet_lille = wb["ISG_Lille"]

    row = sheet_lille.max_row
    col = sheet_lille.max_column
    student_list = []
    sherpas_list = []
    for i in range(2,row + 1):
        current_sherpa1 = ''
        sherpa1 = Sherpa()
        sherpa2 = Sherpa()
        student = Pioupiou()
        for j in range (3,col - 2):
            print(sheet_lille.cell(i, j).value)
            if (j == 3):
                student.human.firstname = sheet_lille.cell(i,j).value
            if (j == 4):
                student.human.lastname = sheet_lille.cell(i,j).value
            if (j == 5):
                student.human.email = sheet_lille.cell(i,j).value
            if (j == 6):
                index = projects.index(sheet_lille.cell(i,j).value)
                projects[index].students.append(student)
            if (j == 7):
                sherpa1.human.firstname = sheet_lille.cell(i,j).value.split(" ")[0]
                sherpa1.human.lastname = sheet_lille.cell(i, j).value.split(" ")[1]
            if (j == 8):
                sherpa2.human.firstname = sheet_lille.cell(i, j).value.split(" ")[0]
                sherpa2.human.lastname = sheet_lille.cell(i, j).value.split(" ")[1]
            if (j == 9):
                student.mission = sheet_lille.cell(i, j).value
        print('\n')

if __name__ == '__main__':
    parse_lille()

