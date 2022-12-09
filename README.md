# mass-update-ssh-keys
A Python script that will connect to servers and re-write the authorized_keys file with new defined keys. 

The paramiko library is required and can be installed using Pip:

```
pip install paramiko
```

To execute the command, you would write via SSH on any server running Python3:

```
python3 updatekeys.py
```
