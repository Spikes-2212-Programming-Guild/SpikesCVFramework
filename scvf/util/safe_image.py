from threading import Lock


class SafeImage:
    def __init__(self):
        self.lock = Lock()
        self.image_container = []

    def set(self, img):
        with self.lock:
            if len(self.image_container) == 0:
                self.image_container.append(img)
            else:
                self.image_container.pop()
                self.image_container.append(img)

    def get(self):
        with self.lock:
            if len(self.image_container) != 0:
                return self.image_container.pop()
