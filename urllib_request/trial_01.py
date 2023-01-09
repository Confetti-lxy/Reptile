# _*_ coding : utf-8 _*_
# @Time : 08/01/2023 00:01
# @Author : Confetti-Lxy
# @File : trial_01
# @Project : Reptile

import urllib.request

# 读取网站源码
url = 'http://www.baidu.com'  # 网站地址
response = urllib.request.urlopen(url)  # Type:<class 'http.client.HTTPResponse'>

# read() 读取的为二进制编码,一个字节一个字节的读取
# content = response.read()
# print(content)

# read(num) 返回num个字节
# content = response.read(5)
# print(content)

# readline() 按行读取,但只能读取一行,需要进行循环
# content = response.readline()
# print(content)

# readlines() 按行读取,全部读完
# content = response.readlines()
# print(content)

# getcode() 返回状态码,如果返回值为200,说明逻辑正确
# print(response.getcode())

# geturl() 返回url地址
# print(response.geturl())

# getheaders() 返回一些状态信息
# print(response.getheaders())
