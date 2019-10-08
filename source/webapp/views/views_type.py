from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Type, IssueTracker
from webapp.forms import TypeForm, IssueForm
from webapp.views.views_detail import UpdateView


class TypeView(ListView):
    template_name = 'type/type_view.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(CreateView):
    template_name = 'type/type_create.html'

    model = IssueTracker

    form_class = IssueForm

    def get_success_url(self):
        return reverse('type_view', kwargs={'pk': self.object.pk})


class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    form_class = TypeForm
    object_name = 'type'

    def get_redirect_url(self):
        return reverse('type_view', kwargs={'pk': self.item.pk})


class TypeDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        typ = get_object_or_404(Type, pk=kwargs['pk'])
        return render(request, 'type/type_delete.html', context={'type': typ})

    def post(self, request, **kwargs):
        types = get_object_or_404(Type, pk=kwargs['pk'])
        try:
            types.delete()
            return redirect('type_view')
        except Exception:
            return redirect('type_view')
