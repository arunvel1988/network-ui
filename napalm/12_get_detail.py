from napalm import get_network_driver

driver = get_network_driver("ios")
device = driver("10.0.0.1", "admin", "123")
device.open()

env = device.get_environment()
print("\n=== DEVICE ENVIRONMENT ===")
for key, value in env.items():
    print(f"{key}: {value}")

device.close()
