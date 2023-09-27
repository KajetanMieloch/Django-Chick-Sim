from django.urls import path

from . import views

app_name = 'market'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy_sell_eggs/', views.buy_sell_eggs, name='buy_sell_eggs'),
]
