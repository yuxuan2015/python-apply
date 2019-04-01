#-*- coding:utf-8 _*-
"""
@author:lyy
@file: loaddata_es.py
@time: 2019/04/01
@Software: PyCharm
"""

from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

actions = []

f = open('test.txt', encoding="utf8")
i = 1
for line in f:
    line = line.strip().split('\t')
    action = {
        "_index": "quros",
        "_type": "texts",
        "_id": i,
        "_source": {
            "label": line[0],
            "q1": line[1],
            "q2": line[2]
        }
    }
    i += 1
    actions.append(action)
    if (len(actions) == 500):
        helpers.bulk(es, actions)
        del actions[0:len(actions)]

if (len(actions) > 0):
    helpers.bulk(es, actions)
