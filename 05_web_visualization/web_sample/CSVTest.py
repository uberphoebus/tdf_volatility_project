#Module name : CSVTest.py

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("mydb.db")
df = pd.read_csv("mycsv.csv")
print(df.head())
df.to_sql(name='user2', con=conn, if_exists='replace')

# plt.scatter(df.UID, df.UPW)
# plt.hist(df.UID)
sns.countplot(df.UID)
plt.show()

#sns.countplot(comp_df.Embarked)

