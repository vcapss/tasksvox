from django.conf.urls import url
from tasks import views


urlpatterns = [
    url(
        r'^$',
        views.TasksList.as_view(),
        name=views.TasksList.name
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.TasksDetail.as_view(),
        name=views.TasksDetail.name
    ),
    url(
        r'^(?P<pk>[0-9]+)/finish/$',
        views.TasksDone.as_view(),
        name=views.TasksDetail.name
    ),
]
