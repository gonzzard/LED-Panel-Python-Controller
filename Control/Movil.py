# simple inquiry example
import bluetooth, subprocess

addr = '' # Device Address

port = 1 

# Now, connect in the same way as always with PyBlueZ
try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((addr,port))
    while True:
        data = str.encode(input())
        if data:
            s.send(data)
except bluetooth.btcommon.BluetoothError as err:
    # Error handler
    print("ERRRRRROR")
    pass