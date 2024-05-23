import requests
def test_connection():    
    print('__________Connection to API Server_____________')
    req_post = requests.post(   url     = 'http://13.92.86.145:5677/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = '{"inputs": {"umap_x": [".3"], "umap_y": [".3"]}}' )
    is_connected = req_post.ok
    if is_connected : print('OK : Connected to API Server')
    assert is_connected

