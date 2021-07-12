from neomodel import UniqueIdProperty, StructuredNode, StringProperty, Relationship, RelationshipTo, RelationshipFrom, \
    config
from neomodel import db

class Human4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)


class Binome4j(StructuredNode):
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


class Pioupiou4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    campus = StringProperty(unique_index=True)
    team = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)


class Partenaire4j(StructuredNode):
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    job = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)


class Project4j(StructuredNode):
    name = StringProperty(unique_index=True)

    binome = RelationshipFrom(Binome4j, 'LEADERS')
    partenaire = RelationshipFrom(Partenaire4j, 'CLIENT')
    sherpas = RelationshipFrom(Sherpa4j, 'SHERPA')
    students = RelationshipFrom(Pioupiou4j, 'WORKS_ON')
