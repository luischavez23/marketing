from django.shortcuts import render

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

def login(request):
    return render(request, 'users/login.html',{})