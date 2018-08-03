from subprocess import call


class CameraManager:
    def __init__(self, cameras):
        self.cameras = cameras
        if len(cameras.keys()) < 1:
            self.current_id = ""
        else:
            self.current_id = cameras.keys()[0]

    def set_camera(self, camera_id):
        if self.current_id is not camera_id and self.current_id in self.cameras.keys():
            self.current_id = camera_id

    def set_exposure(self, exposure):
        call(f"v412-ctl --device=/dev/video{self.current_id} -c exposure_auto=1 -c exposure_absolute={exposure}")

    def get_image(self):
        cam = self.cameras.get(self.current_id, None)
        if cam is not None:
            success, img = cam.read()
            if success:
                return img
