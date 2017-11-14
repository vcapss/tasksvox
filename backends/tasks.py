import abc


class TasksInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def delete(self, instance):
        pass

    @abc.abstractmethod
    def get_existents_tasks(self):
        pass

