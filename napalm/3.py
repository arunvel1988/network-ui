from ncclient import manager

device_params = {
    "host": "10.0.0.1",
    "username": "admin",
    "password": "123",
    "hostkey_verify": False
}

with manager.connect(**device_params) as m:
    print("Connected using NETCONF!")

    for capability in m.server_capabilities:
        print(capability)
