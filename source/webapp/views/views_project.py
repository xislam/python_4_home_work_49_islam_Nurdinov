from django.urls import reverse
from django.views.generic import ListView, CreateView
from webapp.models import Project
from webapp.forms import ProjectForm
from webapp.views.views_detail import UpdateView, DeleteView


class ProjectView(ListView):
    template_name = 'project/view.html'
    context_object_name = 'projects'
    model = Project


class ProjectCreateView(CreateView):
    template_name = 'project/create.html'

    model = Project

    form_class = ProjectForm

    def get_success_url(self):
        return reverse('view')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    object_name = 'project'

    def get_redirect_url(self):
        return reverse('view')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    form_class = ProjectForm
    object_name = 'project'
    page = 'error.html'

    def get_redirect_url(self):
        return reverse('view')
