import pandas as pd

from bs4 import BeautifulSoup
import requests

comments = pd.read_csv("everyLink2.csv")
page = comments["links"].values
print(len(page))
page = list(set(page))
print((len(page)))
#soup = BeautifulSoup(page.text, "html.parser")
comments = []
date = []
author_rank = []
author_messages = []
author_reputation = []
m = 0
for i in page:
    print(i)
    print(m)
    m+=1
    page1 = requests.get(i)
    soup = BeautifulSoup(page1.text, "html.parser")
    com = soup.findAll('table', class_='postTable')
    for c in com:
        #print(c)
        #print(c.text.split("\n"))
        date.append(c.text.split("\n")[1].split(" ")[2][:-1])
        author_rank.append((c.text.split("\n")[3]))
        author_messages.append(c.text.split("\n")[6].split(" ")[1])
        author_reputation.append(c.text.split("\n")[7].split(" ")[1])
        comments.append((c.text.split("\n")[9]))


csv = pd.DataFrame()
csv['comments'] = comments
csv["author_rank"] = author_rank
csv["author_messges"] = author_messages
csv["author_reputation"] = author_reputation
csv["comment_text"] = comments
csv.to_csv("everyComment2.csv")
