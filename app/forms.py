from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer


class CustomerRegistrationForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': True}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        # widget = {'username': forms.TextInput(
        #     attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'current-password'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autofocus': True, 'autocomplete': 'current-password'}))
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'autocomplete': 'email'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'new-password'}))


class CustomerProfileForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    locality = forms.CharField(
        label=_('Locality'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    # state = forms.CharField(label=_('State'),widget=forms.TextInput(attrs={'class': 'form-control'}))
    zipcode = forms.CharField(label=_('Zipcode'), widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone_number = forms.IntegerField(
        label=_('Mobile No.'), widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'locality', 'state', 'zipcode']

        # widget = {'name':forms.TextInput(attrs={'class': 'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}),'state':forms.TextInput(attrs={'class': 'form-control'}),'zipcode':forms.TextInput(attrs={'class': 'form-control'})}


class contactformemail(forms.Form):
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'style': 'height: 150px;'}))
