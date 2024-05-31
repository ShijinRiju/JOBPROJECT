"""
URL configuration for JOBPROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from JOBAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register/',views.register),
    path('signin/',views.signin),
    path('signout/',views.signout),
    path('user_index/',views.user_index),    
    path('job_listing/',views.job_listing),    
    path('admin_index/',views.admin_index),    
    path('job_publish/',views.job_publish),    
    path('job_details/',views.job_details), 
    path('job_apply/',views.job_apply), 
    path('my_jobs/',views.my_jobs), 
    path('applicant_details/',views.applicant_details), 
    path('applications/',views.applications), 
    path('approve_application/',views.approve_application), 
    path('reject_application/',views.reject_application), 
]
