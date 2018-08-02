class LockedImage:
    def __init__(self):
        self._img = None
        self._locked = False

    def set(self, img):
        if not self._locked:
            self._img = img

    def get(self):
        return self._img

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False
