import paramiko
import time

routers = [
    {"ip": "10.0.0.1", "user": "admin", "password": "123"},
    {"ip": "10.0.0.2", "user": "admin", "password": "123"},
    {"ip": "10.0.0.3", "user": "admin", "password": "123"},
]

command = "show ip interface brief"

def run_command(ip, user, pwd):
    print(f"\nConnecting to {ip}...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=pwd)

    shell = client.invoke_shell()
    shell.send(command + "\n")
    time.sleep(2)

    output = shell.recv(90000).decode()
    print(output)

    client.close()

for r in routers:
    run_command(r["ip"], r["user"], r["password"])
