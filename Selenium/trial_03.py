# _*_ coding : utf-8 _*_
# @Time : 15/01/2023 13:00
# @Author : Confetti-Lxy
# @File : trial_03
# @Project : Reptile

from selenium import webdriver
import time

browser = webdriver.Edge()

url = 'https://www.baidu.com'
browser.get(url)
time.sleep(2)

Input = browser.find_element('id', 'kw')
Input.send_keys('周杰伦')
time.sleep(2)

Button = browser.find_element('id', 'su')
Button.click()
time.sleep(2)

for i in range(5):
    js_bottom = 'document.documentElement.scrollTop=100000'
    browser.execute_script(js_bottom)
    time.sleep(2)
    if i == 0:
        next_page = browser.find_element('xpath', '//a[@class="n"]')
        next_page.click()
        time.sleep(2)
    else:
        next_page = browser.find_elements('xpath', '//a[@class="n"]')[1]
        next_page.click()
        time.sleep(2)

# browser.back()
# time.sleep(2)
#
# browser.forward()
# time.sleep(3)

browser.quit()
