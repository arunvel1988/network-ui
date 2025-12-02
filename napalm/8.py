from napalm import get_network_driver

driver = get_network_driver("ios")
device = driver("10.0.0.1", "admin", "123")
device.open()

config = """
router ospf 1
 router-id 1.1.1.1
 network 10.0.0.0 0.0.0.255 area 0
"""

device.load_merge_candidate(config=config)
print("\n=== CONFIG DIFF ===")
print(device.compare_config())
device.commit_config()

device.close()
