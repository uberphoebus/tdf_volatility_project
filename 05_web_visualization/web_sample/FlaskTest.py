#Module Name : FlaskTest.py

from flask import Flask, render_template, request
import numpy as np
import pickle
from sklearn.metrics import accuracy_score

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/predict')
@app.route("/predict", methods=['POST'])
def titanic_predict():
    # res = 모델 예측 "Pclass","Sex", "Age", "SibSp","Parch"
    a1 = request.form["Pclass"]
    a2 = request.form["Sex"]
    a3 = request.form["Age"]
    a4 = request.form["SibSp"]
    a5 = request.form["Parch"]
    ff = request.form["Myfile"]
    print(ff)


    list = [a1, a2, a3, a4, a5]
    문제지1 = np.array(list).reshape(1,-1)

    #학습 완료 후 저장했던 모델 불러들이기
    model = pickle.load(open('mymodel.pkl', 'rb'))
    computer_answer = model.predict(문제지1)  # 시험(예측) =========================

    return render_template('result.html', MYRESULT=computer_answer, CHART='/static/chartimg/aa_chart.jpg')


if __name__ == '__main__':
    app.debug = True
    app.run(port=9999)
