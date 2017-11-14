from ramos.mixins import ThreadSafeCreateMixin
from rest_framework.response import Response

from backends.tasks import TasksInterface
from tasks.models import Tasks


class TasksBackend(ThreadSafeCreateMixin, TasksInterface):
    id = 'tasks'

    def delete(self, instance):
        instance.deleted = True
        instance.save()

        return Response(status=204)

    def get_existents_tasks(self):
        return Tasks.objects.filter(deleted=False)
