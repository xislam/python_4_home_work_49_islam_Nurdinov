from rest_framework import serializers
from webapp.models import Project, IssueTracker


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Project

        fields = ('id', 'name_project', 'description_project', 'created_at', 'updated_at')


class IssueSerializer(serializers.ModelSerializer):

    class Meta:

        model = IssueTracker

        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'date_ct', 'created_by', 'assigned_to')
