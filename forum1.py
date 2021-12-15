import pandas as pd
import numpy as np

# Визуализация
import seaborn as sns
import matplotlib.pyplot as plt

# Обращение к сайтам + bs
from bs4 import BeautifulSoup
import requests

# Регулярные выражения
import re

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

forum1 = "http://forumswimming.ru/"
forum2 = "https://forum.sportbox.ru/index.php?showforum=106"
forum3 = "https://www.trilife.ru/forum/forum14/"
forum4 = "https://www.trilife.ru/forum/forum14/"


forum2_df = pd.read_html(requests.get(forum1, headers=header).text)[2]

print(forum2_df.columns)


features_forum2 = ['Название темы', 'Статистика']


stat_forum2 = pd.DataFrame()
stat_forum2['themes'] = forum2_df[2]
stat_forum2['ans'] = forum2_df[3]
stat_forum2.drop(labels=[0,1],axis = 0,inplace = True)
#print(stat_forum2["themes"])
#stat_forum2['views'] = forum2_df['Статистика'].apply(lambda it: it.replace('Горячая тема', '')).apply(lambda it: int(it.split()[3]))
#themes_forum2 = forum2_df['Название темы']


#print(stat_forum2)


page = requests.get(forum1)
print(page.status_code)


soup = BeautifulSoup(page.text, "html.parser")

all_links = [a['href'] for a in soup.findAll('a', class_='forum')]
i = 0
for item in all_links:
    all_links[i] = "http://forumswimming.ru" + item
    i+=1

comments = []
sub_links = []

for j, link in enumerate(all_links):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    p = [a['href'] for a in soup.findAll('a', class_='forum')]
    i = 0
    for item in p:
        p[i] = "http://forumswimming.ru" + item
        i += 1
    sub_links = sub_links + p

all_links = all_links + sub_links
print(len(all_links))
sub_links = []
f_all_links = []

for j, link in enumerate(all_links):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    p = int(soup.find('span', class_='numPages').text)
    if p == 1:
        sub_links.append(link)
    for i in range(1,p):
        #print(link+"-0-"+str(i))
        sub_links.append(link+"-0-"+str(i))
    f_all_links = f_all_links + sub_links
    sub_links = []

all_links = []
sub_links = []

for j, link in enumerate(f_all_links):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    p = [a['href'] for a in soup.findAll('a', class_='threadLink')]
    for i in p:
        #print(link+"-0-"+str(i))
        sub_links.append(link+i)
    all_links = all_links + sub_links
    sub_links = []

f_all_links = []
sub_links = []

temp_str = ""
for j, link in enumerate(all_links):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    p = int(soup.find('span', class_='numPages').text)
    #print(p)
    if p == 1:
        sub_links.append(link)
    for i in range(1, p):
        temp_str = link[:-1]
        sub_links.append(temp_str + str(i))
    f_all_links = f_all_links + sub_links



#print(f_all_links)
print(len(f_all_links))

csv = pd.DataFrame()
csv['links'] = f_all_links
csv.to_csv("everyLink2.csv")


comments = []

for j, link in enumerate(f_all_links):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    p = soup.findAll('li', class_='pagejump')
    if (len(p) == 0):
        p = 1
    else:
        p = int(p[0].find('a').text.split()[3])
        #print(p)
    comments.append([])
    for i in range(1, p + 1):
        page = requests.get(link+f'&page={i}')
        soup = BeautifulSoup(page.text, "html.parser")
        com = soup.findAll('div', class_='post')
        for c in com:
            comments[j].append(c.text)
    print(f'end {j}')

print(comments)

