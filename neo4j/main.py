from neomodel import UniqueIdProperty, StructuredNode, StringProperty, Relationship, RelationshipTo, RelationshipFrom, \
    config
from neomodel import db
from retrieve_data_isg import *

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
db.set_connection('bolt://neo4j:password@localhost:7687')


class Human4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)


class Binome(StructuredNode):
    uid = UniqueIdProperty()

    human1 = Relationship(Human4j, 'LEADER')
    human2 = Relationship(Human4j, 'BINOME')


class Sherpa4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    campus = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)

    # projet = RelationshipTo(Project, "WORKS_ON")


class Pioupiou4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    campus = StringProperty(unique_index=True)
    team = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)

    # projet = RelationshipTo(Project, "WORKS_ON")


class Project(StructuredNode):
    name = StringProperty(unique_index=True)

    binome = RelationshipFrom(Binome, 'LEADERS')
    sherpas = RelationshipFrom(Sherpa4j, 'SHERPA')
    students = RelationshipFrom(Pioupiou4j, 'WORKS_ON')


# clear all categories of nodes in the db
def clear_db():
    humans = Human4j.nodes.all()
    for h in humans:
        h.delete()
    binomes = Binome.nodes.all()
    for b in binomes:
        b.delete()
    projects = Project.nodes.all()
    for p in projects:
        p.delete()
    sherpas = Sherpa4j.nodes.all()
    for sh in sherpas:
        sh.delete()
    students = Pioupiou4j.nodes.all()
    for piou in students:
        piou.delete()


if __name__ == '__main__':
    # CSV containing the list of epita binomes and their infos
    file = "ressources/Liste leads.csv"
    # projects list
    p_list = create_project_list(read_csv(file))
    parse_lille(p_list)

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
        binome = Binome().save()

        binome.human1.connect(h1)
        binome.human2.connect(h2)

        # create a project node and a relation with the associated binome
        p = Project(name=project.project_name).save()
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
