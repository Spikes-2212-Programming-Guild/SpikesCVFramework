from scvf.constants import settings_keys


def pipeline_loop(image_container, pipeline_manager, settings, output_consumer, running):
    while running():
        if settings.is_updated():
            pipeline_manager.set_pipeline(settings.get(settings_keys["pipeline_name"], ''))
        img = image_container.get()
        if img is not None:
            pipeline_manager.process(img)
            output_consumer(pipeline_manager.get_output())
