from django.urls import path
from .views import *

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/add/project/<int:pk>/', IssueCreateView.as_view(), name='issue_add'),
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

    path('project/create/', ProjectCreateView.as_view(), name='create_project'),
    path('project/', ProjectView.as_view(), name='view_project'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('project/<int:pk>/',  ProjectDetailView.as_view(), name='projects'),
]