
from flask import Flask, render_template, request
import requests
import json
import subprocess

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

@app.route('/deploy_to_staging/')                         # deploy to Staging
def deploy():
    str_output  = 'Git Pull Model:\n' + pull()             # phase_1 git pull model
    str_output += 'Restart Server:\n' + restart()          # phase_2 restart model server
    return str_output
def pull():
    dir_root = '/home/azureuser/project_7/'
    str_command_pull = 'cd ' + dir_root + ' ; git pull origin main'
    str_output = run_shell(str_command_pull)
    return str_output
def restart():
    port_staging_server = '5677'
    str_command_serve = 'mlflow models serve -m ../api/staging_model/ -p ' + port_staging_server + ' -h 0.0.0.0 --no-conda &'
    str_command_ps = 'ps aux | grep  ":' + port_staging_server + '" | grep -v grep | awk \'{print $2, $15, $19}\' '
    str_output = 'Process BEFORE Restart:\n'             # check process BEFORE restart
    str_output += run_shell(str_command_ps)
    run_shell('pkill -f ":' + port_staging_server + '" ; sleep 1')     # RESTART
    subprocess.Popen(str_command_serve, start_new_session=True, shell=True)
    str_output += 'Process AFTER Restart:\n'           # check process AFTER restart
    str_output += run_shell('sleep 4 ; ' + str_command_ps)
    return str_output
def run_shell(command):
    shell_process = subprocess.run([command], shell=True, capture_output=True, text=True)
    return str(shell_process.stdout) + str(shell_process.stderr)
