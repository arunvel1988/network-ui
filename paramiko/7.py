import paramiko
import time
from datetime import datetime

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

# Running-config
shell.send("show running-config\n")
time.sleep(3)
running = shell.recv(200000).decode()

# Startup-config
shell.send("show startup-config\n")
time.sleep(3)
startup = shell.recv(200000).decode()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

with open(f"running_config_{timestamp}.txt", "w") as f:
    f.write(running)

with open(f"startup_config_{timestamp}.txt", "w") as f:
    f.write(startup)

print("✔ Backup completed")

client.close()
