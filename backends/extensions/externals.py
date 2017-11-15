from ramos.mixins import ThreadSafeCreateMixin

from backends.external_resources import ExternalInterface


class ExternalsBackend(ThreadSafeCreateMixin, ExternalInterface):
    id = 'external'

    def get_file_from_bucket(self, file):
        raise NotImplementedError

    def publish_file_on_bucket(self, file):
        raise NotImplementedError

    def index_file_on_elastic_search(self, file):
        raise NotImplementedError
