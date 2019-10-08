from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Type, IssueTracker
from webapp.forms import TypeForm, IssueForm


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


class TypeUpdateView(TemplateView):

    def get(self, request, **kwargs):
        types = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data={'type': types.type})
        return render(request, 'type/type_update.html', context={'form': form, 'type': type})

    def post(self, request, **kwargs):
        types = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            types.type = data['type']
            types.save()
            return redirect('issue_view')
        else:
            return render(request, 'type/type_update.html', context={'form': form})


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
