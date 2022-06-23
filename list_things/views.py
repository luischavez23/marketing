from django.shortcuts import render
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
    form = RegisterForm( request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')

        print(username)
        print(password)
        print(email)
        
    return render(request, 'users/login.html', {'form':form})

def signup_view(request):
    return render(request, 'users/signup.html', {})