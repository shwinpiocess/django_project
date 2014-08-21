from django.contrib import admin

from polls.models import Poll, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class PollAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question']
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question', 'pub_date']
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date informatioin', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)