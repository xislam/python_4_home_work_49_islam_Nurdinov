
from django import forms
from webapp.models import Type, Status, IssueTracker, Project


class IssueForm(forms.ModelForm):

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
    class Meta:

        model = Project

        fields = ['name_pj', 'description_pj']

