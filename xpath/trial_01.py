# _*_ coding : utf-8 _*_
# @Time : 2023/1/10 22:55
# @Author : Confetti-Lxy
# @File : trial_01
# @Project : Reptile

from lxml import etree

tree = etree.parse('trial_01.html')
print(tree.xpath('//ul/li/text()'))
print(tree.xpath('//ul/li[@id]/text()'))
print(tree.xpath('//ul/li[@id="l1"]/text()'))
print(tree.xpath('//ul/li[@id="l1"]/@class'))
print(tree.xpath('//ul/li[contains(@id,"l")]/text()'))
print(tree.xpath('//ul/li[starts-with(@id,"c")]/text()'))
print(tree.xpath('//ul/li[@id="l1" and @class = "c1"]/text()'))
print(tree.xpath('//ul/li[@id = "l1"]/text() | //ul/li[@id = "l2"]/text()'))
