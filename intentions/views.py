from django.shortcuts import render
from intentions.forms import NewUserForm
from django.views import generic
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Create your views here.


def home(request):
    context = {}
    return render(request, 'intentions/home.html', context)


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
