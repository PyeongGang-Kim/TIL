from django.urls import path
from . import views

urlpatterns = [

    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('islotto', views.islotto),
    path('ispal/<word>', views.ispal),
    path('isbirth/<int:month>/<int:day>', views.isbirth),
    path('template_language/', views.template_language),
    path('area/<int:r>', views.area),
    path('product/<int:num1>/<int:num2>', views.product),
    path('prod/<str:name>/<int:age>', views.prod),
    path('hello/<str:name>/<int:age>', views.hello),
    path('image/', views.image),
    path('dinner/', views.dinner),
    path('index/', views.index),
    path('introduce/', views.introduce),
]