# _*_ coding : utf-8 _*_
# @Time : 2023/1/13 16:10
# @Author : Confetti-Lxy
# @File : trial_01
# @Project : Reptile

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('trial_01.html', encoding='utf-8'), 'lxml')
print(soup.a)
print(soup.a.attrs)

print(soup.find('a'))
print(soup.find('a', title='a2'))
print(soup.find('a', class_='a1'))
print(soup.find_all('a'))
print(soup.find_all(['a', 'span']))
print(soup.find_all('li', limit=2))
print(soup.select('a'))
print(soup.select('.a1'))
print(soup.select('#l1'))
print(soup.select('li[id]'))
print(soup.select('li[id="l2"]'))
print(soup.select('div li'))
print(soup.select('div > ul > li'))
print(soup.select('a , li'))
print(soup.select('#d1')[0].getText())
print(soup.select('#p1')[0].name)
print(soup.select('#p1')[0].attrs)
print(soup.select('#p1')[0].attrs.get('class'))
print(soup.select('#p1')[0].get('class'))
print(soup.select('#p1')[0]['class'])
