class Settings:
    def __init__(self):
        self.__values = dict()
        self.__isUpdated = False

    def update(self, **values):
        for key in values.keys():
            if self.__values.get(key, "") != values.get(key, ""):
                self.__isUpdated = True
                self.__values[key] = values[key]

    def get(self):
        self.__isUpdated = False
        return self.__values.copy()

    def is_updated(self):
        return self.__isUpdated
