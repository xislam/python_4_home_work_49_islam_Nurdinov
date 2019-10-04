
from django import forms
from webapp.models import Type, Status


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='краткое описание')
    description = forms.CharField(max_length=3000, required=False, label='Описание')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, widget=forms.Select)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, widget=forms.Select)


class StatusForm(forms.Form):
    status = forms.CharField(max_length=20, required=True, label='Статус')


class TypeForm(forms.Form):
    type = forms.CharField(max_length=20, required=True, label='Тип')


