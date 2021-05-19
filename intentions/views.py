from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from intentions.forms import NewUserForm
from django.views import generic
from django.urls import reverse_lazy, reverse

from intentions.models import Prompt, Entry, today_prompt
from .forms import EntryForm
import datetime
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'intentions/home.html')


def dashboard(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('intentions:home'))

    count = len(Entry.get_entries(user))
    entries = Entry.get_entries(user).order_by('-date')[:5]
    prompt = today_prompt()
    context = {
        'entries': entries,
        'prompt': prompt,
        'count': count,
    }

    return render(request, 'intentions/dashboard.html', context)


def entry_page(request):
    user = request.user
    prompt = today_prompt()

    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('intentions:home'))
    if request.method == 'POST':
        new_entry = Entry(
            user=user,
            prompt=prompt,
            date=timezone.now(),
            mood=request.POST.get('mood'),
            headspace=request.POST.get('headspace'),
            prompt_response=request.POST.get('prompt_response')
        )
        new_entry.save()
        return HttpResponseRedirect(reverse('intentions:dashboard'))

    form = EntryForm()
    return render(request, 'intentions/entry_page.html', {'form': form})


class EntriesView(generic.ListView):
    template_name = 'intentions/entries.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return Entry.objects.filter(
            user=self.request.user,
        ).order_by('-date')


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
