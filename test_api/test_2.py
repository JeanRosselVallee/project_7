
import requests
import pandas as pd
import json

def test_predict():
    dict_inputs = {"index": [2291, 2292, 2293], "columns": ["CODE_GENDER_M", "NAME_CONTRACT_TYPE_Cash_loans", "EXT_SOURCE_3", "NAME_EDUCATION_TYPE_Higher_education", "EXT_SOURCE_2", "FLAG_OWN_CAR", "NAME_EDUCATION_TYPE_Secondary_or_secondary_special"], "data": [[1, 1, 0.4740512892789932, 0, 0.3147092250216505, False, 1], [0, 1, 0.1595195404777181, 1, 0.3225519037906617, True, 0], [0, 1, 0.1261005588362325, 0, 0.3007587165928464, False, 1]]}                  # input observations      
    df_result_grid = pd.DataFrame(data=dict_inputs['data'], columns=dict_inputs['columns'])
    df_result_grid['target'] = [1, 1, 1]      # expected output

    # Send input data to prediction API via POST request 
    req_post = requests.post(   url     = 'http://4.233.201.217:5677/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = '{"dataframe_split": {"index": [2291, 2292, 2293], "columns": ["CODE_GENDER_M", "NAME_CONTRACT_TYPE_Cash_loans", "EXT_SOURCE_3", "NAME_EDUCATION_TYPE_Higher_education", "EXT_SOURCE_2", "FLAG_OWN_CAR", "NAME_EDUCATION_TYPE_Secondary_or_secondary_special"], "data": [[1, 1, 0.4740512892789932, 0, 0.3147092250216505, false, 1], [0, 1, 0.1595195404777181, 1, 0.3225519037906617, true, 0], [0, 1, 0.1261005588362325, 0, 0.3007587165928464, false, 1]]} }' )
    
    dict_predicted = json.loads(req_post.text)  # output predictions {'predictions': [1, 1, 1]}

    
    print(dict_predicted)

    
    df_result_grid['prediction'] = dict_predicted['predictions']
    print(df_result_grid.round(3).T)            # results as pandas

    # Compare predicted vs. expected values
    assert df_result_grid['prediction'].equals(df_result_grid['target'])

