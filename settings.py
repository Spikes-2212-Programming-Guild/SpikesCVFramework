from threading import Lock

class Settings:
    def __init__(self):
        self.__values = dict()
        self.__isUpdated = False
        self.__lock = Lock()

    def update(self, **values):
        with self.__lock:
            for key in values.keys():
                if self.__values.get(key, "") != values.get(key, ""):
                    self.__isUpdated = True
                    self.__values[key] = values[key]

    def get(self):
        with self.__lock:
            self.__isUpdated = False
            return self.__values.copy()

    def get_is_updated(self):
        with self.__lock:
            return self.__isUpdated
