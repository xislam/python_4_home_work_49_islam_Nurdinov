from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api_v2 import views
from api_v2.views import LogoutView

router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'issue', views.IssueViewSet)
app_name = 'api_v2'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_auth_token, name='obtain_auth_token'),
    path('logout/', LogoutView.as_view(), name='delete_auth_token')
]
