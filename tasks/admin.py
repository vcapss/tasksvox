from django.contrib import admin

from tasks.models import Tasks, Files

admin.site.register(Tasks)
admin.site.register(Files)
