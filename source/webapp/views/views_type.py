from django.shortcuts import redirect
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
        return reverse('webapp:type_view')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('webapp:type_view')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/type_delete.html'
    form_class = TypeForm
    context_object_name = 'type'
    page = 'type_view'

    def get_success_url(self):
        return reverse('webapp:type_view')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
