from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.views.generic.base import View


class DetailView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = get_object_or_404(self.model, pk=kwargs['pk'])
        return context


class UpdateView(View):
    form_class = None

    template_name = None

    redirect_url = ''

    model = None

    key_kwarg = 'pk'

    context_key = 'object'

