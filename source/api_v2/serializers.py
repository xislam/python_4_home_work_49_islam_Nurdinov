from rest_framework import serializers
from webapp.models import Project, IssueTracker


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueTracker
        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'date_ct', 'created_by', 'assigned_to')


class ProjectSerializer(serializers.ModelSerializer):
    issue_project = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name_project', 'description_project', 'created_at', 'updated_at', 'issue_project')

