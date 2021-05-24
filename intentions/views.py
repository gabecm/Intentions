from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from intentions.forms import NewUserForm
from django.views import generic
from django.urls import reverse_lazy, reverse

from intentions.models import Prompt, Entry, today_prompt
from .forms import EntryForm
import datetime

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
        form = EntryForm(request.POST or None)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = user
            new_entry.prompt = prompt
            new_entry.date = timezone.now()
            new_entry.save()
        return HttpResponseRedirect(reverse('intentions:dashboard'))

    form = EntryForm()
    return render(request, 'intentions/entry_page.html', {'form': form})


class EntryView(generic.DetailView):
    model = Entry
    template_name = 'intentions/entry.html'

    def get_queryset(self):
        return Entry.objects.filter(date__lte=timezone.localtime(timezone.now()))


class EntriesView(generic.ListView):
    template_name = 'intentions/entries.html'
    context_object_name = 'entries'

    def get_queryset(self):
        entries = Entry.objects.filter(user=self.request.user,).order_by('-date')
        query = self.request.GET.get('title')
        sort = self.request.GET.get('sort')
        filter = self.request.GET.get('filter')
        if query:
            entries = entries.filter(prompt__prompt_text__icontains=query)
        if sort:
            entries = entries.order_by(sort)
        if filter:
            today = datetime.date.today()
            if filter == 'week':
                start_week = today - datetime.timedelta(today.weekday())
                end_week = start_week + datetime.timedelta(days=7)
                entries = entries.filter(date__range=[start_week, end_week])
            if filter == 'month':
                entries = entries.filter(date__month=today.month, date__year=today.year)
            if filter == 'year':
                entries = entries.filter(date__year=today.year)
        return entries

    def get_context_data(self):
        context = super(EntriesView, self).get_context_data()
        query = self.request.GET.get('title')
        sort = self.request.GET.get('sort')
        filter = self.request.GET.get('filter')
        if query:
            context['query'] = query
        else:
            context['query'] = ''
        if sort:
            context['sort'] = sort
        if filter:
            context['filter'] = filter
        return context


class PromptView(generic.DetailView):
    model = Prompt
    template_name = 'intentions/prompt.html'


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
