from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class DetailView(TemplateView):
    model = None
    issue_key = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.issue_key] = get_object_or_404(self.model, pk=kwargs['pk'])
        return context
