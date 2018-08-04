from scvf import constants


def settings_loop(settings_supplier, pipeline_settings, camera_settings, running):
    while running():
        pipeline_settings.update(pipeline_name=settings_supplier(constants.pipeline_name_settings_key))
        camera_settings.update(camera_id=settings_supplier(constants.camera_id_settings_key),
                               exposure=settings_supplier(constants.exposure_settings_key))
