class ImageContainer:
    """
        This class is responsible for holding a reference to the most relevant image.
    """
    def __init__(self):
        self.img = None

    def set(self, img):
        self.img = img

    def get(self):
        return self.img