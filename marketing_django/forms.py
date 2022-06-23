from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=6, max_length=50, 
                                widget=forms.TextInput(attrs={
                                    'class':'form-control mb-3',
                                    'id':'username'
                                }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'id':'password'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control mb-3', 'id':'email'}))