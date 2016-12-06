from django.contrib import admin


# Register your models here.
from polls.models import Choice, Question, Aboutus

#class ChoiceInline(admin.StackedInline):
class AboutusAdmin(admin.ModelAdmin):
	#fields = ['texting']
	list_filter = ['pub_date']
	search_fields = ['texting']
	list_display = ('texting','pub_date', 'was_published_recently')
	fieldsets = [
        (None,               {'fields': ['texting']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 3


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}), #,'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('choice_text',)
	#list_filter = ('choice_text','pub_date')
	search_fields = ['choice_text']

#admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
