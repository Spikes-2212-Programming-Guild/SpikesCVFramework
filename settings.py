class Settings:
    def __init__(self):
        self._values = dict()
        self._isUpdated = False

    def update(self, **values):
        for key in values.keys():
            if self._values.get(key, "") != values.get(key, ""):
                self._isUpdated = True
                self._values[key] = values[key]

    def get(self):
        self._isUpdated = False
        return self._values.copy()
