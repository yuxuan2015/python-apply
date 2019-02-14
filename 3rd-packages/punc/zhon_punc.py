#-*- coding:utf-8 _*-
"""
@author:lyy
@file: zhon_punc.py
@time: 2019/02/13
@Software: PyCharm
"""

from zhon.hanzi import punctuation
import re

line='！今天写了个爬虫。、？'
print(re.sub(r"[%s]+" %punctuation, "", line))