# Built by greenindia - Sabuj Jana - Jadavpur University 
# www.janasabuj.github.io
# 28-29 Sept 2019
import os
import sys
import requests
import time
import re
import ssl
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

parent_path = os.getcwd()
illegal = ["<", ">", "[", "]",  "?", ":", "*" , "|"]

#f Function to generate the extension of the solution file according to the language preffered by the user
def get_extension():
    language = input('\nWhat is the language of your choice? \n1-C++ \n2-C \n3-Python \n4-Java \n5-Kotlin \n6-Javascript \n7-PHP \n8-Ruby \nEnter your choice: ')
    hash = {
        1 : '.cpp',
        2 : '.c',
        3 : '.py',
        4 : '.java',
        5 : '.kt',
        6 : '.js',
        7 : '.php',
        8 : '.rb'
    }
    return hash[int(language)]
  
contest_url = 'https://codeforces.com/contest/'
contest_id =  input('Enter the contest id: ') #ask-for-id
extension = get_extension() #ask-for-lang and get-ext

contest_url = contest_url + contest_id
print(contest_url)
page = requests.get(contest_url, verify = True)
if(page.status_code != 200):
    print("Failed to retrive contest {}!!!!".format(contest_id))
    exit(1)
else:
    print("Contest page parsing has started !!!!")
soup = BeautifulSoup(page.text, 'html.parser') #page.text contains the html or the page source
contest_problem_url = 'https://codeforces.com/contest/{}/problem/'.format(contest_id)



#f get the png plot
def get_matplotlib_png(prob_x, acc_y,folder_name):
    plt.plot(prob_x,acc_y, color='r', marker='o', label='Success rate')
    plt.title('Problem VS Acceptance Rate')
    plt.xlabel('Problem')
    plt.ylabel('Acceptance')
    plt.legend()
    pic_path = os.path.join(folder_name,"stats.png")
    plt.savefig(pic_path)

#f Extract i/o statements for the problem 
def get_contest_io(contest_problem_url,prob_folder_name,prob_no,prob_name,contest_id):
    file2 = prob_no + ".txt"
    file2 = os.path.join(prob_folder_name,file2)
    fname = open(file2, "a")
    

    url = 'https://codeforces.com/contest/{}/problem/{}'.format(contest_id,prob_no)
    page = requests.get(url, verify = True)
    soup = BeautifulSoup(page.text, 'html.parser')
    fname.write("Problem URL: " + url)

    inp = soup.findAll('div', attrs={"class" : "input"})
    out = soup.findAll('div', attrs={"class" : "output"})

    txt = ""
    for i in range(len(inp)):
        x = inp[i].text
        y = out[i].text
        txt = txt + "\n---------------------------------------------------"
        txt = txt + "\n" + x + "\n" + y
        txt = txt + "---------------------------------------------------"

    # print(txt)
    fname.write("\nI/O statements for {} {} \n".format(prob_no,prob_name))
    fname.write(txt)
    fname.close()    

#f Create problem folders 
def create_problem_folder(prob_no, prob_name,contest_problem_url,folder_name,extension,template_txt,contest_id):
    print(prob_no,prob_name, "\nExtracting ......")
    contest_problem_url = contest_problem_url +  prob_no
    print(contest_problem_url, "is being parsed .....")
    print(folder_name)
    
    prob_folder_name = prob_no + " " + prob_name

    for str_char in illegal:
        prob_folder_name = prob_folder_name.replace(str_char," ")
    prob_folder_name = os.path.join(folder_name, prob_folder_name)
    os.mkdir(prob_folder_name)
    print("Problem {} folder created".format(prob_no))

    file1 = prob_no + extension
    file1 = os.path.join(prob_folder_name,file1)
    fname = open(file1,"a")
    fname.write(template_txt)
    fname.close()

    print("\nTime to get the i/o for {} {}".format(prob_no,prob_name))
    
    get_contest_io(contest_problem_url,prob_folder_name,prob_no,prob_name,contest_id)
    print("I/O extraction a Success !")

    #create the input.txt file for personal input output
    file3 = "input.txt"
    file3 = os.path.join(prob_folder_name,file3)
    fname = open(file3,"a")
    fname.close()

    print("Done . Rest for 5s. Move on......\n\n")
    time.sleep(5)

#f Function to get the folder_name 
def get_folder_name(contest_name):
    folder_name = os.path.join(parent_path,contest_name)
    for str_char in illegal:
        folder_name = folder_name[0:10] + folder_name[10:].replace(str_char," ")
    return folder_name

#f Function to make the stats.txt file 
def make_stats_file(stats_text,folder_name,prob_x, acc_y):
    stats_file = os.path.join(folder_name,"stats.txt")
    fname = open(stats_file, "a")
    fname.write(stats_text)
    fname.close()
    print("Stats.txt created.\n Graph is being plotted !!!")
    get_matplotlib_png(prob_x, acc_y,folder_name)
    print("\n\n-----The end---------")

#f Function to extract the standing row 
def standings_row_extraction(contest_name, folder_name,prob_x):
    #First extract the stats of the contest from the standings page
    page_stats = requests.get(contest_url + '/standings' , verify = True)
    # print(page_stats)
    if(page_stats.status_code != 200):
        print("Failed to retrive stats for contest {}!!!!".format(contest_id))
    else:
        print("Stats for contest {} are being retrieved !!!".format(contest_id))
    soup_stats = BeautifulSoup(page_stats.text, 'html.parser')
    acc_tried = soup_stats.find('table')

    acc_tried_notice = acc_tried.findAll('span', attrs={"class": "notice"})
    acc_tried_AC = acc_tried.findAll('span', attrs={"class": "cell-passed-system-test"})
    
    print("Standings row for stats captured!!!")
    
    x = len(acc_tried_notice)
    acc_tried_AC = acc_tried_AC[-x:] #extract last n rows
    
    
    acc_y=[]

    stats_text = "AC Stats: \n"
    for i in range(len(acc_tried_AC)):
        if i==0:continue
        
        ac_num = acc_tried_AC[i].text
        try_num = acc_tried_notice[i].text
        if int(try_num) == 0:
            per = 0
        else:
            per = (int(ac_num) / int(try_num)) * 100.00
            per = round(per,2)

        temp_text = "\nProblem {} - Accepted: {} Tried: {} Success: {}%".format(i,ac_num,try_num,per)
        acc_y.append(per)
        stats_text = stats_text + temp_text
    make_stats_file(stats_text, folder_name,prob_x,acc_y)
    

#---------------------------------MAIN---------------------------------------------#
#Extract the contest-details
tables = soup.findAll('table')
contest_name = tables[0].find('a').text.strip()
print(contest_name)

#universal folder name
folder_name = get_folder_name(contest_name)

#extract the datatable 
problems = soup.find('div', attrs={"class":"datatable"}).find('table').findAll('a')

#template-parse
fname = open('template.txt', "r")
template_txt = fname.read().strip()
fname.close()

#create the problem folder
os.mkdir(folder_name)

print("\n\nThe problems will be parsed. Hold your horses for 3 secs!!!!")
time.sleep(3)
prob_x = [] #list of problems

for i in range(len(problems)):
    #For every contest
    if i%4 !=0 : continue
    txt = problems[i].text.strip()
    prob_no = problems[i].text.strip()
    prob_name = problems[i+1].text.strip()
    prob_x.append(prob_no)
    create_problem_folder(prob_no,prob_name,contest_problem_url,folder_name,extension,template_txt,contest_id)

# Get the stats-txt file
standings_row_extraction(contest_name,folder_name,prob_x)

