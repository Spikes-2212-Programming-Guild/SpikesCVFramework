

def callback(camera_settings, pipeline_settings):
    """
        this function generates a callback should be called each time a new settings arrives.
        the ``settings_supplier`` is responsible for receiving new settings and calling this function when
        a new settings arrives. in turn, the callback updates the given setting sets with the setting.
    :param camera_settings:
        the settings for the ``camera_loop``
    :param pipeline_settings:
        the settings for the ``pipeline_loop``
    :return:
        a callback that updates the given settings
    """
    def c(key, value):
        camera_settings.update(**{key: value})
        pipeline_settings.update(**{key: value})
    return c