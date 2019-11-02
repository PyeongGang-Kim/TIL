from django.urls import path
from . import views

app_name= 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('', views.index, name='index'),
]

