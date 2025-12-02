import paramiko
import time

hostname = "10.0.0.1"
username = "admin"
password = "123"
enable_password = "Ssjcoe12345678@#"

config_commands = [
    "interface gigabitEthernet 2",
    "description Connected-to-LAN",
    "ip address 20.0.0.2 255.255.255.0",
    "no shut",
    "exit",
]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

shell = client.invoke_shell()

shell.send("enable\n")
time.sleep(1)
shell.send(enable_password + "\n")
time.sleep(1)

# Enter config mode
shell.send("configure terminal\n")
time.sleep(1)

for cmd in config_commands:
    shell.send(cmd + "\n")
    time.sleep(1)

shell.send("end\n")
time.sleep(1)

shell.send("write memory\n")
time.sleep(2)

output = shell.recv(90000).decode()
print(output)

client.close()
