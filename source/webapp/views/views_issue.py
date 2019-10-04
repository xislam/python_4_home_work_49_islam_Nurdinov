from django.views.generic import TemplateView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from webapp.views.views_detail import DetailView
from webapp.models import IssueTracker
from webapp.forms import IssueForm


class IndexView(ListView):
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    model = IssueTracker
    paginate_by = 4
    paginate_orphans = 1


class IssueView(DetailView):
    template_name = 'issue/issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_pk = kwargs.get('pk')
        context['issue'] = get_object_or_404(IssueTracker, pk=context_pk)
        return context


class IssueCreateView(View):
    def get(self, request, **kwargs):
        form = IssueForm()
        return render(request, 'issue/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue = IssueTracker.objects.create(summary=data['summary'],
                                                description=data['description'],
                                                status=data['status'],
                                                type=data['type'])
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'issue/create.html', context={'form': form})


class IssueUpdateView(TemplateView):

    def get(self, request, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        form = IssueForm(data={'summary': issue.summary,
                               'description': issue.description,
                               'type': issue.type_id,
                               'status': issue.status_id})

        return render(request, 'issue/update.html', context={'form': form, 'issue': issue})

    def post(self, request, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue.description = data['description']
            issue.summary = data['summary']
            issue.status_id = data['status']
            issue.type_id = data['type']
            issue.save()
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'issue/update.html', context={'form': form})


class IssueDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])
        return render(request, 'issue/delete.html', context={'issue': issue})

    def post(self, request, **kwargs):
        issue = get_object_or_404(IssueTracker, pk=kwargs['pk'])

        issue.delete()
        return redirect('index')
