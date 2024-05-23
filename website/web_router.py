
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__) # get work dirs

@app.route('/')                                           # index
def index():
    return render_template('index.html') # HTML as string

@app.route('/form/')                                      # form
def form():
    return render_template('form.html')

@app.route('/result/', methods=['POST'])                  # result predicted by API
def result():    
    dict_features = request.form.to_dict(flat=False) #{port:[5678],umap_x:[.3],umap_y:[.3]}
    port = dict_features.pop('port')[0]
    req_post = requests.post(   url     = 'http://localhost:' + str(port) + '/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = json.dumps({'inputs': dict_features}) )
    dict_prediction = json.loads(req_post.text)     #{predictions:[1]}
    return render_template('result.html', port=port, features=dict_features, target_value=dict_prediction)

@app.route('/deploy/')                                    # deploy
def deploy():
    import subprocess
    status_phase_1 = '1. Git Pull'
    dir_root = '/home/azureuser/project_7/'
    shell_command = 'cd ' + dir_root + ' ; git pull origin main'
    shell_process = subprocess.run([shell_command], shell=True, capture_output=True, text=True)
    return shell_process.stdout + shell_process.stderr

