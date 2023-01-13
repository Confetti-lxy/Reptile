# _*_ coding : utf-8 _*_
# @Time : 2023/1/13 14:39
# @Author : Confetti-Lxy
# @File : trial_01
# @Project : Reptile

import jsonpath
import json

obj = json.load(open('trial_01.json', encoding='utf-8'))
# print(jsonpath.jsonpath(obj, '$.store.book[*].author'))
# print(jsonpath.jsonpath(obj, '$..author'))
# print(jsonpath.jsonpath(obj, '$.store.*'))
# print(jsonpath.jsonpath(obj, '$..store..price'))
# print(jsonpath.jsonpath(obj, '$..store.book[2]'))
# print(jsonpath.jsonpath(obj, '$..store.book[(@.length-1)]'))
# print(jsonpath.jsonpath(obj, '$..store.book[0:2]'))  # [0,1]也可以
# print(jsonpath.jsonpath(obj, '$..book[?(@.isbn)].price'))
print(jsonpath.jsonpath(obj, '$..book[?(@.price>10)].title'))
