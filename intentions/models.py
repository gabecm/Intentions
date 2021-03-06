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
    mood = models.CharField(max_length=20, default='Okay')
    headspace = models.CharField(max_length=50)
    prompt_response = models.CharField(max_length=2000)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def get_entries(user):
        user_entries = Entry.objects.filter(user=user)
        return user_entries
