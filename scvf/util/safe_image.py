
class SafeImage:
    def __init__(self):
        self.old_img = None
        self.new_img = None

    def set(self, img):
        self.new_img = img

    def get(self):
        b = self.old_img
        self.old_img = self.new_img
        return b
