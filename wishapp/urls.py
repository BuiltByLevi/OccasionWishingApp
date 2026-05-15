from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wall/', views.friends_wall, name='friends_wall'),
    path('add-friend/', views.add_friend, name='add_friend'),
]