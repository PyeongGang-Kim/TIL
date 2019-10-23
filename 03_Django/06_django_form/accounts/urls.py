from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),

    # signup 이나 login이라는 유저네임이 있으면 문제가 발생할 수 있기 때문에 아래의 항목을 맨 위에 두면 안된다.
    # 순차 접근하기 때문임.
    path('<username>/', views.profile, name='profile'),

]