from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/update/', views.update, name='update'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    path('<int:article_id>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:comment_id>/comment_delete/', views.comment_delete, name='comment_delete'),

]