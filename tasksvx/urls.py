from django.conf.urls import url, include
from django.contrib import admin

from tasks import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/', include('users.urls')),
    url(
        r'^tasks/$',
        views.TasksList.as_view(),
        name=views.TasksList.name
    ),
    url(
        r'^tasks/(?P<pk>[0-9]+)/$',
        views.TasksDetail.as_view(),
        name=views.TasksDetail.name
    ),
    url(
        r'^tasks/(?P<pk>[0-9]+)/finish/$',
        views.TasksDone.as_view(),
        name=views.TasksDetail.name
    ),
]
