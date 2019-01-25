from scvf.constants import settings_keys


def camera_loop(image_container, camera_manager, settings, running):
    """
    This function is responsible for constantly reading images from the camera buffer,
    so that the image available to the loop is as relevant as possible
    :param image_container:
        an object that is responsible for storing the most relevant image
    :param camera_manager:
        an instance of ``CameraManager`` that is responsible for managing all the cameras
        and reading images from them
    :param settings:
        the ``Settings`` object for the camera_loop
    :param running:
        a lambda that tells the pipeline_loop whether it should continue to run
    """
    while running():
        if settings.is_updated():
            camera_manager.set_exposure(settings.get(settings_keys["exposure"], ""))
            camera_manager.set_camera(settings.get(settings_keys["camera_id"], ""))

        img = camera_manager.get_image()
        if img is not None:
            image_container.set(img)
    camera_manager.release()