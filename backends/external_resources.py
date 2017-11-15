import abc


class ExternalInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_file_from_bucket(self, file):
        pass

    @abc.abstractmethod
    def publish_file_on_bucket(self, file):
        pass

    @abc.abstractmethod
    def index_file_on_elastic_search(self, file):
        pass
