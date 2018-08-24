from subprocess import call

from cv2 import VideoCapture


class CameraManager:
    def __init__(self, port=0):
        self.port = port
        self.camera = VideoCapture(port)

    def set_camera(self, port):
        if self.port is not port:
            try:
                port = int(port)
                self.camera.release()
                self.camera = VideoCapture(port)
                self.port = port
            except ValueError as e:
                pass

    def set_exposure(self, exposure):
        def safe_format(x):
            if x is None:
                return 0
            return x

        call(f"v4l2-ctl --device=/dev/video{safe_format(self.port)}"
             f" -c exposure_auto=1 -c exposure_absolute={safe_format(exposure)}")

    def get_image(self):
        success, img = self.camera.read()
        if success:
            return img

    def release(self):
        self.camera.release()
