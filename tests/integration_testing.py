import requests
import pandas as pd
import json
import sys


def generate_url(name1, volume1, name2, volume2, local=True):
    if local == "False":
        print('Testing gcp environment')
        url = f'https://northamerica-northeast1-durable-cacao-374303.cloudfunctions.net/crude?name1={name1}&volume1={volume1}&name2={name2}&volume2={volume2}&json_y=y'
    else:
        print('Testing local environment')
        url = f'http://127.0.0.1:8080/?name1={name1}&volume1={volume1}&name2={name2}&volume2={volume2}&json_y=y'
    print(url)
    return url


def compare_result(true_y, pred_y):
    df = pd.DataFrame([true_y, pred_y]).T
    df.columns = ['true','pred']
    df['diff'] = df.apply(lambda x: abs(x['true']-x['pred']),axis=1)
    mae = df['diff'].sum()/21
    print ('Mean absolute error is:', mae )
    return mae

name1 = "Pembina"
name2 = "Fort Hills Dilbit"
volume1 = 1
volume2 = 2

def test_case_1(name1='Pembina', volume1=1, name2='Fort_Hills_Dilbit', volume2=0, local=True):
    url = generate_url(name1, volume1, name2, volume2, local)
    true_y = {
        "0": 34.1,
        "5": 52.7,
        "10": 92.5,
        "15": 111.6,
        "20": 135.7,
        "25": 159.2,
        "30": 180.6,
        "35": 206.9,
        "40": 235.5,
        "45": 266.9,
        "50": 298.7,
        "55": 327.8,
        "60": 360.3,
        "65": 394.2,
        "70": 427.4,
        "75": 461.5,
        "80": 508.5,
        "85": 565.2,
        "90": 644.4,
        "95": 690.4,
        "99": 690.4
    }
    pred_y = json.loads(requests.get(url).text)
    compare_result(true_y, pred_y)
    print('Test case 1 is successfully completed.')
    
def test_case_2(name1='Pembina', volume1=0, name2='Syncrude_Sweet_Premium', volume2=1, local=True):
    url = generate_url(name1, volume1, name2, volume2, local)
    true_y = {
        "0": 34.7,
        "5": 102.5,
        "10": 143.7,
        "15": 182,
        "20": 213.7,
        "25": 239.4,
        "30": 261.8,
        "35": 282.1,
        "40": 300.3,
        "45": 317.2,
        "50": 334.2,
        "55": 351,
        "60": 366.9,
        "65": 383.5,
        "70": 400.5,
        "75": 416.6,
        "80": 431.9,
        "85": 452.1,
        "90": 475.5,
        "95": 508.2,
        "99": 583.7
    }
    pred_y = json.loads(requests.get(url).text)
    compare_result(true_y, pred_y)
    print('Test case 2 is successfully completed.')

local = sys.argv[1]
test_case_1(local=local)
test_case_2(local=local)
