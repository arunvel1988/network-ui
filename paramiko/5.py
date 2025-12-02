import paramiko
import time

hostname = "10.0.0.1"
username = "admin"
password = "123"
enable_password = "Ssjcoe12345678@#"

# Read commands from external file
with open("commands.txt") as f:
    commands = [line.strip() for line in f.readlines()]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

shell = client.invoke_shell()

shell.send("enable\n")
time.sleep(1)
shell.send(enable_password + "\n")
time.sleep(1)

for cmd in commands:
    shell.send(cmd + "\n")
    time.sleep(2)
    print(shell.recv(99999).decode())

client.close()
