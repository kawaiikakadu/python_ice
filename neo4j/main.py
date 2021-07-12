from neo4j_class import *
from retrieve_data_partenaires import *

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
db.set_connection('bolt://neo4j:password@localhost:7687')


# clear all categories of nodes in the db
def clear_db():
    humans = Human4j.nodes.all()
    for h in humans:
        h.delete()
    binomes = Binome4j.nodes.all()
    for b in binomes:
        b.delete()
    projects = Project4j.nodes.all()
    for p in projects:
        p.delete()
    sherpas = Sherpa4j.nodes.all()
    for sh in sherpas:
        sh.delete()
    students = Pioupiou4j.nodes.all()
    for piou in students:
        piou.delete()
    partenaires = Partenaire4j.nodes.all()
    for part in partenaires:
        part.delete()


if __name__ == '__main__':
    # CSV containing the list of epita binomes and their infos
    file = "ressources/Liste leads.csv"
    wb = openpyxl.load_workbook("ressources/effectif_campus_clean.xlsx")
    # projects list
    p_list = create_project_list(read_csv(file))
    parse_excel(p_list)
    parse_excel_partenaire(p_list)

    clear_db()

    for project in p_list:

        # create the 2 humans nodes inside an epita binome
        h1 = Human4j(
            firstname=project.binome.human1.firstname,
            lastname=project.binome.human1.lastname,
            number=project.binome.human1.number,
            email=project.binome.human1.email,
            school=project.binome.human1.school
        ).save()
        h2 = Human4j(
            firstname=project.binome.human2.firstname,
            lastname=project.binome.human2.lastname,
            number=project.binome.human2.number,
            email=project.binome.human2.email,
            school=project.binome.human2.school
        ).save()

        # create a binome node and its relations to the 2 humans
        binome = Binome4j().save()

        binome.human1.connect(h1)
        binome.human2.connect(h2)

        # create a project node and a relation with the associated binome
        p = Project4j(name=project.project_name).save()
        p.binome.connect(binome)

        for sherpa in project.sherpas:
            s = Sherpa4j(
                firstname=sherpa.human.firstname,
                lastname=sherpa.human.lastname,
                number=sherpa.human.number,
                email=sherpa.human.email,
                campus=sherpa.campus,
                school=sherpa.human.school
            ).save()
            p.sherpas.connect(s)

        for student in project.students:
            s = Pioupiou4j(
                firstname=student.human.firstname,
                lastname=student.human.lastname,
                number=student.human.number,
                email=student.human.email,
                team=student.team,
                campus=student.campus,
                school=student.human.school
            ).save()
            p.students.connect(s)

        part = Partenaire4j(
            firstname=project.partenaire.firstname,
            lastname=project.partenaire.lastname,
            number=project.partenaire.number,
            email=project.partenaire.email,
            job=project.partenaire.job,
        ).save()
        p.partenaire.connect(part)
