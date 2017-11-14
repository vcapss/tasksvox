from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from backends.pools.querysets import QuerySetsPool
from backends.pools.tasks import TasksPool
from users.models import User
from .models import Tasks, Files
from .serializers import TasksSerializer


class TasksList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    name = 'task-list'

    def get_queryset(self):
        backend = TasksPool.get('tasks')
        return backend.get_existents_tasks()

    def get_serializer(self, *args, **kwargs):
        try:
            kwargs['data']['owner'] = self.request.user.pk
        except KeyError:
            pass
        return super(TasksList, self).get_serializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        backend = QuerySetsPool.get('querysets')
        user = backend.get_or_404(User, 'pk', request.data.get('owner'))

        tasks = {
            'description': request.data.get('description'),
            'name': request.data.get('name'),
            'priority': request.data.get('priority'),
            'owner': user.pk,
            'deleted': False,
        }

        serializer = TasksSerializer(data=tasks)

        if serializer.is_valid():
            tasks['owner'] = user
            tasks = backend.create_resource(Tasks, **tasks)

            for file in request.data['files'][0].items():
                if file[0] == 'id':
                    file = backend.get_or_404(
                        Model=Files,
                        key='pk',
                        value=file[1]
                    )
                else:
                    file = backend.create_resource(Files, **{"url": file[1]})

                tasks.files.add(file)

            tasks.save()

            return Response(status=201)
        else:
            return Response(data=serializer.errors, status=400)


class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    name = 'task-detail'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        backend = TasksPool.get('tasks')

        return backend.delete(instance)
