## MS Azure
### Cost Analysis
- [Custom: Cost analysis - Microsoft Azure](https://portal.azure.com/#view/Microsoft_Azure_CostManagement/CostAnalysis/scope/%2Fproviders%2FMicrosoft.Billing%2FbillingAccounts%2F688e2018-b916-5441-11ec-c59b7772b9e9%3A395c7ee6-4f61-4267-9133-62fa7b59675a_2019-05-31/isAcmContext~/true/viewId/%2Fproviders%2FMicrosoft.Billing%2FbillingAccounts%2F688e2018-b916-5441-11ec-c59b7772b9e9%3A395c7ee6-4f61-4267-9133-62fa7b59675a_2019-05-31%2Fproviders%2FMicrosoft.CostManagement%2Fviews%2Fms%3ADailyCosts/openByNewTab~/true)

### Create a VM
  - [_Use the Azure CLI to create a Linux VM | Microsoft Learn_](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli)
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

### SSH Tunnel
```
ssh -N -L 5678:localhost:5678 azureuser@13.92.86.145
```


### Access VM
```
ssh azureuser@13.92.86.145
```

## VM (Virtual Machine)

### Installation de Python
Cf. _§Python install_ in [_How to Setup MLflow On Azure | Medium_](https://medium.com/swlh/how-to-setup-mlflow-on-azure-5ba67c178e7d)

python3 --version
sudo apt install python3-pip
pip install virtualenv
history
sudo apt install python3.10-venv

### Create Inbound port rule
[myVM063b54 - Microsoft Azure](https://portal.azure.com/#@jvisa4031gmail.onmicrosoft.com/resource/subscriptions/a49ee12c-d832-486e-97d4-f71b6df0169e/resourceGroups/myVMResourceGroup063b54/providers/Microsoft.Compute/virtualMachines/myVM063b54/networkSettings)

### Check open ports
```
netstat -tunlp | grep "0:[56]"
```
### Access Virtual Environment
```
source ~/environments_folder/my_env/bin/activate
```

## Python Virtual Environment
On VM -> V-Env
```
source ~/environments_folder/my_env/bin/activate
```

## Git

sudo apt-get install git

## Notebook Jupyter

### Install
...

### Launch
On V-Env
```
jupyter notebook --no-browser  --ip=0.0.0.0 --port=5555 &
ps aux | grep jupyter
```

### Tunnel SSH
On CLI
```
ssh -N -L 5555:localhost:5555 azureuser@13.92.86.145
```

### Open port
...

### Access online
On Browser
- [Firrst connection](http://13.92.86.145:5555/?token=53f2bdd1110cb7c5e75e2fb9839af8ef755ad905d40deb82)
- [List of notebooks](http://13.92.86.145:5555/tree)

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