import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")
print(df)

NaN = df["director"].isnull().sum()


countries = []
i = ""
for i in df[df.director.isnull()]["country"].values:
    a = []
    try:
        a = i.replace(" ","").split(",")
        for i in a:
            countries.append(i)
    except AttributeError:
        a = []
d = dict()
for i in countries:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
sorted_keys = sorted(d.items(), key=lambda x: x[1], reverse=True)

df = pd.DataFrame(sorted_keys).head()

plt.bar(df[0],df[1])
plt.title("Страны без режиссеров",fontweight="bold")
plt.xlabel('страны')
plt.ylabel('количество')


def autolabel(rects, labels=None, height_factor=1.01):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if labels is not None:
            try:
                label = labels[i]
            except (TypeError, KeyError):
                label = ' '
        else:
            label = '%d' % int(height)
        ax.text(rect.get_x() + rect.get_width()/2., height_factor*height,
                '{}'.format(label),
                ha='center', va='bottom')

ax = plt.gca()
autolabel(ax.patches, df[1], height_factor=1.01)

plt.show()



df = pd.read_csv("netflix_titles.csv")
countries = []
i = ""
for i in df["country"].values:
    a = []
    try:
        a = i.replace(" ","").split(",")
        for i in a:
            countries.append(i)
    except AttributeError:
        a = []
d = dict()
for i in countries:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1

sorted_keys = sorted(d.items(), key=lambda x: x[1], reverse=True)
df = pd.DataFrame(sorted_keys).head()

colors = sns.color_palette('pastel')[0:5]
plt.pie(df[1],labels=df[0],autopct='%1.2f%%',colors = colors)

plt.title("Топ по количеству",fontweight="bold",family = 'monospace')

plt.show()


df = pd.read_csv("netflix_titles.csv")
countries = []
i = ""
for i in df["rating"].values:
    a = []
    try:
        a.append(i)
        for i in a:
            countries.append(i)
    except AttributeError:
        a = []
d = dict()
for i in countries:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
sorted_keys = d.items()
df1 = pd.DataFrame(sorted_keys)
df1.columns = ['a', 'b']
df1 = df1.query("b > 50")




plt.subplot(121)
plt.title("Рейтинг")
plt.pie(df1["b"],labels=df1["a"], autopct='%1.1f%%', shadow=True, wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"}, rotatelabels=True)
plt.subplot(122)





countries = []
for i in df[df.rating == "TV-MA"]["country"].values:
    a = []
    try:
        a = i.replace(" ","").split(",")
        for i in a:
            countries.append(i)
    except AttributeError:
        a = []
d = dict()
for i in countries:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
sorted_keys = sorted(d.items(), key=lambda x: x[1], reverse=True)



df2 = pd.DataFrame(sorted_keys)
df3 = df2
for ind, rows in df2.iterrows():
    if ind>2:
        print(ind)
        df3.drop(index = ind,inplace = True)
print(df3)
df3.columns = ['a', 'b']
plt.title("количество")
plt.bar(df3["a"],df3["b"])
ax.yaxis.set_ticks_position('right')
ax.set_xlabel('', visible=False)
ax.set_ylabel('Количество фильмов')
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
plt.show()



##############################################3
print(df["date_added"])
df["date_added"] = pd.to_datetime(df['date_added'])
df['year'] = pd.DatetimeIndex(df['date_added']).year
df['month'] = pd.DatetimeIndex(df['date_added']).month


countries = []
for i in df["month"].values:
    a = []
    try:
        countries.append(i)
    except AttributeError:
        a = []
d = dict()
for i in countries:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
sorted_keys = d.items()
df1 = pd.DataFrame(sorted_keys)
df1 = df1.dropna()
plt.plot(df1[1], 'rx', df1[1],  'b+', linestyle='solid')
plt.title("Фильмы по месяцам",fontweight="bold")
plt.xlabel('месяцы')
plt.ylabel('количество')
plt.xticks(np.arange(1, 13, step=1))
plt.show()

print(df["year"])

countries = []
for i in df["year"].values:
    a = []
    try:
        countries.append(i)
    except AttributeError:
        a = []
d = dict()
for i in countries:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
sorted_keys = d.items()
df = pd.DataFrame(sorted_keys)
df = df.dropna()
plt.plot(df[1], 'rx', df[1], linestyle='dashed')
plt.title("Фильмы по годам",fontweight="bold")
plt.xlabel('годы')
plt.ylabel('количество')
plt.show()

df = pd.read_csv("netflix_titles.csv")



###################################
import re
countries = []
for i in df["duration"].values:
    a = ""
    try:
        a = i
        re.search("min",a).group(0)
        a = a.split(" ")
        countries.append(a[0])
    except AttributeError:
        a = []
sorted_keys = countries
df["mins"] = pd.DataFrame(sorted_keys)



countries = []
for i in df["duration"].values:
    a = ""
    try:
        a = i
        re.search("Season",a).group(0)
        a = a.split(" ")
        countries.append(a[0])
    except AttributeError:
        a = []

sorted_keys = countries
df["seasons"] = pd.DataFrame(sorted_keys)

df2 = df["seasons"]
df2 = df2.dropna()
df1 = df["mins"]
df1 = df1.dropna()
print(df1)
plt.subplot(121)
plt.hist(df1)
plt.title("минуты",fontweight="bold")
plt.xlabel('годы')
plt.ylabel('минуты')
plt.subplot(122)
plt.title("cезоны",fontweight="bold")
plt.xlabel('годы')
plt.ylabel('сезоныо')
plt.hist(df2)
plt.show()

print(df1)
df1 = df1.astype('float')
df = df.astype('float')
plt.boxplot(df1, x = df["seasons"])
plt.show()
