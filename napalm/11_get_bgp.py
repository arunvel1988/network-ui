from napalm import get_network_driver

driver = get_network_driver("ios")
device = driver("10.0.0.1", "admin", "123")
device.open()

bgp_neighbors = device.get_bgp_neighbors()
print("\n=== BGP NEIGHBORS ===")
for asn, neighbors in bgp_neighbors.items():
    print(f"ASN: {asn}")
    for neighbor, details in neighbors.items():
        print(f"  Neighbor: {neighbor}")
        for k, v in details.items():
            print(f"    {k}: {v}")

device.close()
