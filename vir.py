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
else:
    print("Contest page parsing has started !!!!")
# print(page.text)
# Note- page.text contains the html or the page source
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())


#Function to make the stats.txt file
def make_stats_file(stats_text):
    print(stats_text)




#First extract the stats of the contest from the standings page
page_stats = requests.get(contest_url + '/standings')
# print(page_stats)
if(page_stats.status_code != 200):
    print("Failed to retrive stats for contest {}!!!!".format(contest_id))
else:
    print("Stats for contest {} are being retrieved !!!".format(contest_id))
soup_stats = BeautifulSoup(page_stats.text, 'html.parser')
acc_tried = soup_stats.find('table')

acc_tried_notice = acc_tried.findAll('span', attrs={"class": "notice"})
acc_tried_AC = acc_tried.findAll('span', attrs={"class": "cell-passed-system-test cell-accepted"})
print("Standings row for stats captured!!!")
# print(len(acc_tried_notice))
# print(len(acc_tried_AC))
stats_text = "AC Stats: \n"
for i in range(len(acc_tried_AC)):
    if i==0:continue
    
    ac_num = acc_tried_AC[i].text
    try_num = acc_tried_notice[i].text
    per = (int(ac_num) / int(try_num)) * 100.00
    per = round(per,2)

    temp_text = "\nProblem {} - Accepted: {} Tried: {} Success: {}%".format(i,ac_num,try_num,per)
    # print(temp_text)
    stats_text = stats_text + temp_text

# make_stats_file(stats_text)


#Extract the contest-details
# print(soup.prettify())
tables = soup.findAll('table')
print(tables)




