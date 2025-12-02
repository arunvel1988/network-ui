from napalm import get_network_driver

router_ip = "10.0.0.1"
username = "admin"
password = "123"

driver = get_network_driver("ios")
device = driver(router_ip, username, password)

print("Opening connection...")
device.open()

arp_table = device.get_arp_table()

print("\n=== ARP TABLE ===")
for entry in arp_table:
    print(f"""
IP Address : {entry['ip']}
MAC        : {entry['mac']}
Interface  : {entry['interface']}
Age        : {entry['age']}
""")

device.close()
print("\nConnection closed.")
