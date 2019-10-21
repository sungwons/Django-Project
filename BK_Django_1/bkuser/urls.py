from django.urls import path
from . import views

urlpatterns = [
    # path('임의지정', views.함수이름)
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('', views.register)
]
