
import requests
import pandas as pd
import json

def test_predict():
    dict_inputs = {"index": [2582, 2583, 2584], "columns": ["NAME_EDUCATION_TYPE_Higher_education", "EXT_SOURCE_3", "EXT_SOURCE_2", "CODE_GENDER_M", "NAME_EDUCATION_TYPE_Secondary_or_secondary_special", "NAME_CONTRACT_TYPE_Cash_loans", "NAME_INCOME_TYPE_Working"], "data": [[0, 0.3944954053123993, 0.2731892846252296, 0, 1, 1, 1], [0, 0.1566398270314114, 0.5342365946929042, 1, 1, 1, 0], [0, 0.1176137317080569, 0.4562911010223129, 0, 1, 1, 0]]}                     # input observations      
    df_result_grid = pd.DataFrame(data=dict_inputs['data'], columns=dict_inputs['columns'])
    df_result_grid['target'] = [1, 1, 1]      # expected output

    # Send input data to prediction API via POST request 
    req_post = requests.post(   url     = 'http://4.233.201.217:5677/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = '{"dataframe_split": {"index": [2582, 2583, 2584], "columns": ["NAME_EDUCATION_TYPE_Higher_education", "EXT_SOURCE_3", "EXT_SOURCE_2", "CODE_GENDER_M", "NAME_EDUCATION_TYPE_Secondary_or_secondary_special", "NAME_CONTRACT_TYPE_Cash_loans", "NAME_INCOME_TYPE_Working"], "data": [[0, 0.3944954053123993, 0.2731892846252296, 0, 1, 1, 1], [0, 0.1566398270314114, 0.5342365946929042, 1, 1, 1, 0], [0, 0.1176137317080569, 0.4562911010223129, 0, 1, 1, 0]]} }' )
    
    dict_predicted = json.loads(req_post.text)  # output predictions {'predictions': [1, 1, 1]}
    df_result_grid['prediction'] = dict_predicted['predictions']
    print(df_result_grid.round(3).T)            # results as pandas

    # Compare predicted vs. expected values
    assert df_result_grid['prediction'].equals(df_result_grid['target'])

