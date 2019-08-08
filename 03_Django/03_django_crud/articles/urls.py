from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index),
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
]
