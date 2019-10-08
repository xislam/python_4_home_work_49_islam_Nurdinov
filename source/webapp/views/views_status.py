from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Status, IssueTracker
from webapp.forms import StatusForm, IssueForm
from webapp.views.views_detail import UpdateView, DeleteView


class StatusView(ListView):
    template_name = 'status/status_view.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(CreateView):
    template_name = 'status/create_status.html'

    model = Status

    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_view', kwargs={'pk': self.object.pk})


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'status/update_status.html'
    form_class = StatusForm
    object_name = 'status'

    def get_redirect_url(self):
        return reverse('task_view', kwargs={'pk': self.item.pk})


class StatusDeleteView(DeleteView):
    model = IssueTracker
    template_name = 'status/delete_status.html'
    form_class = StatusForm
    object_name = 'status'
    page = 'status_view'

    def get_redirect_url(self):
        return reverse('status_view')
