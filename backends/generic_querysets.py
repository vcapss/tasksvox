import abc


class QuerysetsInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_or_404(self, Model, key, value):
        pass

    @abc.abstractmethod
    def create_resource(self, Model, **data):
        pass
