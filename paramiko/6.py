import paramiko
import time

hostname = "10.0.0.1"
username = "admin"
password = "123"
enable_password = "Ssjcoe12345678@#"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

shell = client.invoke_shell()

shell.send("enable\n")
time.sleep(1)
shell.send(enable_password + "\n")
time.sleep(1)

shell.send("show processes cpu | include one minute\n")
time.sleep(1)
output = shell.recv(9000).decode()

print(output)

if "90" in output or "95" in output:
    print("⚠ ALERT: CPU is very high!")

client.close()
