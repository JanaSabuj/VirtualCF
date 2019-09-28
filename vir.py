# Built by greenindia - Sabuj Jana - Jadavpur University 
# www.janasabuj.github.io

import os
import sys
import requests
import time
import re
from bs4 import BeautifulSoup

contest_url = 'http://codeforces.com/contest/'
contest_id = '1216'

contest_url = contest_url + contest_id
print(contest_url)
page = requests.get(contest_url)
# print(page.status_code)
if(page.status_code != 200):
    print("Failed to retrive contest {}!!!!".format(contest_id))
    exit(1)

# print(page.text)
# Note- page.text contains the html or the page source
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())


