from django.db import models

from users.models import User

PRIORITY_LEVEL = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Files(models.Model):
    url = models.CharField(max_length=500, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    priority = models.IntegerField(default=1, null=False, choices=PRIORITY_LEVEL)
    files = models.ManyToManyField(Files)
    owner = models.ForeignKey(
        'users.User',
        related_name='owner_task',
        on_delete=models.CASCADE
    )
    deleted = models.BooleanField(default=False, null=False)
    done = models.BooleanField(default=False, null=False)
    user_task_owner = models.OneToOneField(User, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
