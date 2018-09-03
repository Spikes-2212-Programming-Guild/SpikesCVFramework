from threading import Lock


class SafeImage:
    def __init__(self):
        self.lock = Lock()
        self.old_img = None
        self.new_img = None

    def set(self, img):
        while self.lock:
            self.new_img = img

    def get(self):
        with self.lock:
            b = self.old_img
            self.old_img = self.new_img
            return b
