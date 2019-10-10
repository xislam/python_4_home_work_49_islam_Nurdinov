from django.urls import reverse
from django.views.generic import ListView, CreateView
from webapp.views.views_detail import DetailView, UpdateView, DeleteView
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


class IssueUpdateView(UpdateView):
    model = IssueTracker
    template_name = 'issue/update.html'
    form_class = IssueForm
    object_name = 'issue'

    def get_redirect_url(self):
        return reverse('issue_view', kwargs={'pk': self.item.pk})


class IssueDeleteView(DeleteView):
    model = IssueTracker
    template_name = 'issue/delete.html'
    form_class = IssueForm
    object_name = 'issue'
    page = 'index'

    def get_redirect_url(self):
        return reverse('index')
