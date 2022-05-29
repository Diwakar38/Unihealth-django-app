from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [    #URL dispatching.....
    path('', views.login, name='index'),  #calls the index function from view
    path('index',views.index, name= 'index'),  #calls about function from view
    path('login',views.login, name= 'login'),
    path('register',views.register, name= 'register')
]