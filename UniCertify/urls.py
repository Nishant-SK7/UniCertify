"""
URL configuration for UniCertify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from core import views as core_views
from accounts import views as accounts_views
from students import views as students_views
from admins import views as admins_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),
    path('admin_login/', accounts_views.admin_login, name='admin_login'),
    path('student_login/', accounts_views.student_login, name='student_login'),
    path('signup/', accounts_views.signup, name='signup'),
    path('student_dashboard/', students_views.student_dashboard, name='student_dashboard'),
    path('admin_dashboard/', admins_views.admin_dashboard, name='admin_dashboard'),
    path('upload/', core_views.file_upload, name='file_upload'),

]
