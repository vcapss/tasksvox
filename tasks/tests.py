import json

from django.test import TestCase, Client
from model_mommy import mommy
from rest_framework.authtoken.models import Token

from tasks.models import Tasks, Files
from tasks.serializers import TasksSerializer


class TasksTest(TestCase):
    def setUp(self):
        self.task = mommy.make(Tasks, make_m2m=True, deleted=False)
        self.token = mommy.make(Token, user=self.task.owner)

        self.authenticated_client = Client(
            HTTP_AUTHORIZATION='Token {}'.format(self.token.key)
        )
        self.unauthorized_client = Client()

        self.task_payload = json.dumps({
                "name": "Tasks",
                "description": "desc",
                "priority": 3,
                "owner": str(self.task.owner.pk),
                "files": [
                    {"url": "asas1"}
                ]
            })

    def test_should_return_valid_tasks(self):
        response = self.authenticated_client.get('/tasks/')
        serializer = TasksSerializer(data=response.json()[0])

        assert response.status_code == 200
        assert serializer.is_valid()

    def test_should_return_unauthorized_request_without_token(self):
        response = self.unauthorized_client.get('/tasks/')

        assert response.status_code == 401

    def test_should_return_specific_task(self):
        response = self.authenticated_client.get(
            '/tasks/{}/'.format(self.task.pk)
        )
        serializer = TasksSerializer(data=response.json())

        assert response.status_code == 200
        assert serializer.is_valid()

    def test_should_return_inexistent_task(self):
        response = self.authenticated_client.get('/tasks/{}/'.format(10))

        assert response.status_code == 404
        assert response.data['detail'] == 'Não encontrado.'

    def test_should_return_deleted_task(self):
        response = self.authenticated_client.delete('/tasks/{}/'.format(self.task.pk))

        assert response.status_code == 204
        assert Tasks.objects.get(pk=self.task.pk).deleted

    def test_should_return_created_on_post_task(self):
        response = self.authenticated_client.post(
            '/tasks/',
            self.task_payload,
            content_type='application/json'
        )

        assert response.status_code == 201

    def test_should_return_unauthorized_on_post_task(self):
        response = self.unauthorized_client.post(
            '/tasks/',
            self.task_payload,
            content_type='application/json'
        )

        assert response.status_code == 401
