from django.urls import path

from . import views

app_name = 'buildings'

urlpatterns = [
    path('', views.index, name='index'),
    path('build_building/', views.build_building, name='build_building'),
]