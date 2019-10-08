from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Status, IssueTracker
from webapp.forms import StatusForm, IssueForm
from webapp.views.views_detail import UpdateView


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


class StatusDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'status/delete_status.html', context={'status': status})

    def post(self, request, *args,  **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        try:
            status.delete()
            return redirect('status_view')
        except Exception:
            return redirect('status_view')
