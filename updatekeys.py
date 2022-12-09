# Import the necessary libraries
import paramiko

# Set the variables for the SSH connection
USERNAME = "yoursshusername" # SSH username used to connect to destination
SSH_KEY = "/root/.ssh/yourkey.priv" # Path to the SSH key used to connect to the destination

# Set up an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Define a list of server hostnames
SERVERS = [
    "SERVERHOSTNAME1",
    "SERVERHOSTNAME2"
]

# Define a list of SSH keys
AUTH_KEYS = [
    "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC6RItj+PvAJWd2l0nJfMgRNYtQ68...",
    "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC5jwD5if5q3l881lSmr1jfO9..."
]

# Loop through the servers and update the authorized keys
for server in SERVERS:
    try:
        ssh.connect(server, username=USERNAME, key_filename=SSH_KEY, password="SSHKEYPASSWORDHERE") # ensure you enter your SSH key password if applicable here, otherwise remove the password arg

        # Clear the authorized keys file
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cat /dev/null > ~/.ssh/authorized_keys")

        # Add the keys to the authorized keys file
        for key in AUTH_KEYS:
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"echo {key} >> ~/.ssh/authorized_keys")

        print(f"Successfully updated authorized keys file on {server}")
    except Exception as e:
        print(f"Failed to update authorized keys file on {server}: {e}")
    finally:
        ssh.close()
