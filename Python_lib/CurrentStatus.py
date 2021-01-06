from threading import Lock, Thread

class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
class CurrentStatus(metaclass=SingletonMeta):
    status: str = None
    def __init__(self, status: str = "") -> None:
        self.status = "VOICE"