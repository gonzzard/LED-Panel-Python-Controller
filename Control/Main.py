from BlueToothController import BluetoothController
from CurrentStatus import CurrentStatus
from FaceController import FaceController
from threading import Lock, Thread

if __name__ == "__main__":
    
    blue = BluetoothController(CurrentStatus())
    principal = FaceController(CurrentStatus())
    
    process1 = Thread(target=blue.ListenBluetooth)
    process2 = Thread(target=principal.cara)
    process1.start()
    process2.start()