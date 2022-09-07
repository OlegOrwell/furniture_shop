from django import forms
from .models import UserBase
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'id_user'}))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Password', 'id': 'login-pwd'}))


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label="Enter Username", min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, this field must be filled'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)


    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.object.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError('Username already exists')
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.object.filter(email=email).exists():
            raise forms.ValidationError('This email is already used, try another one')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


