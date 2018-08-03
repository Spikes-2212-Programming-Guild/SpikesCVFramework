from .loops.camera_loop import camera_loop
from .loops.pipeline_loop import pipeline_loop
from .loops.settings_loop import settings_loop

from .util.locked_image import LockedImage
from .util.camera_manager import CameraManager
from .util.pipeline_manager import PipelineManager
from .util.settings import Settings


def start(cameras, pipelines, output_consumer=lambda: None, settings_supplier=lambda: None):
    img = LockedImage()
    pipeline_settings = Settings()
    camera_settings = Settings()

    pipeline_manager = PipelineManager(pipelines)
    camera_manager = CameraManager(cameras)

