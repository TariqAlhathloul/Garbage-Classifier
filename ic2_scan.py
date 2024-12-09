import smbus

bus = smbus.SMBus(1)
for device in range(128):
    try:
        bus.read_byte(device)
        print(f"Device found at address: {hex(device)}")
    except:
        pass
