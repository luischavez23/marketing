from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from marketing_django.forms import RegisterForm

def index(request):
    return render(request, 'list_things/index.html', {
        'title': 'Product List',
        'items':[
            {'id':1, 'item': 'T-Shirt', 'available': True},
            {'id':2, 'item': 'Jeans', 'available': True},
            {'id':3, 'item': 'Backpack', 'available': True},
            {'id':4, 'item': 'Hat', 'available': False},
            {'id':5, 'item': 'Shirt', 'available': True},
        ]
    })

def login_view(request):
    return render(request, 'users/login.html', {})

def signup_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'User created satisfactory')
            return redirect('index')

    return render(request, 'users/signup.html', {'form': form})