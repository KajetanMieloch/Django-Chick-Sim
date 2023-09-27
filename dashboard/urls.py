from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('chart_data/', views.chart_data, name='chart_data'),
]
