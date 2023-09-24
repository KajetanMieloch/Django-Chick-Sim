from django.urls import path

from . import views

app_name = 'henHouse'

urlpatterns = [
    path('', views.index, name='index')
]