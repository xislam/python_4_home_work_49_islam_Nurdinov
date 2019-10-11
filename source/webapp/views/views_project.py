from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Project
from webapp.forms import ProjectForm


class ProjectView(ListView):
    template_name = 'project/view_project.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['created_at']

    def get_queryset(self):
        return Project.objects.all().order_by('created_at')


class ProjectDetailView(DetailView):
    template_name = 'project/projects.html'
    context_key = 'project'
    model = Project


class ProjectCreateView(CreateView):
    template_name = 'project/create.html'

    model = Project

    form_class = ProjectForm

    def get_success_url(self):
        return reverse('view_project')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    object_name = 'project'

    def get_redirect_url(self):
        return reverse('view_project')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    form_class = ProjectForm
    object_name = 'project'
    page = 'error.html'

    def get_success_url(self):
        return reverse('view_project')
