from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), # GET
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'), # GET 작성, POST 생성
    path('<int:article_pk>/', views.detail, name='detail'), # GET
    path('<int:article_pk>/delete/', views.delete, name='delete'), # POST
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'), # GET 수정, POST 업데이트
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/<int:comment_pk>/comment_delete/', views.comment_delete, name='comment_delete')
]
