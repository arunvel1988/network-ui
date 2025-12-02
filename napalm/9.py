from napalm import get_network_driver

driver = get_network_driver("ios")
device = driver("10.0.0.1", "admin", "123")
device.open()

config = """
router bgp 65001
 bgp router-id 1.1.1.1
 neighbor 10.0.0.2 remote-as 65002
 address-family ipv4 unicast
"""

device.load_merge_candidate(config=config)
print("\n=== CONFIG DIFF ===")
print(device.compare_config())
device.commit_config()

device.close()
