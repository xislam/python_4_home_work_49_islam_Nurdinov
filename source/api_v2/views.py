from rest_framework import viewsets
from webapp.models import Project, IssueTracker
from api_v2.serializers import ProjectSerializer, IssueSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = IssueTracker.objects.all()
    serializer_class = IssueSerializer
