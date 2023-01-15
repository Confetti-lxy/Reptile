# _*_ coding : utf-8 _*_
# @Time : 14/01/2023 23:20
# @Author : Confetti-Lxy
# @File : trial_01
# @Project : Reptile

from selenium import webdriver

browser = webdriver.Edge()
url = 'https://www.baidu.com'
browser.get(url)

print(browser.find_element_by_id('su'))
print(browser.find_element_by_name('wd'))
print(browser.find_element_by_xpath('//input[@id="su"]'))
print(browser.find_elements_by_tag_name('input'))
print(browser.find_element_by_css_selector('#su'))
print(browser.find_element_by_link_text('新闻'))
