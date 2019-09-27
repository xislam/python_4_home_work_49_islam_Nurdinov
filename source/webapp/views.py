from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.models import IssueTracker, Type, Status
from webapp.forms import IssueForm, TypeForm, StatusForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = IssueTracker.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        return context


class IssueCreateView(View):

    def get_context_data(self, request, **kwargs):
        form = IssueForm()
        return render(request, 'create.html', context={'form': form})

    def post_context_data(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue = IssueTracker.objects.create(summary=data['summary'],
                                                description=data['description'],
                                                status=data['status'], type=data['type'])
            return redirect('task_view', pk=issue.pk)
        else:
            return render(request, 'create.html', context={'form': form})


class IssueUpdateView(TemplateView):

    def get(self, request, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        form = IssueForm(data={'summary': issue.summary,
                               'description': issue.description,
                               'type': issue.type,
                               'status': issue.status})

        return render(request, 'update.html', context={'form': form, 'issue': issue})

    def post(self, request, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue.description = data['description']
            issue.summary = data['summary']
            issue.status = data['status']
            issue.type = data['type']
            issue.save()
            return redirect('task_view', pk=issue.pk)
        else:
            return render(request, 'update.html', context={'form': form})


class TaskDeleteView(TemplateView):
    def get_context_data(self, request, *args, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        return render(request, 'delete.html', context={'issue': issue})

    def post_context_data(self, request, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])

        issue.delete()
        return redirect('index')


class TypeView(TemplateView):

    name = 'types.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(View):

    def get_context_data(self, request, **kwargs):
        form = TypeForm()
        return render(request, 'type_create.html', context={'form': form})

    def post_context_data(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.isvalid():
            data = form.cleaned_data
            Type.objects.create(type=data['type'])
            return redirect('type_view')
        else:
            return render(request, 'type_create.html', context={'form': form})


class TypeUpdateView(TemplateView):

    def get_context_data(self, request, **kwargs):
        types = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data={'type': types.type})
        return render(request, 'type_update.html', context={'form': form, 'type': type})

    def post_context_data(self, request, **kwargs):
        types = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            types.type = data['type']
            types.save()
            return redirect('types_view')
        else:
            return render(request, 'type_update.html', context={'form': form})


class TypeDeleteView(TemplateView):
    def get_context_data(self, request, *args, **kwargs):
        types = get_object_or_404(Type, pk=kwargs['pk'])
        return render(request, 'type_delete.html', context={'type': type})

    def post_context_data(self, request, **kwargs):
        types = get_object_or_404(Type, pk=kwargs['pk'])

        types.delete()
        return redirect('types_view')


class StatusView(TemplateView):

    name = 'status_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class StatusCreateView(View):

    def get_context_data(self, request, **kwargs):
        form = StatusForm()
        return render(request, 'status_create.html', context={'form': form})

    def post_context_data(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Status.objects.create(status=data['status'])
            return redirect('status_view')
        else:
            return render(request, 'status_create.html', context={'form': form})


class StatusUpdateView(TemplateView):

    def get_context_data(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data={'status': status.status})
        return render(request, 'status_update.html', context={'form': form,
                                                              'status': status})

    def post_context_data(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            status.status = data['status']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'status_update.html', context={'form': form})


class StatusDeleteView(TemplateView):
    def get_context_data(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'status_delete.html', context={'status': status})

    def post_context_data(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])

        status.delete()
        return redirect('status_view')