from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Type, IssueTracker
from webapp.forms import TypeForm, IssueForm
from webapp.views.views_detail import UpdateView, DeleteView


class TypeView(ListView):
    template_name = 'type/type_view.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(CreateView):
    template_name = 'type/type_create.html'

    model = Type

    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_view', kwargs={'pk': self.object.pk})


class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    form_class = TypeForm
    object_name = 'type'

    def get_redirect_url(self):
        return reverse('type_view', kwargs={'pk': self.item.pk})


class TypeDeleteView(DeleteView):
    model = IssueTracker
    template_name = 'type/type_delete.html'
    form_class = TypeForm
    object_name = 'type'
    page = 'type_view'

    def get_redirect_url(self):
        return reverse('type_view')
