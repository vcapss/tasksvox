from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .models import Tasks
from .serializers import TasksSerializer


class TasksList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    name = 'task-list'

    def get_queryset(self):
        return Tasks.objects.filter(deleted=False)

    def get_serializer(self, *args, **kwargs):
        try:
            kwargs['data']['owner'] = self.request.user.pk
        except KeyError:
            pass
        return super(TasksList, self).get_serializer(*args, **kwargs)


class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    name = 'task-detail'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()

        return Response(status=204)
