# Getting into the AAP

## General
The AAP (Apple Accessory Protocol) is a protocol directly build upon the L2CAP layer. The service PSM is `0x1001`. 

In python a simple channel can be created using the pybluez library:
```python
import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

bt_addr = "YOUR-DEVICE-ADDR"
psm = 0x1001

sock.connect((bt_addr, psm))
```

That is all that is required to communicate with apple headphones using the AAP protocol.


## Magic Pairing

Magic Pairing is done using a magic key and the BLE broadcast. The last 32 bytes of the broadcast is responsible for that. The decryption / encryption is done using AES with ECB mode.

The magic key retrieval has the following package exchange (`>` send / `<` recv):
```
> update magic keys (with cmd,key,hint,unknown,address [this order])
> request magic cloud keys (cmd. nothing special)
< update magic cloud keys (status?)
< update magic cloud keys (with cmd,magic irk,the key [last 16 bytes])
``` 

The `unknown` package has probably something to do with the IRK, at least the `Master Cloud IRK` is mentioned in the log together with the rest of the message (see `updateMagicCloudPairingKeys`)

Important is the bytes of `the key`. Maybe the rest is required for that, maybe it isn't. 

**EDIT**: As it turns out, the `request magic cloud keys [04 00 04 00 30 00 05 00]` can be triggered without going through the whole "update magic keys" process at all. The AirPods will return the key willingly to you. You just need to initialize the connection first using using the `Connect AAP service command`.
