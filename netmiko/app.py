from netmiko import ConnectHandler
import time

R1 = {
    "device_type": "cisco_ios",
    "host": "R1_IP",
    "username": "admin",
    "password": "admin"
}

R2 = {
    "device_type": "cisco_ios",
    "host": "R2_IP",
    "username": "admin",
    "password": "admin"
}

# R1 CONFIG
R1_CONFIG = [
    "hostname R1",
    "interface f0/0",
    "ip address 20.0.0.1 255.255.255.0",
    "no shutdown",
    "exit",
    "interface f0/1",
    "ip address 30.0.0.1 255.255.255.0",
    "no shutdown",
    "exit",
    "ip route 40.0.0.0 255.255.255.0 20.0.0.2"
]

# R2 CONFIG
R2_CONFIG = [
    "hostname R2",
    "interface f0/0",
    "ip address 20.0.0.2 255.255.255.0",
    "no shutdown",
    "exit",
    "interface f0/1",
    "ip address 40.0.0.1 255.255.255.0",
    "no shutdown",
    "exit",
    "ip route 30.0.0.0 255.255.255.0 20.0.0.1"
]


def connect(router):
    return ConnectHandler(**router)


def configure(name, router, config):
    conn = connect(router)
    print(f"\nConfiguring {name}")
    print(conn.send_config_set(config))
    conn.disconnect()


def verify():
    print("\nVerification from R1\n")
    conn = connect(R1)

    print("IP Interface Brief:")
    print(conn.send_command("show ip interface brief"))

    print("\nRouting Table:")
    print(conn.send_command("show ip route"))

    print("\nPing test to R2 LAN (40.0.0.1):")
    print(conn.send_command("ping 40.0.0.1 repeat 5"))

    conn.disconnect()


if __name__ == "__main__":

    print("\nStarting Network Automation Demo\n")

    configure("R1", R1, R1_CONFIG)
    configure("R2", R2, R2_CONFIG)

    print("\nWaiting for network to stabilize\n")
    time.sleep(3)

    verify()

    print("\nDemo Completed\n")
    ################################################################################################
