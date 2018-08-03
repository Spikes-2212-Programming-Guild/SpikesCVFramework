from threading import Thread

from .loops.camera_loop import camera_loop
from .loops.pipeline_loop import pipeline_loop
from .loops.settings_loop import settings_loop

from .util.locked_image import LockedImage
from .util.camera_manager import CameraManager
from .util.pipeline_manager import PipelineManager
from .util.settings import Settings

capturing = False


def start(cameras, pipelines, output_consumer=lambda: None, settings_supplier=lambda: None):
    global capturing
    img = LockedImage()
    pipeline_settings = Settings()
    camera_settings = Settings()

    pipeline_manager = PipelineManager(pipelines)
    camera_manager = CameraManager(cameras)

    pipeline_thread = Thread(target=pipeline_loop, args=(img, pipeline_manager, pipeline_settings,
                                                         output_consumer, lambda: capturing))
    camera_thread = Thread(target=camera_loop, args=(img, camera_manager, camera_settings, lambda: capturing))
    settings_thread = Thread(target=settings_loop, args=(settings_supplier, pipeline_settings,
                                                         camera_settings, lambda: capturing))


def close():
    global capturing
    capturing = False
