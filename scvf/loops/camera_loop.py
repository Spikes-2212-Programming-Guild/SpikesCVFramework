from scvf import constants


def camera_loop(locked_image, camera_manager, settings, running):
    with camera_manager as c:
        while running():
            if settings.is_updated():
                c.set_exposure(settings.get().get(constants.exposure_settings_key, ""))
                c.set_camera(settings.get().get(constants.camera_id_settings_key, ""))

            img = c.get_image()
            if img is not None:
                locked_image.set(img)
