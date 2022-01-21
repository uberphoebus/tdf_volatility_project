from typing import final
from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from PIL import Image


# path = "./static/images/graph"
# if os.path.exists(path):
#     os.makedirs(path)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', CHART1=list)


import final_func
@app.route('/page2', methods=['POST'])
def page2():
    if request.method == 'POST':
        form = request.form

    form_gp = form['options']

    if form_gp == '1_1':
        return_gp = 'att'
    elif form_gp == '1_2':
        return_gp = 'neu'
    elif form_gp == '1_3':
        return_gp = 'def'

    bench, rb   = final_func.get1_1(gp=return_gp)
    bench2, rb2 = final_func.get1_2(gp=return_gp)

    if return_gp == 'att':
        IMG_DIR  = 'br_img/mdd_att_2021-11-27.png'
        IMG_DIR2 = 'br_img/rb_att_2021-11-27.png'
    elif return_gp == 'neu':
        IMG_DIR  = 'br_img/mdd_neu_2021-11-27.png'
        IMG_DIR2 = 'br_img/rb_neu_2021-11-27.png'
    elif return_gp == 'def':
        IMG_DIR  = 'br_img/mdd_def_2021-11-27.png'
        IMG_DIR2 = 'br_img/rb_def_2021-11-27.png'
    
    DF5 = final_func.get3(gp=return_gp)

    ARR5 = DF5[:, 0].tolist()
    ARR6 = DF5[:, 1].tolist()
    
    
    return render_template(
        'index2.html', 
        BENCH=bench,
        RB=rb, 
        BENCH2=bench2, 
        RB2=rb2, 
        IMG_DIR=IMG_DIR,
        IMG_DIR2=IMG_DIR2, 
        DF5=DF5, 
        ARR5=ARR5, 
        ARR6=ARR6, 
    )

# a = final_func.get3(gp='att')[:, 0].tolist()
# print(a)

# print(final_func.get3('neu'))

# @app.route('/page3')
# def page3():
#     return render_template('index3.html')

# @app.route('/main_menu1', methods=['GET'])
# def main_menu1():
#     pass

# print(rb5)
# #---------------------------------
# @app.route('/go_rest', methods=['POST'])
# def go_rest():

#     a1 = request.form["Price"]
#     a2 = request.form["GlidePath"]
#     a3 = request.form["STDEV"]

#     a1 = int(a1)
#     a3 = int(a3)

#     print(a1, a2, a3)
#     # model_load
#     # res = m.predict(xxxxxxx)
#     global go_res
#     global test_df
#     res = "0.684"
#     test_df = pd.DataFrame({"name":['a','b','c'], "score":[1,2,3]})
#     return "ok"
#     # render_list = []
#     # render_list.append(res)
#     # render_list.append(test_df)
#     # return render_list

# #---------------------------------------------
# # http://127.0.0.1:8088/go_rest3
# @app.route('/go_popup', methods=['POST'])
# def go_popup():
#     return render_template('popup.html', MY_RES=res, MY_DF=test_df)


# @app.route('/predict', methods=['POST'])
# def predict():
#     a1 = request.form["Price"]
#     a2 = request.form["GlidePath"]
#     a3 = request.form["STDEV"]


#     a1 = int(a1)
#     a3 = int(a3)
#     # if a2 == 'attack':
#     #
#     # elif a2 == 'neutral':
#     #     pass
#     # elif a2 == 'depens':
#     #     pass
#     # else:
#     #     pass

#     print(a1, a2, a3)
#     #model_load
#     #res = m.predict(xxxxxxx)
#     res = "0.684"
#     return render_template('result.html', MYKEY=res)

#-------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    # app.run(host="127.0.0.1", port="5000", debug=True)
