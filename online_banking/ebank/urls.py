from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('apply/', views.apply, name='apply'),
    path('apply/appform/', views.app_form, name='appform'),
    path('logout/',views.logout,name="logout"),

]
