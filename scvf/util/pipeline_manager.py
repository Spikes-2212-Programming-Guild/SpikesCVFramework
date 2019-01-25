class PipelineManager:
    """
        This pipeline is responsible for managing all given pipelines.

        Note that you have to pass a setting that tells which pipeline should be used.
        otherwise the loop wouldn't use any pipeline.
    """
    def __init__(self, pipelines):
        self.pipelines = pipelines
        if len(pipelines.keys()) < 1:
            self.current_pipeline = ""
        else:
            self.current_pipeline = list(pipelines.keys())[0]

    def set_pipeline(self, pipeline_id):
        """
            changes the current pipeline to the pipeline with the given id
        :param pipeline_id:
            the id of the pipeline
        """
        if pipeline_id in self.pipelines.keys():
            self.current_pipeline = pipeline_id

    def process(self, img):
        """
        this function gives the current pipeline process a given image
        :param img:
            the image that should be processed
        :return:
        """
        pipeline = self.pipelines.get(self.current_pipeline, None)
        if pipeline is not None:
            pipeline.process(img)

    def get_output(self):
        """
            This function returns the current output of the current pipeline
        :return:
            the output of the pipeline
        """
        pipeline = self.pipelines.get(self.current_pipeline, None)
        if pipeline is not None:
            return pipeline.get_output()
