import yaml
from napalm import get_network_driver

with open("interfaces.yml") as f:
    data = yaml.safe_load(f)

driver = get_network_driver("ios")
device = driver("10.0.0.1", "admin", "123")
device.open()

config = ""
for iface in data["interfaces"]:
    config += f"""
interface {iface['name']}
 description {iface['description']}
 ip address {iface['ip']} {iface['mask']}
 no shut
"""

device.load_merge_candidate(config=config)
print("\n=== CONFIG DIFF ===")
print(device.compare_config())

device.commit_config()
device.close()
