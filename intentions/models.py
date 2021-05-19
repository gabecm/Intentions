from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


def today_prompt():
    try:
        return Prompt.objects.get(date__date=timezone.localtime(timezone.now()).date())
    except:
        return None


# Prompt Model
class Prompt(models.Model):
    prompt_text = models.CharField(max_length=200)
    date = models.DateTimeField('date')

    def __str__(self):
        return self.prompt_text


# Entries Model
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField('date published')
    mood = models.IntegerField(default=3)
    headspace = models.CharField(max_length=15)
    prompt_response = models.CharField(max_length=500)
    public = models.BooleanField(default=False)

    def get_entries(user):
        user_entries = Entry.objects.filter(user=user)
        return user_entries
