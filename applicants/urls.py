
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('signup/', views.user_signup, name='signup'),
     path('signup-page/', views.show_signup, name= 'show_signup'),
     path('login/', views.user_login, name = 'login'),
     path('login-page/', views.show_login, name= 'show_login'),
     path('', views.show_home, name='homepage'),
     path('adminpage', views.show_admin, name = 'admin_dashboard'),
     path('userpage', views.show_user, name = 'user_dashboard'),
     path('create_job/', views.create_job, name='create_job'),
     path('show_createjob', views.create_job_template, name = 'create_new_job'), # render template

     path('search_jobs/', views.search_jobs, name='search_jobs'),
     path('submit_application/', views.submit_application, name='submit_application'),
     path('apply/',views.apply, name = 'apply_jobs'),

     path('my_applications/', views.user_applications, name='user_applications'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)