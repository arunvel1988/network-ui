from napalm import get_network_driver

router_ip = "10.0.0.1"
username = "admin"
password = "123"

driver = get_network_driver("ios")
device = driver(router_ip, username, password)

print("Opening connection...")
device.open()

interfaces = device.get_interfaces()

print("\n=== INTERFACE DETAILS ===")
for iface, details in interfaces.items():
    print(f"\nInterface: {iface}")
    print(f"  Enabled      : {details['is_enabled']}")
    print(f"  Up/Down      : {details['is_up']}")
    print(f"  Speed        : {details['speed']} Mbps")
    print(f"  MAC Address  : {details['mac_address']}")
    print(f"  Description  : {details.get('description', '')}")

device.close()
print("\nConnection closed.")
