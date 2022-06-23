from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/login', views.login_view, name='login'),
    path('user/signup', views.signup_view, name='signup')
]
