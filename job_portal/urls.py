"""
URL configuration for job_portal project.

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

from django.urls import path
from django.contrib import admin
from jobs import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/home_appliciant/', views.home_appliciant, name='home_appliciant'),
    path('register/home_company/', views.home_company, name='home_company'),
    path('', views.home_page, name='home'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('create/job/', views.create_job_view, name='create_job'),
    path('create/resume/', views.create_resume_view, name='create_resume'),
    path('jobs/', views.job_list_view, name='job_list'),
    path('resumes/', views.resume_list_view, name='resume_list'),
    path('create-vacancy/', views.create_vacancy, name='create_vacancy'),
    path('create-resume/', views.create_resume, name='create_resume'),
]


