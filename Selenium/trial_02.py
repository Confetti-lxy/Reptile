# _*_ coding : utf-8 _*_
# @Time : 15/01/2023 12:29
# @Author : Confetti-Lxy
# @File : trial_02
# @Project : Reptile

from selenium import webdriver

browser = webdriver.Edge()

url = 'https://www.baidu.com'
browser.get(url)

Input = browser.find_element('id', 'su')
a = browser.find_element_by_link_text('新闻')
print(Input.get_attribute('class'))
print(Input.tag_name)
print(a.text)
