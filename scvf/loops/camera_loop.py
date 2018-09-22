from scvf import constants


def camera_loop(safe_image, camera_manager, settings, running):
    while running():
        if settings.is_updated():
            camera_manager.set_exposure(settings.get(constants.exposure_settings_key, ""))
            camera_manager.set_camera(settings.get(constants.camera_id_settings_key, ""))

        img = camera_manager.get_image()
        if img is not None:
            safe_image.set(img)
    camera_manager.release()