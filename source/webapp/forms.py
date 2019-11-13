
from django import forms
from django.contrib.auth.models import User

from accounts.models import Team
from webapp.models import Type, Status, IssueTracker, Project


class IssueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop('project')
        super().__init__(*args, **kwargs)
        teams = Team.objects.filter(project=self.project)
        users = []
        for team in teams:
            users.append(team.user.username)
        self.fields['assigned_to'] = forms.ModelChoiceField(queryset=User.objects.filter(username__in=users))

    class Meta:
        model = IssueTracker
        fields = ['summary', 'description', 'status', 'type']


class StatusForm(forms.ModelForm):
    class Meta:

        model = Status

        fields = ['status']


class TypeForm(forms.ModelForm):
    class Meta:

        model = Type

        fields = ['type']


class ProjectForm(forms.ModelForm):

    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:

        model = Project

        fields = ['name_project', 'description_project', 'users']


class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Найти")