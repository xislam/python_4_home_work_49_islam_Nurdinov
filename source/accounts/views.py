from django.db import transaction
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from accounts.models import Token
from accounts.forms import SignUpForm, PasswordChangeForm, UserForm, UrlForm


def login_view(request):
    context = {}
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '')
            if next_url:
                return redirect(next_url)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:index')


def register_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'register.html', context={'form': form})
    elif request.method == 'POST':
        form = SignUpForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                is_active=True
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('accounts:login')
        return render(request, 'register.html', context={'form': form})


def user_activate_view(request, token):
    token = get_object_or_404(Token, token=token)
    user = token.user
    user.is_active = True
    user.save()
    login(request, user)
    return redirect('webapp:index')


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


# class UserPersonalInfoChangeView(UpdateView):
#     model = User
#     template_name = 'user_info_change.html'
#     form_class = UserChangeForm
#     context_object_name = 'user_obj'
#
#     def get_success_url(self):
#         return reverse('accounts:detail', kwargs={'pk': self.object.pk})
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.pk != self.kwargs['pk']:
#             return HttpResponseForbidden()
#
#         return super().dispatch(request, *args, **kwargs)


class UserPasswordChangeView(UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != self.kwargs['pk']:
            return HttpResponseForbidden()

        return super().dispatch(request, *args, **kwargs)


class UserView(ListView):
    template_name = 'user_data.html'
    context_object_name = 'user_list'
    model = User
    paginate_by = 4
    paginate_orphans = 1


@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UrlForm(request.POST, instance=request.user.accounts_url)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('webapp:index')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UrlForm(instance=request.user.accounts_url)
        return render(request, 'user_info_change.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })