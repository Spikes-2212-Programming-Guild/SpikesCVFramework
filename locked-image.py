from threading import Lock


class LockedImage:
    def __init__(self):
        self.__img = None
        self.__lock = Lock()

    def set(self, img):
        with self.__lock:
            self.__img = img

    def get(self):
        with self.__lock:
            return self.__img
