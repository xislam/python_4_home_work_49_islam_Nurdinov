from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Project
from webapp.forms import ProjectForm, SimpleSearchForm


class ProjectView(ListView):
    template_name = 'project/view_project.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['created_at']
    paginate_by = 3
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
            query = Q(name_project__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectDetailView(DetailView):
    template_name = 'project/projects.html'
    context_object_name = 'project'
    model = Project


class ProjectCreateView(CreateView):
    template_name = 'project/create.html'

    model = Project

    form_class = ProjectForm

    def get_success_url(self):
        return reverse('webapp:view_project')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('webapp:view_project')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    form_class = ProjectForm
    context_object_name = 'project'
    page = 'error.html'

    def get_success_url(self):
        return reverse('webapp:view_project')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)