from . import views
from django.urls import path

urlpatterns = [

    path('credentials',views.reg,name='reg'),
    path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),]
