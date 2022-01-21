import pandas as pd
import numpy as np
from PIL import Image

directory = 'F:/workspace/venv/codes/projects_final/final_re/web_1129_2'

def get1_1(gp):
    df = pd.read_csv(directory + '/static/br_img/returns_hv.csv')
    
    if gp == 'att':
        bench = df['bench_att'].values.tolist()
        rb    = df['bt_att'].values.tolist()
    elif gp == 'neu':
        bench = df['bench_neu'].values.tolist()
        rb    = df['bt_neu'].values.tolist()
    elif gp == 'def':
        bench = df['bench_def'].values.tolist()
        rb    = df['bt_def'].values.tolist()
    return bench, rb

def get1_2(gp):
    df = pd.read_csv(directory + '/static/br_img/returns_hv.csv')
    if gp == 'att':
        bench = df['bench_att_HV'].values.tolist()
        rb    = df['bt_att_hv'].values.tolist()
    elif gp == 'neu':
        bench = df['bench_neu_HV'].values.tolist()
        rb    = df['bt_neu_hv'].values.tolist()
    elif gp == 'def':
        bench = df['bench_def_HV'].values.tolist()
        rb    = df['bt_def_hv'].values.tolist()
    return bench, rb

def get1_3(gp):
    if gp == 'att':
        img = Image.open(directory + '/static/br_img/mdd_att_2021-11-27.png')
    elif gp == 'neu':
        img = Image.open(directory + '/static/br_img/mdd_neu_2021-11-27.png')
    elif gp == 'def':
        img = Image.open(directory + '/static/br_img/mdd_def_2021-11-27.png')
    return img

def get2_1(gp):
    if gp == 'att':
        img = Image.open(directory + '/static/br_img/rb_att_2021-11-27.png')
    elif gp == 'neu':
        img = Image.open(directory + '/static/br_img/rb_neu_2021-11-27.png')
    elif gp == 'def':
        img = Image.open(directory + '/static/br_img/rb_def_2021-11-27.png')
    return img

def get3(gp):
    df = pd.read_csv(directory + '/static/br_img/result.csv')
    if gp == 'att':
        res = df.loc[:, ['bench_att', 'rb_att']]
        res['ind'] = ['Total Return', 'CAGR', 'MDD', 'CALMR', 'Yearly Sharpe', 'Yearly Mean', 'Yearly Vol']
        res = res.values
    elif gp == 'neu':
        res = df.loc[:, ['bench_neu', 'rb_neu']]
        res['ind'] = ['Total Return', 'CAGR', 'MDD', 'CALMR', 'Yearly Sharpe', 'Yearly Mean', 'Yearly Vol']
        res = res.values
    elif gp == 'def':
        res = df.loc[:, ['bench_def', 'rb_def']]
        res['ind'] = ['Total Return', 'CAGR', 'MDD', 'CALMR', 'Yearly Sharpe', 'Yearly Mean', 'Yearly Vol']
        res = res.values
    return res

print(get1_1('att'))