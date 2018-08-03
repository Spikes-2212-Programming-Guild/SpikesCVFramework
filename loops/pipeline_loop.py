import constants


def pipeline_loop(locked_image, pipeline_manager, settings, output_consumer, capturing):
    while capturing():
        if settings.is_updated():
            pipeline_manager.set_pipeline(settings.get().get(constants.pipeline_name_settings_key, ''))
        img = locked_image.get()
        output = pipeline_manager.process(img)
        output_consumer(output)
