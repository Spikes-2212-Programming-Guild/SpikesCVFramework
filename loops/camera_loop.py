import constants


def camera_loop(locked_image, camera_manager, settings, capturing):
    while capturing():
        if settings.is_updated():
            camera_manager.set_exposure(settings.get().get(constants.exposure_settings_key, ""))
            camera_manager.set_camera(settings.get().get(constants.camera_id_settings_key, ""))

        img = camera_manager.get_image()
        if img is not None:
            locked_image.set(img)
