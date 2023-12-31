from django.urls import path

from . import views

app_name = 'buildings'

urlpatterns = [
    path('', views.index, name='index'),
    path('build_building/', views.build_building, name='build_building'),
    path('upgrade/', views.upgrade_building, name='upgrade_building'),
    path('save_eggs/', views.save_eggs, name='save_eggs'),
    path('collect_eggs/', views.collect_eggs, name='collect_eggs'),
]