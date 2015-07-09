from django.contrib.staticfiles.storage import ManifestFilesMixin
from pipeline.storage import PipelineMixin
from storages.backends.s3boto import S3BotoStorage


class S3PipelineManifestStorage(PipelineMixin, ManifestFilesMixin, S3BotoStorage):
    pass
