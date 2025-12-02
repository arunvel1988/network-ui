from napalm import get_network_driver

routers = [
    {"host": "10.0.0.1", "user": "admin", "pass": "123"},
    {"host": "10.0.0.2", "user": "admin", "pass": "123"},
]

driver = get_network_driver("ios")

for r in routers:
    device = driver(r["host"], r["user"], r["pass"])
    device.open()
    print(f"\n=== FACTS FOR {r['host']} ===")
    print(device.get_facts())
    device.close()
