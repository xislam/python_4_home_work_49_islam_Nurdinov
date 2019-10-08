from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from webapp.views.views_detail import DetailView
from webapp.models import IssueTracker
from webapp.forms import IssueForm


class IndexView(ListView):
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    model = IssueTracker
    paginate_by = 4
    paginate_orphans = 1


class IssueView(DetailView):
    template_name = 'issue/issue.html'
    context_key = 'issue'
    model = IssueTracker


class IssueCreateView(CreateView):
    template_name = 'issue/create.html'

    model = IssueTracker

    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(TemplateView):

    def get(self, request, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        form = IssueForm(data={'summary': issue.summary,
                               'description': issue.description,
                               'type': issue.type_id,
                               'status': issue.status_id})

        return render(request, 'issue/update.html', context={'form': form, 'issue': issue})

    def post(self, request, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue.description = data['description']
            issue.summary = data['summary']
            issue.status_id = data['status']
            issue.type_id = data['type']
            issue.save()
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'issue/update.html', context={'form': form})


class IssueDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        return render(request, 'issue/delete.html', context={'issue': issue})

    def post(self, request, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])

        issue.delete()
        return redirect('index')
