# _*_ coding : utf-8 _*_
# @Time : 15/01/2023 13:52
# @Author : Confetti-Lxy
# @File : trial_04
# @Project : Reptile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--disable-gpu')
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chromeOptions.binary_location = path
browser = webdriver.Chrome(chrome_options=chromeOptions)
url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('baidu.png')
