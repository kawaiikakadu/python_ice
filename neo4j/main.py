from neo4j_class import *
from retrieve_data_partenaires import *
from neomodel import db, config

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
    ps = Planete_Solidaire.nodes.all()
    for misc in ps:
        misc.delete()


# function that init the db with general data not in any ressources given
def init_data():
    ps = Planete_Solidaire().save()

    maya = Human4j(
        firstname='Maya',
        lastname='Hannachi',
        number='0620902819',
        email='maya.hannachi@epita.fr',
        school='EPITA'
    ).save()
    mailinh = Human4j(
        firstname='Mai-Linh',
        lastname='Lannes',
        number='0612632032',
        email='mai-linh.lannes@epita.fr',
        school='EPITA'
    ).save()
    michel = Human4j(
        firstname='Michel',
        lastname='Sasson',
        number='0662739612',
        email='michel.sasson@epita.fr',
        school='EPITA'
    )
    cedric = Human4j(
        firstname='Cédric',
        lastname='Joly',
        number='',
        email='cedric.joly@epita.fr',
        school='EPITA'
    )
    caroline = Human4j(
        firstname='Caroline',
        lastname='De Paoli',
        number='',
        email='caroline.depaoli@isg.fr',
        school='ISG'
    )

    binome = Binome4j().save()
    binome.human1 = mailinh
    binome.human2 = maya

    ps.binome = binome
    ps.michel = michel
    ps.cedric = cedric
    ps.caroline = caroline


if __name__ == '__main__':
    # CSV containing the list of epita binomes and their infos
    file_epita = "ressources/Liste leads.csv"
    wb = openpyxl.load_workbook("ressources/effectif_campus_clean.xlsx")

    # projects list
    p_list = create_project_list(read_csv(file_epita))

    # complete each project info with data in the isg excel
    parse_excel_isg(p_list)

    # complete each project info with data in the clients excel
    parse_excel_partenaires(p_list)

    # clear the db from any residual data
    clear_db()

    # init the db with data that cannot be found in provided files
    init_data()

    # create all projects nodes in neo4j representation
    for project in p_list:
        # create a project node
        p = Project4j(name=project.project_name).save()

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

        # connect the 2 leaders to the binome node
        binome.human1.connect(h1)
        binome.human2.connect(h2)

        # create a relation with the associated binome
        p.binome.connect(binome)

        # create each sherpa node and connects it to the associated project
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

        # create each isg student node and connects it to the associated project
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

        # create the client node and connects it to the associated project
        part = Partenaire4j(
            firstname=project.partenaire.firstname,
            lastname=project.partenaire.lastname,
            number=project.partenaire.number,
            email=project.partenaire.email,
            job=project.partenaire.job,
        ).save()
        p.partenaire.connect(part)
