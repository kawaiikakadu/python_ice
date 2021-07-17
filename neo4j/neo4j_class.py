from neomodel import UniqueIdProperty, StructuredNode, StringProperty, Relationship, RelationshipFrom


# basic human representation
class Human4j(StructuredNode):
    """
    A neo4j class to represent a human node.

    ...

    Attributes
    ----------
    firstname : StringProperty
        first name of the human
    lastname : StringProperty
        family name of the human
    school : StringProperty
        school of the human
    number : StringProperty
        telephone number of the human
    email : StringProperty
        email of the human

    Methods
    -------
    None
    """
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)


# duo of epita students, leaders on projects
class Binome4j(StructuredNode):
    """
    A neo4j class to represent a binome node of two EPITA students.

    ...

    Attributes
    ----------
    human1 : Relationship()
        relationship between the leader of the binome and the binome node
    human2 : Relationship()
        relationship between the mate of the leader and the binome node
    uid : UniqueIdProperty
        unique Id of the binome

    Methods
    -------
    None
    """
    uid = UniqueIdProperty()

    human1 = Relationship(Human4j, 'LEADER')
    human2 = Relationship(Human4j, 'BINOME')


# isg referents managing isg students
class Sherpa4j(StructuredNode):
    """
    A Neo4j class to represent a sherpa node = tutor of ISG students.

    ...

    Attributes
    ----------
    firstname : StringProperty
        first name of the sherpa
    lastname : StringProperty
        family name of the sherpa
    school : StringProperty
        school of the sherpa
    number : StringProperty
        telephone number of the sherpa
    email : StringProperty
        email of the sherpa
    campus : StringProperty
        ISG's campus the sherpa works at

    Methods
    -------
    None
    """
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    campus = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)


# isg students
class Pioupiou4j(StructuredNode):
    """
    A neo4j class to represent a pioupiou node = student from ISG.

    ...

    Attributes
    ----------
    firstname : StringProperty
        first name of the pioupiou
    lastname : StringProperty
        family name of the pioupiou
    school : StringProperty
        school of the pioupiou
    number : StringProperty
        telephone number of the pioupiou
    email : StringProperty
        email of the pioupiou
    campus : StringProperty
        campus of the ISG the pioupiou works at
    team : StringProperty
        number of the team the pioupiou is in

    Methods
    -------
    None
    """
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    campus = StringProperty(unique_index=True)
    team = StringProperty(unique_index=True)
    school = StringProperty(unique_index=True)


# client on each project
class Partenaire4j(StructuredNode):
    """
    A neo4j class to represent a partenaire node.

    ...

    Attributes
    ----------
    firstname : StringProperty
        first name of the partenaire
    lastname : StringProperty
        family name of the partenaire
    job : StringProperty
        job of the partenaire
    number : StringProperty
        telephone number of the partenaire
    email : StringProperty
        email of the partenaire

    Methods
    -------
    None
    """
    firstname = StringProperty(unique_index=True)
    lastname = StringProperty(unique_index=True)
    job = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    number = StringProperty(unique_index=True)


# the projects in Planete Solidaire
class Project4j(StructuredNode):
    """
    A neo4j class to represent a project node

    ...

    Attributes
    ----------
    name : StringProperty
        name of the project
    binome : RelationshipFrom()
        relationship from EPITA's binome leading the project to project node
    partenaire : RelationshipFrom()
        relationship from partenaire the project is for to the project node
    sherpas : RelationshipFrom()
        relationship from list of the sherpas working on the project to the project node
    students: RelationshipFrom()
        relationship from list of the students working on the project to the project node

    Methods
    -------
    None
    """
    name = StringProperty(unique_index=True)

    binome = RelationshipFrom(Binome4j, 'LEADERS_EPITA')
    partenaire = RelationshipFrom(Partenaire4j, 'CLIENT')
    sherpas = RelationshipFrom(Sherpa4j, 'SHERPA')
    students = RelationshipFrom(Pioupiou4j, 'WORKS_ON')


# the main project, a node itself as there is no client in particular
class Planete_Solidaire(StructuredNode):
    """
    A neo4j class to represent a Planete Solidaire node

    ...

    Attributes
    ----------
    binome : RelationshipFrom()
        relationship from the binome leading planete solidaire to the planete solidaire node
    caroline : RelationshipFrom()
        relationship from caroline to the planete solidaire node
    michel : RelationshipFrom()
        relationship from michel to the planete solidaire node
    cedric : RelationshipFrom()
        relationship from cedric to the planete solidaire node
    name: StringProperty
        name of the planete solidaire node

    Methods
    -------
    None
    """
    binome = RelationshipFrom(Binome4j, 'LEADERS_EPITA')
    caroline = RelationshipFrom(Human4j, 'LEADER_ISG')
    michel = RelationshipFrom(Human4j, 'CONSULTANT_EPITA')
    cedric = RelationshipFrom(Human4j, 'CONSULTANT_EPITA')

    name = StringProperty(unique_index=True)
