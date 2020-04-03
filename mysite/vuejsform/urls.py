from django.conf.urls import include
from django.urls import path
from .router import router

from . import views

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
]
