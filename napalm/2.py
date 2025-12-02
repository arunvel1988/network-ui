from napalm import get_network_driver

router_ip = "10.0.0.1"
username = "admin"
password = "123"

driver = get_network_driver("ios")
device = driver(hostname=router_ip, username=username, password=password)

print("Connecting...")
device.open()

print("\n----- Facts -----")
print(device.get_facts())

print("\n----- Interfaces -----")
print(device.get_interfaces())

print("\n----- ARP Table -----")
print(device.get_arp_table())

print("\n----- Running Config -----")
print(device.get_config()['running'])

device.close()
