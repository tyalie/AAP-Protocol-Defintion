import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

bt_addr = "60:83:73:A1:BC:63" # sys.argv[1]
psm = 0x1001  # AAP

print(f"Trying to connect to {bt_addr} on PSM 0x{psm:04X}...")

sock.connect((bt_addr, psm))

print("Connected. Type something...")
while True:
    data = input("> ")
    if data == "quit":
        break

    try:
        byts = bytes(int(b, 16) for b in data.split(" "))
        sock.send(byts)
    except:
        ...

    try:
        data = sock.recv(1024)
        print("Data received:", data.hex())
    except:
        ...

sock.close()
