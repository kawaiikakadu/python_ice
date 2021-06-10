from retrieve_data import read_csv, create_project_list, print_project_list
from neomodel import UniqueIdProperty, StructuredNode, StringProperty, Relationship, RelationshipTo, RelationshipFrom, config
from neomodel import db

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
db.set_connection('bolt://neo4j:password@localhost:7687')


class School(StructuredNode):
    name = StringProperty(unique_index=True)


class Human4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)

    school = RelationshipTo(School, 'WORKS_AT')


class Binome(StructuredNode):
    uid = UniqueIdProperty()

    human1 = Relationship(Human4j, 'LEADER')
    human2 = Relationship(Human4j, 'BINOME')


class Project(StructuredNode):
    name = StringProperty(unique_index=True)

    binome = RelationshipFrom(Binome, 'LEADERS')


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
    schools = School.nodes.all()
    for s in schools:
        s.delete()


if __name__ == '__main__':
    # CSV containing the list of epita binomes and their infos
    file = "ressources/Liste leads.csv"
    # projects list
    p_list = create_project_list(read_csv(file))

    clear_db()
    epita = School(name='EPITA').save()

    for project in p_list:

        # create the 2 humans nodes inside an epita binome
        h1 = Human4j(
                    firstname=project.binome.human1.firstname,
                    lastname=project.binome.human1.lastname,
                    number=project.binome.human1.number,
                    email=project.binome.human1.email
                ).save()
        h1.school.connect(epita)
        h2 = Human4j(
                    firstname=project.binome.human2.firstname,
                    lastname=project.binome.human2.lastname,
                    number=project.binome.human2.number,
                    email=project.binome.human2.email
                ).save()
        h2.school.connect(epita)

        # create a binome node and its relations to the 2 humans
        binome = Binome().save()

        binome.human1.connect(h1)
        binome.human2.connect(h2)

        # create a project node and a relation with the associated binome
        Project(name=project.project_name).save().binome.connect(binome)
