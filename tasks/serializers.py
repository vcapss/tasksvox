from rest_framework import serializers

from tasks.models import Tasks, Files


class FileSerializer(serializers.ModelSerializer):
    url = serializers.CharField(allow_blank=True)

    class Meta:
        model = Files
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    files = FileSerializer(required=False, many=True)

    class Meta:
        model = Tasks
        fields = ('id', 'name', 'description', 'priority', 'owner', 'files', 'created', 'done', 'user_task_owner',)


class TasksStatusSerializer(serializers.Serializer):
    done = serializers.BooleanField(required=True)

    class Meta:
        fields = ('done',)
