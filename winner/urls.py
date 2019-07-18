from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.win_Mercedes, name='winner'),
]