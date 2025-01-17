from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model =Choice
    extra  = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_text'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_text','was_recently_published')
    list_filter = ['pub_text']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)