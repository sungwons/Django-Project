from django.urls import path
from . import views

urlpatterns = [
    # path('임의지정', views.함수 이름)
    path('list/', views.board_list),
    path('write/', views.board_write),
    path('detail/<int:pk>', views.board_detail),
    ]

