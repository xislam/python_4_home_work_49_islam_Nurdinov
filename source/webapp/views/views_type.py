from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.models import Type
from webapp.forms import TypeForm


class TypeView(ListView):
    template_name = 'type/type_view.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(CreateView):
    template_name = 'type/type_create.html'

    model = Type

    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_view')


class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    form_class = TypeForm
    object_name = 'type'

    def get_redirect_url(self):
        return reverse('type_view')


class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/type_delete.html'
    form_class = TypeForm
    object_name = 'type'
    page = 'type_view'

    def get_redirect_url(self):
        return reverse('type_view')
