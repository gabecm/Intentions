"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import SignUpView
from . import views

app_name = 'intentions'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('entry/<int:pk>/', views.EntryView.as_view(), name='entry'),
    path('entry_page/', views.entry_page, name='entry_page'),
    path('entries/', views.EntriesView.as_view(), name='entries'),
    path('prompt/<int:pk>', views.PromptView.as_view(), name='prompt'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]
