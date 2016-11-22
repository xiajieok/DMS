from django.conf.urls import url, include
from fisherman import views

urlpatterns = [
    url(r'^$', views.index),
]
