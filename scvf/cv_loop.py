from threading import Thread

from scvf.loops import camera_loop, pipeline_loop, settings_loop
from scvf.util import PipelineManager, LockedImage, CameraManager, Settings


running = False


def start(pipelines, camera_port=0, output_consumer=lambda: None, settings_supplier=lambda: None):
    global running
    img = LockedImage()
    pipeline_settings = Settings()
    camera_settings = Settings()

    pipeline_manager = PipelineManager(pipelines)
    camera_manager = CameraManager(camera_port)

    pipeline_thread = Thread(target=pipeline_loop, args=(img, pipeline_manager, pipeline_settings,
                                                         output_consumer, lambda: running))
    camera_thread = Thread(target=camera_loop, args=(img, camera_manager, camera_settings, lambda: running))
    settings_thread = Thread(target=settings_loop, args=(settings_supplier, pipeline_settings,
                                                         camera_settings, lambda: running))

    pipeline_thread.start()
    camera_thread.start()
    settings_thread.start()


def end():
    global running
    running = False
