from napalm import get_network_driver

driver = get_network_driver("ios")
device = driver("10.0.0.1", "admin", "123")

device.open()

config = """
interface GigabitEthernet2
 description LINK_TO_FIREWALL
 ip address 192.168.50.1 255.255.255.0
 no shut
"""

device.load_merge_candidate(config=config)

diff = device.compare_config()
print("\n=== CONFIG DIFF ===")
print(diff)

if diff:
    print("Committing configuration...")
    device.commit_config()
else:
    print("No changes detected.")

device.close()
