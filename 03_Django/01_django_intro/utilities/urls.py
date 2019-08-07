from django.urls import path
from . import views

urlpatterns = [
    # 메인 페이지 
    path('', views.index),
    path('papago/', views.papago),
    path('translated/', views.translated),
]