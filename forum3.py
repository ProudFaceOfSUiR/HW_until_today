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

'''
forum3_df = pd.read_html(requests.get(forum2, headers=header).text)[1]
print(forum2_df["Статистика"])

print("kkkkkkkkkk")


features_forum2 = ['Название темы', 'Статистика']
stat_forum2 = pd.DataFrame()
stat_forum2['ans'] = forum2_df['Статистика'].apply(lambda it: it.replace('Горячая тема', '')).apply(lambda it: int(it.split()[0]))
stat_forum2['views'] = forum2_df['Статистика'].apply(lambda it: it.replace('Горячая тема', '')).apply(lambda it: int(it.split()[2]))
themes_forum2 = forum2_df['Название темы']


print(stat_forum2.values)


page = requests.get(forum2)
print(page.status_code)

print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")




#print(page.text)
'''

def change_month(str):
    str.replace("января", "01")
    str.replace("февраля", "02")
    str.replace("марта", "03")
    str.replace("апреля", "04")
    str.replace("мая", "05")
    str.replace("июля", "06")
    str.replace("июня", "07")
    str.replace("августа", "08")
    str.replace("сентября", "09")
    str.replace("октября", "10")
    str.replace("ноября", "11")
    str.replace("декабря", "12")
    return str




page1 = requests.get(forum3)
page2 = requests.get(forum3+"?PAGEN_1=2")
page3 = requests.get(forum3+"?PAGEN_1=1")
print(page1.status_code)

def get_csv(csv, page):
    soup = BeautifulSoup(page.text, "html.parser")
    all_links = []
    for a in range (0, len(soup.findAll('span', class_='forum-item-title'))):
        all_links.append(str(soup.findAll('span', class_='forum-item-title')[a]).split('href="')[1].split('" title')[0])

    print(all_links)

    comments = []
    date = []
    author_rank = []
    author_messages = []
    author_reputation = []
    #print(requests.get(all_links[1]).text)
    rank = []
    for j, link in enumerate(all_links):
        lk = "https://www.trilife.ru"+link
        #print(lk)
        page = requests.get(lk)
        page_tmp = requests.get("https://forum.sportbox.ru/index.php?showforum=106")
        soup_tmp = BeautifulSoup(page_tmp.text, "html.parser")
        soup = BeautifulSoup(page.text, "html.parser")
        i = 1
        com = soup.findAll('div', class_='forum-post-text')
        com_prev = soup_tmp.findAll('div')
        #print(com[0].text)
        #print(com_prev)
        print(com == com_prev)
        while com[0].text != com_prev[0].text:
            com_prev = BeautifulSoup(requests.get(lk+'/?PAGEN_1='+str(i+1)).text, "html.parser").findAll('div', class_='forum-post-text')
            page = requests.get(lk+'/?PAGEN_1='+str(i))
            print(lk+'/?PAGEN_1='+str(i))
            #print(page.content)
            soup = BeautifulSoup(page.text, "html.parser")
            com = soup.findAll('div', class_='forum-post-text')
            #print(len(com))
            dat = soup.findAll('div', class_='forum-post-date')
            #print(len(dat))
            print(com == com_prev)
            print(com[0].text)
            print(com_prev[0].text)
            #print(len(com))

            a = 0
            i+=1
            for c in com:
                comments.append(str(c.text))
                #print(comments[a])
                #print(dat[a].text)
                date.append(dat[a].text.split(",")[1][1:][:-8])
                #print(date[a])
                author_reputation.append("nan")
                author_messages.append('nan')
                author_rank.append('nan')
                a += 1

        #rank = soup.findAll("p", {"class": "desc member_title"})
        #rep = soup.findAll("li", {"class": "group_title"})
        #name = soup.findAll("span", {"itemprop":"name"})

        #print(f'end {j}')

    csv = pd.DataFrame()
    print(len(comments))
    print(comments.__class__)

    csv["author_rank"] = author_rank
    csv["author_messges"] = author_messages
    csv["author_reputation"] = author_reputation
    csv["comment_text"] = comments
    csv["date"] = date
    csv.to_csv("forum3.csv")



csv = pd.DataFrame()
get_csv(csv, page1)

