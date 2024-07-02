
import requests
import pandas as pd
import json

def test_predict():
    dict_inputs = {"index": [2355, 2356, 2357], "columns": ["CODE_GENDER_M", "EXT_SOURCE_3", "EXT_SOURCE_2", "NAME_EDUCATION_TYPE_Secondary_or_secondary_special", "NAME_EDUCATION_TYPE_Higher_education", "NAME_CONTRACT_TYPE_Cash_loans", "NAME_INCOME_TYPE_Working"], "data": [[0, 0.2188590822283744, 0.5886784110239339, 1, 0, 1, 1], [1, 0.5108529061799658, 0.3679405554386685, 1, 0, 1, 1], [0, 0.0701088438273582, 0.0301835652520893, 0, 1, 1, 0]]}                  # input observations      
    df_result_grid = pd.DataFrame(data=dict_inputs['data'], columns=dict_inputs['columns'])
    df_result_grid['target'] = [1, 1, 1]      # expected output

    # Send input data to prediction API via POST request 
    req_post = requests.post(   url     = 'http://4.233.201.217:5677/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = '{"dataframe_split": {"index": [2355, 2356, 2357], "columns": ["CODE_GENDER_M", "EXT_SOURCE_3", "EXT_SOURCE_2", "NAME_EDUCATION_TYPE_Secondary_or_secondary_special", "NAME_EDUCATION_TYPE_Higher_education", "NAME_CONTRACT_TYPE_Cash_loans", "NAME_INCOME_TYPE_Working"], "data": [[0, 0.2188590822283744, 0.5886784110239339, 1, 0, 1, 1], [1, 0.5108529061799658, 0.3679405554386685, 1, 0, 1, 1], [0, 0.0701088438273582, 0.0301835652520893, 0, 1, 1, 0]]} }' )
    
    dict_predicted = json.loads(req_post.text)  # output predictions {'predictions': [1, 1, 1]}

    
    print(dict_predicted)

    
    df_result_grid['prediction'] = dict_predicted['predictions']
    print(df_result_grid.round(3).T)            # results as pandas

    # Compare predicted vs. expected values
    assert df_result_grid['prediction'].equals(df_result_grid['target'])

