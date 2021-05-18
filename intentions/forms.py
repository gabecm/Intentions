from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from intentions.models import Entry, Prompt, today_prompt

MOOD_CHOICES = [
    (1, 'Bad'),
    (2, 'Not Good'),
    (3, 'Okay'),
    (4, 'Pretty Good'),
    (5, 'Great!'),
]


# Custom User Creation Form
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EntryForm(forms.ModelForm):
    mood = forms.ChoiceField(
        choices=MOOD_CHOICES, widget=forms.RadioSelect,
        label='How are you feeling today?')

    headspace = forms.CharField(
        label='What is taking up most of my headspace? (15 Char)',
        max_length=15,
    )

    prompt_response = forms.CharField(
        label=today_prompt().prompt_text + ' (500 Char)',
        max_length=500,
        widget=forms.Textarea,
    )

    public = forms.BooleanField(
        label='I would like this entry to be public',
        required=False,
    )

    class Meta:
        model = Entry
        fields = ['mood', 'headspace', 'prompt_response', 'public']
