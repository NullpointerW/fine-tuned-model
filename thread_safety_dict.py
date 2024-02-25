import threading


class ThreadSafeDict(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.dict = {}

    def set(self, key, value):
        with self.lock:
            self.dict[key] = value

    def get(self, key):
        with self.lock:
            return self.dict.get(key)

    def exist(self, key):
        with self.lock:
            return key in self.dict

    def clear(self):
        with self.lock:
            self.dict.clear()
