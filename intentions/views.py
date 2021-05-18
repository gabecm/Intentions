from django.http import HttpResponseRedirect
from django.shortcuts import render
from intentions.forms import NewUserForm
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'intentions/home.html')


def dashboard(request):
    user = request.user
    entries = []
    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('intentions:home'))

    context = {
        'entries': entries
    }

    return render(request, 'intentions/dashboard.html', context)


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
