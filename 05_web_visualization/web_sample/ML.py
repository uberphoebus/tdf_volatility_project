#Module Name : ML.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("titanic.csv")
print(df.info())
#Sex : 수치화
df['Sex'] = df['Sex'].apply(lambda x:1 if x=='Male' else 0)
#결측처리
df.fillna(0, inplace=True)
답안지 = df["Survived"]
문제지 = df[["Pclass","Sex", "Age", "SibSp","Parch"]]

print("-----문제지  가공 후 --------")
print(문제지.info())
print(문제지.head())


from sklearn.model_selection import train_test_split
문제지70, 문제지30, 답안지70, 답안지30 = \
    train_test_split(문제지, 답안지, test_size=0.3, random_state=11)


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(문제지70, 답안지70)         #학습 =========================
컴퓨터답안 = model.predict(문제지30)   #시험(예측) =========================


from sklearn.metrics import accuracy_score
score = accuracy_score(답안지30, 컴퓨터답안)
print("정확도:", score)


import pickle
pickle.dump(model, open('mymodel.pkl', 'wb'))
# model.save('mymodel.h5')

