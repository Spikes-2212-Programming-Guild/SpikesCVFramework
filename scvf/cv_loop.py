from threading import Thread

from scvf.loops import camera_loop, pipeline_loop, settings_callback
from scvf.util import PipelineManager, SafeImage, CameraManager, Settings


running = False


def start(pipelines, camera_port=0, output_consumer=lambda: None, settings_supplier=lambda x: None):
    global running
    img = SafeImage()
    pipeline_settings = Settings()
    camera_settings = Settings()

    pipeline_manager = PipelineManager(pipelines)
    camera_manager = CameraManager(camera_port)

    pipeline_thread = Thread(target=pipeline_loop, args=(img, pipeline_manager, pipeline_settings,
                                                         output_consumer, lambda: running))
    camera_thread = Thread(target=camera_loop, args=(img, camera_manager, camera_settings, lambda: running))
    running = True
    settings_supplier(settings_callback(camera_settings, pipeline_settings))
    pipeline_thread.start()
    camera_thread.start()


def end():
    global running
    running = False
