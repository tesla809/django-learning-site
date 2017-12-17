"""url to route views for courses app."""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_list)
]
