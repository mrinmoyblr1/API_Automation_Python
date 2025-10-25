import paramiko

# EC2 connection details
hostname = "ec2-3-135-230-206.us-east-2.compute.amazonaws.com"  # Public DNS or IP of your EC2
username = "ec2-user"  # e.g., 'ubuntu' for Ubuntu AMIs, 'ec2-user' for Amazon Linux
key_path = "/Users/mrinmoy/Documents-Local/Documents/Development/MBAWS001.pem"  # Path to your SSH private key file

# Command you want to execute
#command = "ls -l /home/ec2-user"  # Example: list directory contents
command = "ls -al"  # Example: list directory contents
# command = "cat demofile"  # Example: list directory contents

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect using private key
    ssh.connect(hostname=hostname, username=username, key_filename=key_path)

    # Execute the command
    stdin, stdout, stderr = ssh.exec_command(command)

    # Print command output
    print("Output:\n", stdout.read().decode())
    print("Errors:\n", stderr.read().decode())

except Exception as e:
    print("Error:", e)

finally:
    ssh.close()
