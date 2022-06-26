from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=6, max_length=50, 
                                widget=forms.TextInput(attrs={
                                    'class':'form-control mb-3',
                                    'id':'username'
                                }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control mb-3', 'id':'email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'id':'password'}))
    confirm = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'label':'Confirm password','class': 'form-control mb-3', 'id':'confirm'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The password is already user')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email is already used')
        return email
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('confirm') != cleaned_data.get('password'):
            self.add_error('confirm', 'The confirm password doesn\'t match to the password')
    
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('password'),
            self.cleaned_data.get('email')
        )