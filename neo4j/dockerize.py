from elasticsearch import Elasticsearch
import json
from Python_class import *

es = Elasticsearch()


def elastic(projects):
    """
    Function to dockerize projects list

    :param projects: projects list
    :return: NONE
    """
    for project in projects:
        pt = {
            'name': project.project_name,
            'binome': {
                "leader": json.dumps(project.binome.human1, cls=HumanEncoder, ensure_ascii=False),
                "collègue": json.dumps(project.binome.human2, cls=HumanEncoder, ensure_ascii=False)
            },
            'partenaire': json.dumps(project.partenaire, cls=PartenaireEncoder, ensure_ascii=False),
            'sherpas': json.dumps(project.sherpas, cls=SherpaEncoder, ensure_ascii=False),
            'students': json.dumps(project.students, cls=PioupiouEncoder, ensure_ascii=False)
        }
        res = es.index(index="test-index", id=1, body=pt)

        # res = es.get(index="test-index", id=1)
        # print(res['_source'])
