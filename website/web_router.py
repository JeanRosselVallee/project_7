from flask import Flask, render_template, request
import requests
import json
import subprocess
 
def run_shell(command):
    shell_process = subprocess.run([command], shell=True, capture_output=True, text=True)
    return str(shell_process.stdout) + str(shell_process.stderr)
def pull():
    dir_root = '/home/azureuser/project_7/'
    str_command_pull = 'cd ' + dir_root + ' ; git pull origin main'
    str_output = run_shell(str_command_pull)
    return 'Git Pull Model:===============\n' + str_output
def restart(str_environment) : 
    if str_environment == 'staging'    : dir_model, port = '../api/staging_model/',    '5677'
    if str_environment == 'production' : dir_model, port = '../api/production_model/', '5678' 
    str_command_serve = 'mlflow models serve -m ' + dir_model + ' -p ' + port + ' -h 0.0.0.0 --no-conda &'
    str_command_ps = 'ps aux | grep  ":' + port + '" | grep -v grep | awk \'{print $2, $15, $19}\' '
    str_output = 'Process BEFORE Restart:\n'                    # check process BEFORE restart
    str_output += run_shell(str_command_ps)
    run_shell('pkill -f ":' + port + '" ; sleep 1')     # RESTART
    subprocess.Popen(str_command_serve, start_new_session=True, shell=True)
    str_output += 'Process AFTER Restart:\n'                    # check process AFTER restart
    str_output += run_shell('sleep 4 ; ' + str_command_ps)
    return 'Restart Server:===============\n' + str_output
def copy_model():
    str_command_cp = 'cp -rf ../api/staging_model/* ../api/production_model/ ; echo $?'
    str_output = run_shell(str_command_cp)
    return str_output

# WebApp Router
app = Flask(__name__)                                     

@app.route('/')                                           # Route Index
def index(): return render_template('index.html')         # renders HTML as string

@app.route('/form/')                                      # Route Form
def form(): return render_template('form.html')

@app.route('/result/', methods=['POST'])                  # Route Result (API prediction)
def result():    
    dict_features = request.form.to_dict(flat=False)      #{port:[...],feature:[value],...}
    port = dict_features.pop('port')[0]
    req_post = requests.post(   url     = 'http://localhost:' + str(port) + '/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = json.dumps({'inputs': dict_features}) )
    dict_prediction = json.loads(req_post.text)           # {predictions:[1]}
    return render_template('result.html', port=port, features=dict_features, target_value=dict_prediction)

@app.route('/deploy_to_staging/')                         # Deploys to Staging
def deploy_staging():
    str_output  = pull()                                        # phase_1 git pull model
    str_output += restart('staging')                            # phase_2 restart model server
    return str_output

@app.route('/deploy_to_production/')                      # Deploys to Production
def deploy_production():
    str_output  = 'Copy Model from Staging to Production:===================\n' 
    str_return_code = copy_model()                              # phase_1 copy model
    if str_return_code == '0\n' :
        str_output += 'OK: Model copied\n'
        str_output += restart('production')                     # phase_2 restart model server
    else : 
        str_output += 'ERROR: Model could NOT be copied'
    return str_output

@app.route('/report/')                                      # Route Report
def report(): return render_template('report.html')

@app.route('/report_simul/')                                # Route Report Simulation
def report_simul(): return render_template('report_simulation.html')
