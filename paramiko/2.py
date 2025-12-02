import paramiko
import time
from datetime import datetime

hostname = "10.0.0.1"
username = "admin"
password = "123"
enable_password = "Ssjcoe12345678@#"

commands = [
    "show ip interface brief",
    "show version",
    "show running-config",
    "show ip route",
]

# SSH Client Setup
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

shell = client.invoke_shell()

# Enter Enable Mode
shell.send("enable\n")
time.sleep(1)
shell.send(enable_password + "\n")
time.sleep(1)

# Create logfile
logfile = f"router_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(logfile, "w") as f:
    for cmd in commands:
        shell.send(cmd + "\n")
        time.sleep(2)

        output = shell.recv(90000).decode("utf-8")
        f.write(f"\n\n----- {cmd} -----\n")
        f.write(output)
        print(output)

client.close()
print(f"\n✔ Output saved to {logfile}")
