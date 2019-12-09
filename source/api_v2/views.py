from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Project, IssueTracker
from api_v2.serializers import ProjectSerializer, IssueSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # def get_permissions(self):
    #
    #     if self.request.method in SAFE_METHODS:
    #
    #         return []
    #
    #     return super().get_permissions()


class IssueViewSet(viewsets.ModelViewSet):
    queryset = IssueTracker.objects.all()
    serializer_class = IssueSerializer

    def get_permissions(self):

        if self.request.method in SAFE_METHODS:

            return []

        return super().get_permissions()


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})

