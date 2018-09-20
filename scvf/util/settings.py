class Settings:
    def __init__(self):
        self.values = dict()
        self.isUpdated = False

    def update(self, **values):
        for key in values.keys():
            if self.values.get(key, "") != values.get(key, ""):
                self.isUpdated = True
                self.values[key] = values[key]

    def get(self):
        self.isUpdated = False
        return self.values.copy()

    def is_updated(self):
        return self.isUpdated
