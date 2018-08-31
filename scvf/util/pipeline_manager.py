class PipelineManager:
    def __init__(self, pipelines):
        self.pipelines = pipelines
        if len(pipelines.keys()) < 1:
            self.current_pipeline = ""
        else:
            self.current_pipeline = list(pipelines.keys())[0]

    def set_pipeline(self, pipeline_id):
        if pipeline_id in self.pipelines.keys():
            self.current_pipeline = pipeline_id

    def process(self, img):
        pipeline = self.pipelines.get(self.current_pipeline, None)
        if pipeline is not None:
            pipeline.process(img)

    def get_output(self):
        pipeline = self.pipelines.get(self.current_pipeline, None)
        if pipeline is not None:
            return pipeline.get_output()
