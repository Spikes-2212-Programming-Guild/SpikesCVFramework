from scvf.constants import settings_keys


def pipeline_loop(image_container, pipeline_manager, settings, output_consumer, running):
    """
    This function creates a loop that manages all the pipelines.
    it is responsible for processing an image and sending the output to the output_consumer,
    as well as applying new settings to the pipelines if they arrive.
    :param image_container:
        a container that holds the latest image
    :param pipeline_manager:
        a ``PipelineManager`` instance that holds all the pipelines
    :param settings:
        the ``Settings`` instance for this loop
    :param output_consumer:
        the function that should receive the processed output of the pipeline
    :param running:
        a lambda that tells the pipeline_loop whether it should continue to run
    """
    while running():
        if settings.is_updated():
            pipeline_manager.set_pipeline(settings.get(settings_keys["pipeline_name"], ''))
        img = image_container.get()
        if img is not None:
            pipeline_manager.process(img)
            output_consumer(pipeline_manager.get_output())
