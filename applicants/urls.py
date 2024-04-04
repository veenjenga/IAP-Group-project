
from django.urls import path,include
from . import views

urlpatterns = [
     path('signup/', views.user_signup, name='signup'),
     path('signup-page/', views.show_signup, name= 'show_signup'),
     path('login/', views.user_login, name = 'login'),
     path('login-page/', views.show_login, name= 'show_login'),
     path('', views.show_home, name='homepage'),
     path('adminpage', views.show_admin, name = 'admin_dashboard'),
     path('userpage', views.show_user, name = 'user_dashboard')

]