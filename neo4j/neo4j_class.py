from neomodel import UniqueIdProperty, StructuredNode, StringProperty, Relationship, RelationshipFrom


# basic human representation
class Human4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)


# duo of epita students, leaders on projects
class Binome4j(StructuredNode):
    uid = UniqueIdProperty()

    human1 = Relationship(Human4j, 'LEADER')
    human2 = Relationship(Human4j, 'BINOME')


# isg referents managing isg students
class Sherpa4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    campus = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)


# isg students
class Pioupiou4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    campus = StringProperty(unique_index=True)
    team = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)


# client on each project
class Partenaire4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    job = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)


# the projects in Planete Solidaire
class Project4j(StructuredNode):
    name = StringProperty(unique_index=True)

    binome = RelationshipFrom(Binome4j, 'LEADERS_EPITA')
    partenaire = RelationshipFrom(Partenaire4j, 'CLIENT')
    sherpas = RelationshipFrom(Sherpa4j, 'SHERPA')
    students = RelationshipFrom(Pioupiou4j, 'WORKS_ON')


# the main project, a node itself as there is no client in particular
class Planete_Solidaire(StructuredNode):
    binome = RelationshipFrom(Binome4j, 'LEADERS_EPITA')
    caroline = RelationshipFrom(Human4j, 'LEADER_ISG')
    michel = RelationshipFrom(Human4j, 'CONSULTANT_EPITA')
    cedric = RelationshipFrom(Human4j, 'CONSULTANT_EPITA')
