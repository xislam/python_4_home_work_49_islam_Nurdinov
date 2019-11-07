from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import IssueTracker, Project
from webapp.forms import IssueForm, SimpleSearchForm
from django.utils.http import urlencode


class IndexView(ListView):
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    model = IssueTracker
    paginate_by = 4
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(description__icontains=self.search_value) | Q(summary__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class IssueView(DetailView):
    template_name = 'issue/issue.html'
    context_object_name = 'issue'
    model = IssueTracker


class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = 'issue/create.html'

    model = IssueTracker

    form_class = IssueForm

    def get_form(self, form_class=None):
        form = super().get_form()
        # form.fields['created_by'].initial = self.request.user
        # form.fields['project'].initial = sel
        return form

    def form_valid(self, form):
        project = self.get_project()
        self.object = project.issue_project.create(**form.cleaned_data)
        self.object.created_by = self.request.user
        self.object.project = project
        self.object.save()
        return redirect('webapp:index')

    def get_project(self):
        project_pk = self.kwargs.get('pk')
        return get_object_or_404(Project, pk=project_pk)

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(UpdateView):
    model = IssueTracker
    template_name = 'issue/update.html'
    form_class = IssueForm
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class IssueDeleteView(DeleteView):
    model = IssueTracker
    template_name = 'issue/delete.html'
    form_class = IssueForm
    context_object_name = 'issue'
    page = 'index'

    def get_success_url(self):
        return reverse('webapp:index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)