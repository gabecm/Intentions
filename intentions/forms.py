from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from intentions.models import Entry, Prompt, today_prompt

MOOD_CHOICES = [
    ('Bad', 'Bad'),
    ('Not Good', 'Not Good'),
    ('Okay', 'Okay'),
    ('Pretty Good', 'Pretty Good'),
    ('Great!', 'Great!'),
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
    if today_prompt() is not None:
        prompt_text = today_prompt().prompt_text
    else:
        prompt_text = ''

    mood = forms.ChoiceField(
        choices=MOOD_CHOICES, widget=forms.RadioSelect(attrs={'required': 'required'}),
        label='How are you feeling today?')

    headspace = forms.CharField(
        label='What is taking up most of my headspace? (50 Char)',
        max_length=15,
    )

    prompt_response = forms.CharField(
        label=prompt_text + ' (2000 Char)',
        max_length=2000,
        widget=forms.Textarea,
    )

    public = forms.BooleanField(
        label='I would like this entry to be public',
        required=False,
    )

    class Meta:
        model = Entry
        fields = ['mood', 'headspace', 'prompt_response', 'public']
