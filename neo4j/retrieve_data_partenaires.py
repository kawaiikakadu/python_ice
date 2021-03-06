from retrieve_data_isg import *


# function to parse the sheet in the clients excel
def parse_partenaire(projects, sheet):
    """
    Function to parse the clients excel file

    :param projects: list of the projects
    :param sheet: excel sheet the clients are on
    :return: list of the projects given in argument
    """
    row = count_row(sheet)
    col = sheet.max_column
    for i in range(2, row + 1):
        index = 0
        partenaire = Partenaire()
        for j in range(1, col + 1):
            if j == 1:
                index = get_project_index(projects, sheet.cell(i, j).value)
            if j == 2:
                partenaire.lastname = sheet.cell(i, j).value
            if j == 3:
                partenaire.firstname = sheet.cell(i, j).value
            if j == 4:
                partenaire.job = sheet.cell(i, j).value
            if j == 5:
                partenaire.email = sheet.cell(i, j).value
            if j == 6:
                partenaire.number = sheet.cell(i, j).value
        projects[index].partenaire = partenaire
    return projects


# function that calls the parsing function
def parse_excel_partenaires(projects):
    """
    Function to parse the clients excel
    :param projects: list of the projects
    :return: list of the projects
    """
    wb = openpyxl.load_workbook("ressources/2021 PLANETE SOLIDAIRE - CONTACTS PARTENAIRES.xlsx")
    sheet = wb.worksheets[0]
    parse_partenaire(projects, sheet)
    return projects
