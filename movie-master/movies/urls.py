from django.conf.urls import url
from .views import *

urlpatterns = [
    url('movies', IndexView.as_view(), name='index'),
]
