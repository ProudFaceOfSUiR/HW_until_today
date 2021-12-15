import pandas as pd
df1 = pd.read_csv("everyComment2.csv")
df2 = pd.read_csv("forum2.csv")
print(df1.columns)
print(df2.columns)
column_titles = []
df2 = df2[['Unnamed: 0', 'comment_text', 'author_rank', 'author_messges',
       'author_reputation']]
print(df2.columns)

#csv = pd.read_csv("forum3.csv")
#print(csv.values)
df1 = pd.read_csv("everyComment2.csv")
df2 = pd.read_csv("forum2.csv")
fh = open("forum3.csv")
a = fh.read()
#print(a)

def change_month(str):
    str = str.replace("января", ".01.")
    str = str.replace("февраля", ".02.")
    str = str.replace("марта", ".03.")
    str = str.replace("апреля", ".04.")
    str = str.replace("мая", ".05.")
    str = str.replace("июля", ".07.")
    str = str.replace("июня", ".06.")
    str = str.replace("августа", ".08.")
    str = str.replace("сентября", ".09.")
    str = str.replace("октября", ".10.")
    str = str.replace("ноября", ".11.")
    str = str.replace("декабря", ".12.")
    return str

a = change_month(a)
#print(a)
fh.close()
fh =open("new_forum3.csv", "w")
fh.write(a)
fh.close()
df3 = pd.read_csv('new_forum3.csv')
frames = [df1 ,df3,df2 ]
csv = pd.concat(frames)
print(csv.columns)

csv = pd.read_csv("norm_date.csv")
felps = 0
for i in csv["comment_text"].str.contains('фелпс'):
    if i:
        felps+=1

for i in csv["comment_text"].str.contains('Фелпс'):
    if i:
        felps+=1


for i in csv["comment_text"].str.contains('Felps'):
    if i:
        felps+=1

for i in csv["comment_text"].str.contains('felps'):
    if i:
        felps+=1

print("Felps " + str(felps))
popov = 0
for i in csv["comment_text"].str.contains('Попов'):
    if i:
        popov+=1


for i in csv["comment_text"].str.contains('попов'):
    if i:
        popov+=1

print("Popov "+str(popov))

rylov = 0
for i in csv["comment_text"].str.contains('Рылов'):
    if i:
        rylov+=1

for i in csv["comment_text"].str.contains('рылов'):
    if i:
        rylov+=1
print("Rylov "+str(rylov))
medvedeva = 0
for i in csv["comment_text"].str.contains('Медведев'):
    if i:
        medvedeva+=1

for i in csv["comment_text"].str.contains('медведев'):
    if i:
        medvedeva+=1
print("Medvedeva "+str(medvedeva))

#print(df["date_added"])
df = csv

df["date"] = pd.to_datetime(df['date'])
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
df['day'] = pd.DatetimeIndex(df['date']).day
df.to_csv("norm_date.csv")

print(df.columns)
print(df.values)




