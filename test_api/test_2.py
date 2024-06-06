import requests
import json

def predict(dict_features):
    # Send input data to prediction API
    req_post = requests.post(   url     = 'http://4.233.201.217:5677/invocations',
                                headers = {'Content-Type': 'application/json'},
                                data    = json.dumps({'inputs': dict_features}) )
    # Get predicted value from API
    dict_predicted = json.loads(req_post.text)
    return dict_predicted

def test_prediction():
    li_dict_features = [{"CODE_GENDER_M":0,"NAME_CONTRACT_TYPE_Cash_loans":1,"NAME_EDUCATION_TYPE_Lower_secondary":1,"EXT_SOURCE_3":0.1359510442,"NAME_EDUCATION_TYPE_Higher_education":0,"NAME_EDUCATION_TYPE_Secondary_or_secondary_special":0},{"CODE_GENDER_M":0,"NAME_CONTRACT_TYPE_Cash_loans":1,"NAME_EDUCATION_TYPE_Lower_secondary":1,"EXT_SOURCE_3":0.244516392,"NAME_EDUCATION_TYPE_Higher_education":0,"NAME_EDUCATION_TYPE_Secondary_or_secondary_special":0},{"CODE_GENDER_M":0,"NAME_CONTRACT_TYPE_Cash_loans":1,"NAME_EDUCATION_TYPE_Lower_secondary":1,"EXT_SOURCE_3":0.2485355573,"NAME_EDUCATION_TYPE_Higher_education":0,"NAME_EDUCATION_TYPE_Secondary_or_secondary_special":0}]
    li_targets = [1, 1, 1]
    for idx, (dict_features_i, out_i) in enumerate(zip(li_dict_features, li_targets)) :

        dict_predicted_i = predict(dict_features_i)
        dict_expected_i  = {'predictions':[out_i]}
        print('input features   :', dict_features_i)
        print('output predicted:', dict_predicted_i)
        print('output expected :', dict_expected_i)

        # Compare predicted & expected values
        assert dict_predicted_i == dict_expected_i

