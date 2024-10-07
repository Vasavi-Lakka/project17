"""
URL configuration for project17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_Dept/', insert_Dept, name='insert_Dept'),
    path('insert_Emp/', insert_Emp, name='insert_Emp'),
    path('displayDept/', displayDept, name='displayDept'),
    path('displayEmp/', displayEmp, name='displayEmp'),
    path('empdept/', empdept, name='empdept'),
    path('empmgr/', empmgr, name='empmgr'),
    path('empdeptmgr/', empdeptmgr, name='empdeptmgr'),

]
