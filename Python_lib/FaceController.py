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
            elif self.CurrentStatus.status == "SLEEP":
                if self.last_status != "SLEEP":
                    print("SLEEP")
                    self.last_status = "SLEEP"
            elif self.CurrentStatus.status == "ANGRY":
                if self.last_status != "ANGRY":
                    print("ANGRY")
                    self.last_status = "ANGRY"
            elif self.CurrentStatus.status == "SAD":
                if self.last_status != "SAD":
                    print("SAD")
                    self.last_status = "SAD"
            elif self.CurrentStatus.status == "CONFUSED":
                if self.last_status != "CONFUSED":
                    print("CONFUSED")
                    self.last_status = "CONFUSED"