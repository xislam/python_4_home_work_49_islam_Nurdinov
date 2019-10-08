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
    model = None
    redirect_url = ''
    pk_kwargs = 'pk'
    object_name = None
    item = None

    def get(self, request, **kwargs):
        item = self.get_item()
        form = self.form_class(instance=item)
        return render(request, self.template_name, context={'form': form, self.object_name: item})

    def post(self, request, **kwargs):
        item = self.get_item()
        form = self.form_class(instance=item, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.item = self.get_item()
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})

    def get_redirect_url(self):
        return self.redirect_url

    def get_item(self):
        pk = self.kwargs.get(self.pk_kwargs)
        item = get_object_or_404(self.model, pk=pk)
        return item


