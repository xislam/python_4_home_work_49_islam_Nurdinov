from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import Type
from webapp.forms import TypeForm


class TypeView(TemplateView):
    template_name = 'type/type_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(View):

    def get(self, request, **kwargs):
        form = TypeForm()
        return render(request, 'type/type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Type.objects.create(type=data['type'])
            return redirect('type_view')
        else:
            return render(request, 'type/type_create.html', context={'form': form})


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
