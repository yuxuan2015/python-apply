#-*- coding:utf-8 _*-
"""
@author:lyy
@file: es-demo.py
@time: 2019/04/01
@Software: PyCharm
"""

#https://github.com/elastic/elasticsearch-py

from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#创建索引，索引的名字是my-index,如果已经存在了，就返回个400，
#这个索引可以现在创建，也可以在后面插入数据的时候再临时创建
#es.indices.create(index='my-index')

#插入数据,(这里省略插入其他两条数据，后面用)
#es.index(index="my-index", doc_type="test-type", id=1, body={"any": "data01", "timestamp": datetime.now()})

#查询数据，两种get and search
#get获取
res = es.get(index="my-index", doc_type="test-type", id=1)
print(res)
#es.get(index='indexName', doc_type='typeName', id='idValue')
print(es.search(index="quros", doc_type="texts"))
