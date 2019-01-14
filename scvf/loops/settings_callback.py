

def callback(camera_settings, pipeline_settings):
    def c(key, value):
        camera_settings.update(**{key: value})
        pipeline_settings.update(**{key: value})
    return c