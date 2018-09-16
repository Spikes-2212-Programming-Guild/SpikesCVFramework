from threading import Lock


class SafeImage:
    def __init__(self):
        self.lock = Lock()
        self.image_container = []

    def set(self, img):
        self.lock.acquire()
        if len(self.image_container) != 0:
            self.image_container.pop()
        self.image_container.append(img)
        self.lock.release()

    def get(self):
        if len(self.image_container) != 0:
            self.lock.acquire()
            val = None
            try:
                val = self.image_container.pop()
            finally:
                self.lock.release()
                return val
