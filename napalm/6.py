from napalm import get_network_driver

router_ip = "10.0.0.1"
username = "admin"
password = "123"

driver = get_network_driver("ios")
device = driver(router_ip, username, password)

device.open()

config = device.get_config()
print("\n=== RUNNING CONFIG ===")
print(config["running"][:1000], "...")  # Print first 1000 chars for readability

print("\n=== STARTUP CONFIG ===")
print(config["startup"][:1000], "...")

print("\n=== CANDIDATE CONFIG ===")
print(config["candidate"][:1000], "...")

device.close()
