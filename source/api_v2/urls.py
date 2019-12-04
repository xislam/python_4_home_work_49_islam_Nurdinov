from django.urls import include, path
from rest_framework import routers
from api_v2 import views

router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'issue', views.IssueViewSet)
app_name = 'api_v2'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
