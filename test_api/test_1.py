import requests
def test_connection():    
    print('__________Connection to API Server_____________')
    req_post = requests.post(   url     = 'http://13.92.86.145:5677/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = '{"inputs": {"CODE_GENDER_M":1,"NAME_CONTRACT_TYPE_Cash_loans":1,"NAME_EDUCATION_TYPE_Lower_secondary":0,"EXT_SOURCE_3":1.0,"NAME_EDUCATION_TYPE_Higher_education":1,"NAME_EDUCATION_TYPE_Secondary_or_secondary_special":0}}' )  
    is_connected = req_post.ok
    if is_connected : print('OK : Connected to API Server')
    assert is_connected

