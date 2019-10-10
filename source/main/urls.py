"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/<int:pk>/edit/', IssueUpdateView.as_view(), name='update'),
    path('issue/<int:pk>/', IssueView.as_view(), name='issue_view'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='delete'),
    path('status/create/', StatusCreateView.as_view(), name='create_status'),
    path('status/', StatusView.as_view(), name='status_view'),
    path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name='update_status'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='delete_status'),
    path('type/create/', TypeCreateView.as_view(), name='type_create'),
    path('type/', TypeView.as_view(), name='type_view'),
    path('type/<int:pk>/edit/', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),

]