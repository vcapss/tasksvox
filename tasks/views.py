from django.http import JsonResponse
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from users.models import User
from .models import Tasks, Files
from .serializers import TasksSerializer, FileSerializer


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

    def post(self, request, *args, **kwargs):
        tasks = Tasks.objects.create(
            description=request.data['description'],
            name=request.data['name'],
            priority=request.data['priority'],
            owner=User.objects.get(pk=request.data['owner']),
            deleted=False,
        )

        for file in request.data['files'][0].items():
            if file[0] == 'id':
                file = Files.objects.get(pk=file[1])
            else:
                file = Files.objects.create(url=file[1])

            tasks.files.add(file)

        tasks.save()

        return Response(status=201)


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
