import requests
def test_connection():    
    print('__________Connection to API Server_____________')
    req_post = requests.post(   url     = 'http://4.233.201.217:5677/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = '{"dataframe_split": {"index": [0], "columns": ["CODE_GENDER_M", "EXT_SOURCE_3", "EXT_SOURCE_2", "NAME_EDUCATION_TYPE_Secondary_or_secondary_special", "NAME_EDUCATION_TYPE_Higher_education", "NAME_CONTRACT_TYPE_Cash_loans", "NAME_INCOME_TYPE_Working"], "data": [[1, 0.2020866016820394, 0.5806283658626501, 1, 0, 1, 1]]} }' )
    # Evaluation of response
    is_connected = req_post.ok
    if is_connected : print('OK : Connected to API Server & validated input format')
    assert is_connected

