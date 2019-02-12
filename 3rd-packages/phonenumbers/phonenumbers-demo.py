# -*- coding:utf-8 -*-

#-*- coding:utf-8 _*-
"""
@author:lyy
@file: phonenumbers-demo.py
@time: 2019/02/12
@Software: PyCharm
"""

import phonenumbers

##格式化电话号码
x = phonenumbers.parse("+442083661177", None)
y = phonenumbers.parse("020 8366 1177", "GB")
print(x == y)

z = phonenumbers.parse("+12001230101", None)
print(z)
print(phonenumbers.is_possible_number(z))  # too few digits for USA
print(phonenumbers.is_valid_number(z))  # NPA 200 not used

## 无法正常解析
#z = phonenumbers.parse("02081234567", None)  # no region, no + => unparseable

## 格式化输出
print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL))
print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164))

##
text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
for match in phonenumbers.PhoneNumberMatcher(text, "US"):
    print(match)
    print(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))

#text = "非常紧急转告：被告**，户籍地址:山东***室 。济南律师事务所郑重告知：因你恶意拖欠佰仟金融公司的贷款，我所已经将你“涉嫌贷款诈骗罪”的相关材料已递交到公安局。请保持手机24小时处于待机状态，接受当地公安24小时内随时传唤或询问。原告律师-张良  办公室:0531-8235 0561  手机:15753145942 电话这几天打遍所有联系人和单位。 结果让济南的朋友在电信局通过熟人查到 0531-8235 0561是济南德盈律师事务所的， 还冒充济南律师事务所"
text = "你还为被人骗了而烦恼吗？ 找我就对了，专业轰炸 专业催收 合作qq937852948。02138510106这个是催收电话吗？是这样的，12月1号01095595电话邀请账单分期提额到10万，上个月我自己做了个分期，分期后还款3000多，可是我错就错在当天全额还上了，可是昨天光大银行的催收部门给我打电话，说我上个月没有还款，然后晚上就致电4008111333，确认已经产生滞纳金，于是我当即就还上了，请问卡友们，像这样的情况，三个月后我还能申请临时额度提高吗？以前申请可是从来没有拒绝过"
for match in phonenumbers.PhoneNumberMatcher(text, "CN"):
    print(match)
    print(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.NATIONAL))

##格式化例子
number_list = ["182--6008--6180",
               "1826*00*86180",
               "025-5763062*0"]

for phone in number_list:
    x = phonenumbers.parse(phone, "CN")
    print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL))


##格式化输入号码
formatter = phonenumbers.AsYouTypeFormatter("CN")
for x in "15112345678":
    formatter.input_digit(x)

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

ch_number = phonenumbers.parse("188--1784--006", "CN")
print(ch_number)
print(phonenumbers.is_possible_number(ch_number))  # too few digits for USA
print(phonenumbers.is_valid_number(ch_number))  # NPA 200 not used

##号码归属地
print(geocoder.description_for_number(ch_number, "en"))
print(timezone.time_zones_for_number(ch_number))

ro_number = phonenumbers.parse("+40721234567", "RO")
print(carrier.name_for_number(ro_number, "en"))