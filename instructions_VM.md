On CLI -> VM
```
ssh azureuser@13.92.86.145
```

On VM -> V-Env
```
source ~/environments_folder/my_env/bin/activate
```

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

