import requests
def test_connection():    
    print('__________Connection to API Server_____________')
    req_post = requests.post(   url     = 'http://4.233.201.217:5677/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = '{"dataframe_split": {"index": [0], "columns": ["CODE_GENDER_M", "NAME_CONTRACT_TYPE_Cash_loans", "EXT_SOURCE_3", "NAME_EDUCATION_TYPE_Higher_education", "EXT_SOURCE_2", "FLAG_OWN_CAR", "NAME_EDUCATION_TYPE_Secondary_or_secondary_special"], "data": [[1, 1, 0.1176137317080569, 0, 0.7088758643589249, true, 1]]} }' )
    # Evaluation of response
    is_connected = req_post.ok
    if is_connected : print('OK : Connected to API Server & validated input format')
    assert is_connected

