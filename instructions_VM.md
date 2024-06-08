## MS Azure
### Cost Analysis
- [Custom: Cost analysis - Microsoft Azure](https://portal.azure.com/#view/Microsoft_Azure_CostManagement/CostAnalysis/scope/%2Fproviders%2FMicrosoft.Billing%2FbillingAccounts%2F688e2018-b916-5441-11ec-c59b7772b9e9%3A395c7ee6-4f61-4267-9133-62fa7b59675a_2019-05-31/isAcmContext~/true/viewId/%2Fproviders%2FMicrosoft.Billing%2FbillingAccounts%2F688e2018-b916-5441-11ec-c59b7772b9e9%3A395c7ee6-4f61-4267-9133-62fa7b59675a_2019-05-31%2Fproviders%2FMicrosoft.CostManagement%2Fviews%2Fms%3ADailyCosts/openByNewTab~/true)

### Create a VM
  - [_Use the Azure CLI to create a Linux VM | Microsoft Learn_](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli)
  - Choose Standard D4s_v3 (4CPU 16Gb)
### Access CLI Terminal
  - [_Azure CLI_](https://shell.azure.com/bash)

## File Transfer

### From Google-Drive
- Share file by link
- Extract G-Doc ID from URL
    - https://colab.research.google.com/drive/ 1EPC7oDf6wZNdxx1X_bFO_vF6Z6uwhpse ?usp=drive_link
- Download file
```
wget --no-check-certificate 'https://drive.google.com/uc?export=download&id=1EPC7oDf6wZNdxx1X_bFO_vF6Z6uwhpse' -O Jean_Vallée_2_notebook_modelisation_042024.ipynb
```
## Azure CLI Terminal

### Access VM
```
ssh jvisa4031@4.233.201.217
```

## VM (Virtual Machine)

### Installation de Python
Cf. _§Python install_ in [_How to Setup MLflow On Azure | Medium_](https://medium.com/swlh/how-to-setup-mlflow-on-azure-5ba67c178e7d)
```
sudo apt update
python3 --version
sudo apt install python3-pip
pip install virtualenv
sudo apt install python3.10-venv
# sudo apt install sqlite         # for jupyter history
```
### Create Inbound port rule
[myVM063b54 - Microsoft Azure](https://portal.azure.com/#@jvisa4031gmail.onmicrosoft.com/resource/subscriptions/a49ee12c-d832-486e-97d4-f71b6df0169e/resourceGroups/myVMResourceGroup063b54/providers/Microsoft.Compute/virtualMachines/myVM063b54/networkSettings)

### Check open ports
```
sudo apt install net-tools
netstat -tunlp | grep "0:[56]"
```

### Create Virtual Environment
```
mkdir environments_folder/
cd environments_folder
sudo apt-get update
# sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv my_env
```

### Access Virtual Environment
```
source ~/environments_folder/my_env/bin/activate
```

## Python Virtual Environment

### Notebook Jupyter

#### Install 
```
pip3 install jupyter
pip3 install ipykernel
ipython kernel install --user --name=my_env
```

#### Launch 
```
nohup jupyter notebook --no-browser  --ip=0.0.0.0 --port=5555 &
ps aux | grep "jupyter" | grep -v "grep"
```

#### Access online
On Browser
- First connection :http://4.233.201.217:5555/tree?token=####
- [List of notebooks](http://4.233.201.217:5555/tree)

### SSH Tunnels
```
# Jupyter
nohup ssh -N -L 5555:localhost:5555 jvisa4031@4.233.201.217 &
# Flask webapp
nohup ssh -N -L 6543:localhost:6543 jvisa4031@4.233.201.217 &
```

## Git

### Clone project
```
git clone https://github.com/JeanRosselVallee/project_7
```

### Configuration
```
cd ./project_7/
git config --global user.email "jv.isa4031@gmail.com" 
git config --global user.name "JeanRosselVallee"
git remote rm origin
git remote add origin https://JeanRosselVallee:github_pat_####@github.com/JeanRosselVallee/project_7.git
git remote -v
```

### Publish
```
cd ./project_7/
git pull origin main
git status
git add .
git commit -m "Commit message"
git push origin main
```

## SMTP mail
Send alerts from VM to : jv.virtualm@gmail.com

### Instructions 
Cf. [Configure Postfix to Send Email with Gmail's SMTP From the Terminal](https://dev.to/chigozieco/configure-postfix-to-send-email-with-gmails-smtp-from-the-terminal-4cco)

### Configure G-Account
- Create app password at App Passwords 
- App name = SendAlert

### Install postfix
- system mail name FQDN : VM01.zythql44tdxu1oosyti1qz3pfa.parx.internal.cloudapp.net
- contents of  /etc/postfix/sasl/sasl_passwd :
  - [smtp.gmail.com]:465 jv.virtualm@gmail.com:davi ugnz tjlm cjij
- certificate exists : /etc/ssl/certs/ca-certificates.crt
- correction : sudo ufw allow "postfix SMTP"

### SHELL Commands
```
sudo apt install mailutils
sudo vi /etc/postfix/sasl/sasl_passwd
cat /etc/postfix/sasl/sasl_passwd
sudo postmap /etc/postfix/sasl/sasl_passwd
sudo chmod 600 /etc/postfix/sasl/sasl_passwd /etc/postfix/sasl/sasl_passwd.db
sudo vi /etc/postfix/main.cf
ls /etc/ssl/certs/ca-certificates.crt
sudo systemctl restart postfix
sudo ufw status
sudo ufw allow "Postfix"
sudo ufw allow "postfix SMTPS"
sudo ufw allow "Postfix Submission"
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
nohup ssh -N -L 465:localhost:465 jvisa4031@4.233.201.217 &
ps aux | grep ssh | grep 465
netstat tuln | grep 465
sudo vi ~/.bashrc
source ~/.bashrc
echo "ML Model - score decreased" | mailx -s "Model performance decay" jv.virtualm@gmail.com
```

### Open port




## Ngrok
In a Notebook : 
```
# create remote tunnel using ngrok.com to allow local port access
# borrowed from https://colab.research.google.com/github/alfozan/MLflow-GBRT-demo/blob/master/MLflow-GBRT-demo.ipynb#scrollTo=4h3bKHMYUIG6
!pip install pyngrok --quiet
from pyngrok import ngrok
# Terminate open tunnels if any exist
ngrok.kill()
# Setting the authtoken (optional)
# Get your authtoken from https://dashboard.ngrok.com/auth
ngrok.set_auth_token('#######')

# Open an HTTPs tunnel on port 5000 for http://localhost:5000
ngrok_tunnel = ngrok.connect(addr="5000", proto="http", bind_tls=True) #(port='5001', proto="http", options={'bind_tls': True})
print('MLflow Tracking UI:', ngrok_tunnel.public_url)
```