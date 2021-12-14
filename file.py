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

forum2 = "https://forum.sportbox.ru/index.php?showforum=106"


forum2_df = pd.read_html(requests.get(forum2, headers=header).text)[1]
print(forum2_df)

print(forum2_df.columns)


features_forum2 = ['Название темы', 'Статистика']
stat_forum2 = pd.DataFrame()
stat_forum2['ans'] = forum2_df['Статистика'].apply(lambda it: it.replace('Горячая тема', '')).apply(lambda it: int(it.split()[0]))
stat_forum2['views'] = forum2_df['Статистика'].apply(lambda it: it.replace('Горячая тема', '')).apply(lambda it: int(it.split()[2]))
themes_forum2 = forum2_df['Название темы']


print(stat_forum2)


page = requests.get(forum2)
print(page.status_code)


soup = BeautifulSoup(page.text, "html.parser")

all_links = [a['href'] for a in soup.findAll('a', class_='topic_title')]


comments = []


for j, link in enumerate(all_links):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    p = soup.findAll('li', class_='pagejump')
    if (len(p) == 0):
        p = 1
    else:
        p = int(p[0].find('a').text.split()[3])
    comments.append([])
    for i in range(1, p + 1):
        page = requests.get(link+f'&page={i}')
        soup = BeautifulSoup(page.text, "html.parser")
        com = soup.findAll('div', class_='post')
        for c in com:
            comments[j].append(c.text)
    print(f'end {j}')

print(len(comments))

