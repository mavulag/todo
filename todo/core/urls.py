from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^dashboard/edit-task/(?P<id>\d+)/$', views.edit_task, name='edit_task'),
    url(r'^dashboard/delete-task/(?P<id>\d+)/$', views.delete_task, name='delete_task'),
]