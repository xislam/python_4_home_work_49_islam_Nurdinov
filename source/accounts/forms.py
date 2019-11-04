from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from accounts import admin
from accounts.models import Url, Team


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Username')
    first_name = forms.CharField(max_length=100, required=False, label='first_name')
    last_name = forms.CharField(max_length=100, required=False, label='last_name')
    password = forms.CharField(max_length=100, required=True, label='Password',
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label='Password confirm',
                                       widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label='Email')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('Username already taken.', code='username_taken')
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('Email already registered.', code='email_registered')
        except User.DoesNotExist:
            return email

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        if password_1 != password_2:
            raise ValidationError('Passwords do not match.', code='passwords_do_not_match')
        last_name = self.cleaned_data.get('last_name')
        first_name = self.cleaned_data.get('first_name')
        if not last_name and not first_name:
            raise ValidationError('Напешите инециалы',  code='not last_name and not first_name')

        return self.cleaned_data


class UserChangeForm(forms.ModelForm):
    #
    #
    #

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)
        return super().get_initial_for_field(field, field_name)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        profile_fields = ['url', 'avatar', 'description']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}

    def save(self, commit=True):

        user = super().save(commit)

        self.save_profile(commit)

        return user

    def save_profile(self, commit=True):

        profile = self.instance.profile

        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data[field])

        if not profile.avatar:
            profile.avatar = None

        if commit:
            profile.save()


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['url', 'avatar', 'description']

    def clean_url(self):
        git = 'https://github.com/'
        github = self.cleaned_data['url']
        git_start = github.startswith(git)
        if git_start == False:
            raise ValidationError('error')
        return github


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['user', 'project']




