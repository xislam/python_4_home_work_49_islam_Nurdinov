from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.models import Status
from webapp.forms import StatusForm


class StatusView(ListView):
    template_name = 'status/status_view.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(CreateView):
    template_name = 'status/create_status.html'

    model = Status

    form_class = StatusForm

    def get_success_url(self):
        return reverse('webapp:status_view')


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'status/update_status.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('webapp:status_view')


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'status/delete_status.html'
    form_class = StatusForm
    context_object_name = 'status'
    page = 'error.html'

    def get_success_url(self):
        return reverse('webapp:status_view')
