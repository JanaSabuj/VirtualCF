import os
import requests
from bs4 import BeautifulSoup

page = requests.get('https://codeforces.com/contest/1216/problem/C')
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())

inp = soup.findAll('div', attrs={"class" : "input"})
# print(inp)

out = soup.findAll('div', attrs={"class" : "output"})
# print(out)

txt = ""
for i in range(len(inp)):
    x = inp[i].text
    y = out[i].text
    txt = txt + "\n" + x + "\n" + y

print(txt)


