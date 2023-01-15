# _*_ coding : utf-8 _*_
# @Time : 15/01/2023 14:02
# @Author : Confetti-Lxy
# @File : chrome_handless
# @Project : Reptile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--disable-gpu')
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chromeOptions.binary_location = path
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    return browser
