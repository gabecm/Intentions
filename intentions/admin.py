from django.contrib import admin

# Register your models here.
from intentions.models import Prompt, Entry


class PromptAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['prompt_text']}),
        ('Date Information', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    list_display = ('prompt_text', 'date')
    list_filter = ['date']
    search_fields = ['prompt_text']


class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['user', 'prompt', 'mood', 'headspace',
                                    'prompt_response', 'public']}),
        ('Date Information', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    list_display = ('user', 'prompt', 'mood', 'headspace', 'prompt_response', 'public')
    list_filter = ['date']
    search_fields = ['user']


admin.site.register(Prompt, PromptAdmin)
admin.site.register(Entry, EntryAdmin)