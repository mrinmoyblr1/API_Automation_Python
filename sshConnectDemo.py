import paramiko as paramiko
from idna.idnadata import scripts

from utilities.configurations import getConfig

# Start Connections

host = getConfig()['Server']['host']
username = getConfig()['Server']['username']
# key_path = "/Users/mrinmoy/Library/Mobile Documents/com~apple~CloudDocs/Documents/Development/Python/MBAWS001.pem"
key_path = "/Users/mrinmoy/Documents-Local/Documents/Development/MBAWS001.pem"
# Path to your SSH private key file
# password = getConfig()['Server']['password']
# port = getConfig()['Server']['port']


# command = "cat demofile"
# command = "ls"  # Example: list directory contents
command = "cat demofile"  # Example: list directory contents

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# It will auto add missing Keys policy, at runtime python will create a public key and it will be added

ssh.connect(hostname=host, username=username, key_filename=key_path)

# Run commands
stdin, stdout, stderr = ssh.exec_command(command)
# print(stdout.readlines())
# print("Output:\n", stdout.read().decode())
lines = stdout.readlines()
# print(lines[0])
print(lines)

# Upload Files
sftp = ssh.open_sftp()
destinationPath = "script.py"
localPath = "batchFiles/script.py"
sftp.put(localPath, destinationPath)

destinationPath = "loanasa.csv"
localPath = "batchFiles/loanasa.csv"
sftp.put(localPath, destinationPath)

# Trigger the Batch commands
stdin, stdout, stderr = ssh.exec_command("python3 script.py")

# Download the file to local system
sftp.get("loanasa.csv", "outputFiles/loanasa.csv")

# Parse Output file CSV


ssh.close()
