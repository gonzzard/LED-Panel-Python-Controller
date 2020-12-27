import numpy as np
import sounddevice as sd

class FaceController:
    def __init__(self, status):
        self.CurrentStatus = status
        self.last_status = "VOICE"

    def _print_sound(self, indata, outdata, frames, time, status):
        volume_norm = np.linalg.norm(indata)*10
        print ("|" * int(volume_norm))

    def cara(self):
        while True:
            if self.CurrentStatus.status == "OWO":
                if self.last_status != "OWO":
                    print("OWO")
                    self.last_status = "OWO"
            elif self.CurrentStatus.status == "VOICE":
                self.last_status = "VOICE"
                with sd.Stream(callback=self._print_sound):
                    while True:
                        if self.CurrentStatus.status != "VOICE":
                            break
                        sd.sleep(1)
