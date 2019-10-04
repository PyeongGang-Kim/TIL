from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('new/', views.new),
    path('<int:pk>/', views.detail),
    path('update/<int:pk>/', views.update),
    path('delete/<int:pk>/', views.delete),
    path('edit/<int:pk>/', views.edit),
]