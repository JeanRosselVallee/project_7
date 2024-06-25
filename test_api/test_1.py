import requests
def test_connection():    
    print('__________Connection to API Server_____________')
    req_post = requests.post(   url     = 'http://4.233.201.217:5677/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = '{"dataframe_split": {"index": [0], "columns": ["NAME_EDUCATION_TYPE_Higher_education", "EXT_SOURCE_3", "EXT_SOURCE_2", "CODE_GENDER_M", "NAME_EDUCATION_TYPE_Secondary_or_secondary_special", "NAME_CONTRACT_TYPE_Cash_loans", "NAME_INCOME_TYPE_Working"], "data": [[0, 0.5638350489514956, 0.3058183171273599, 0, 1, 1, 1]]} }' )
    # Evaluation of response
    is_connected = req_post.ok
    if is_connected : print('OK : Connected to API Server & validated input format')
    assert is_connected

