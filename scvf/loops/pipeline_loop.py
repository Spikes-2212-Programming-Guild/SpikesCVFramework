from scvf import constants


def pipeline_loop(safe_image, pipeline_manager, settings, output_consumer, running):
    while running():
        if settings.is_updated():
            pipeline_manager.set_pipeline(settings.get(constants.pipeline_name_settings_key, ''))
        img = safe_image.get()
        if img is not None:
            pipeline_manager.process(img)
            output_consumer(pipeline_manager.get_output())
